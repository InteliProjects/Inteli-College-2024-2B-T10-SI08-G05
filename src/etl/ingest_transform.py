from prefect import task, flow, get_run_logger
from datetime import datetime, timezone
import json
import io
import pyarrow.parquet as pq
from config.connections import get_s3_client, get_clickhouse_client
from config.observability import log_observability
from config.schemas.models import (
    TremPassageirosModel, IntervalosDiaModel, EstacaoModel, MovPeriodoModel, TipoEmbarqueModel
)

class DataIngestion:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3 = get_s3_client()
        self.client = get_clickhouse_client()

    @flow(name="Ingest Data Flow")
    def run_ingestion(self, bucket_name):
        logger = get_run_logger()
        start_time = datetime.now(timezone.utc)

        ingestion = DataIngestion(bucket_name)
        ingestion.create_table()

        parquet_files = ingestion.list_parquet_files()
        for file_key in parquet_files:
            rows = ingestion.process_parquet_file(file_key)
            if rows:
                ingestion.insert_to_clickhouse(rows)

        end_time = datetime.now(timezone.utc)
        details = f"Ingested data from {len(parquet_files)} files in bucket {bucket_name}"
        log_observability("ingest_data", start_time, end_time, details)
        logger.info(details)

    def create_table(self):
        self.client.execute('''
            CREATE TABLE IF NOT EXISTS grupo5.data_ingestion (
                data_ingestao UInt32,
                data_linha String,  
                data_tag String
            ) ENGINE = MergeTree()
            ORDER BY data_ingestao
        ''')

    def list_parquet_files(self):
        response = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix='caixapreta/')
        return [obj['Key'] for obj in response.get('Contents', []) if obj['Key'].endswith('.parquet')]

    def read_parquet_file(self, file_key):
        obj = self.s3.get_object(Bucket=self.bucket_name, Key=file_key)
        buffer = io.BytesIO(obj['Body'].read())
        return pq.ParquetFile(buffer)

    def process_parquet_file(self, file_key):
        parquet_data = self.read_parquet_file(file_key)

        rows = []
        data_tag = file_key

        for batch in parquet_data.iter_batches():
            batch_rows = self.process_batch(batch, data_tag)
            rows.extend(batch_rows)
        return rows

    def process_batch(self, batch, data_tag):
        logger = get_run_logger()
        rows = []

        models_map = {
            "trem_passageiros": TremPassageirosModel,
            "intervalos_dia": IntervalosDiaModel,
            "estacao": EstacaoModel,
            "mov_periodo": MovPeriodoModel,
            "tipo_embarque": TipoEmbarqueModel,
        }

        for row in batch.to_pylist():
            try:
                data_linha = json.dumps(self.convert_to_unix_time(row))
                data_ingestao = int(datetime.now(timezone.utc).timestamp())

                model_class = models_map.get(data_tag)
                if model_class:
                    model_class(**row)  
                else:
                    logger.warning(f"Unknown data_tag format: {data_tag}")
                    continue
                rows.append((data_ingestao, data_linha, data_tag))

            except ValueError as ve:
                logger.error(f"Data validation error: {ve}")
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
        return rows

    @staticmethod
    def convert_to_unix_time(row):
        result = {}
        for k, v in row.items():
            if isinstance(v, datetime):
                result[k] = int(v.timestamp())
            elif k == "timestamp_field":  
                raise ValueError(f"Expected a datetime object in field '{k}'")
            else:
                result[k] = v  
        return result

    def insert_to_clickhouse(self, rows):
        if not rows:
            raise ValueError("Cannot insert empty rows into ClickHouse")
        self.client.execute(
            "INSERT INTO grupo5.data_ingestion (data_ingestao, data_linha, data_tag) VALUES",
            rows
        )