# São testadas todas as funções do ETL nesse código. Sendo elas:
# 1. `create_table`: Cria a tabela no ClickHouse, caso ela ainda não exista.
# 2. `list_parquet_files`: Lista os arquivos Parquet em um bucket S3 que possuem o prefixo especificado.
# 3. `read_parquet_file`: Lê um arquivo Parquet de um bucket S3 e retorna um objeto ParquetFile.
# 4. `process_parquet_file`: Processa um arquivo Parquet, convertendo os dados em linhas prontas para inserção no Clickhouse.
# 5. `process_batch`: Processa um lote de dados de um arquivo Parquet, realizando a validação e transformação das linhas com pydantic.
# 6. `convert_to_unix_time`: Converte campos de timestamp em um dicionário para Unix timestamp, sinalizando erros em valores inválidos.
# 7. `insert_to_clickhouse`: Insere um conjunto de linhas processadas na tabela do ClickHouse.

# Os testes seguem a abordagem "Arrange, Act, Assert":
# - Arrange: Configura os dados ou mocks necessários para o teste.
# - Act: Executa a função a ser testada.
# - Assert: Verifica se o resultado é o esperado ou se os erros são tratados corretamente.

import pytest
import textwrap
from datetime import datetime
from etl.ingest_transform import DataIngestion
from unittest.mock import MagicMock, patch
import pyarrow as pa
import pyarrow.parquet as pq
import io

# Teste para a função `create_table`
# 1. Caso de sucesso (Happy Path): Confirma que a tabela é criada corretamente no ClickHouse.
# 2. Caso de erro: Verifica se um erro é levantado ao tentar criar uma tabela com um comando inválido.

class TestDataIngestion:
    
    def setup_method(self):
        """Configuração inicial para cada teste."""
        self.bucket_name = "test-bucket"
        self.etl = DataIngestion(bucket_name=self.bucket_name)
        self.mock_client = MagicMock()
        self.mock_s3 = MagicMock()

    def test_create_table_happy_path(self):
        # Arrange
        mock_client = MagicMock()
        etl = self.etl
        etl.client = mock_client

        # Act
        etl.create_table()

        # Assert
        expected_query = textwrap.dedent('''\
            CREATE TABLE IF NOT EXISTS grupo5.data_ingestion (
                data_ingestao UInt32,
                data_linha String,
                data_tag String
            ) ENGINE = MergeTree()
            ORDER BY data_ingestao
        ''').strip()

        # Obtendo a query gerada e normalizando espaços e quebras de linha
        actual_query = mock_client.execute.call_args[0][0].strip()

        # Normalizando as strings para comparação
        def normalize_query(query):
            return ' '.join(query.split())

        assert normalize_query(expected_query) == normalize_query(actual_query)

    def test_create_table_error(self):
        """
        Verifica se um erro é tratado ao criar a tabela.
        """
        # Arrange
        mock_client = MagicMock()
        mock_client.execute.side_effect = Exception("Database error")
        
        # Criar a instância do DataIngestion sem passar o client diretamente
        etl = self.etl
        
        # Substituir o client pelo mock
        etl.client = mock_client

        # Act & Assert
        with pytest.raises(Exception, match="Database error"):
            etl.create_table()

    # Teste para a função `list_parquet_files`
    # 1. Caso de sucesso (Happy Path): Confirma que a função retorna uma lista de arquivos Parquet no bucket S3.
    # 2. Caso de erro: Verifica se a função retorna uma lista vazia ou trata corretamente a ausência de arquivos no bucket.

    def test_list_parquet_files_happy_path(self):
        """
        Testa se a função retorna corretamente a lista de arquivos Parquet.
        """
        # Arrange
        mock_s3 = self.mock_s3
        mock_s3.list_objects_v2.return_value = {
            'Contents': [{'Key': 'caixapreta/file1.parquet'}, {'Key': 'caixapreta/file2.parquet'}]
        }
        etl = self.etl
        etl.s3 = mock_s3  

        # Act
        result = etl.list_parquet_files()

        # Assert
        assert result == ['caixapreta/file1.parquet', 'caixapreta/file2.parquet']

    def test_list_parquet_files_error(self):
        """
        Verifica se a função levanta um erro ao não encontrar arquivos Parquet.
        """
        # Arrange
        mock_s3 = self.mock_s3
        mock_s3.list_objects_v2.return_value = {'Contents': []}
        etl = self.etl
        etl.s3 = mock_s3  

        # Act
        result = etl.list_parquet_files()

        # Assert
        assert result == []  

    # Teste para a função `read_parquet_file`
    # 1. Caso de sucesso (Happy Path): Confirma que a função lê corretamente um arquivo Parquet do bucket S3 e retorna um objeto ParquetFile.
    # 2. Caso de erro: Verifica se um erro é levantado ao tentar acessar um arquivo inexistente ou inválido.

    def test_read_parquet_file_happy_path(self):
        """
        Testa a leitura de um arquivo Parquet.
        """
        # Arrange
        mock_s3 = self.mock_s3
        buffer = io.BytesIO()
        
        # Criar tabela de teste em formato Parquet válido
        table = pa.Table.from_pydict({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
        pq.write_table(table, buffer)  # Escrevendo a tabela Parquet no buffer
        buffer.seek(0)  # Reiniciar o ponteiro do buffer para o início

        mock_s3.get_object.return_value = {'Body': buffer}
        etl = self.etl
        etl.s3 = mock_s3

        # Act
        result = etl.read_parquet_file('caixapreta/file1.parquet')

        # Assert
        assert isinstance(result, pq.ParquetFile)

    def test_read_parquet_file_error(self):
        """
        Verifica se a função levanta um erro ao tentar ler um arquivo inexistente.
        """
        # Arrange
        mock_s3 = self.mock_s3
        mock_s3.get_object.side_effect = Exception("File not found")
        etl = self.etl
        etl.s3 = mock_s3  

        # Act & Assert
        with pytest.raises(Exception, match="File not found"):
            etl.read_parquet_file('caixapreta/nonexistent.parquet')


    # Testando a função `convert_to_unix_time`:
    # 1. Caso de sucesso (Happy Path): Confirma que campos datetime são convertidos corretamente.
    # 2. Caso de erro: Verifica se a função levanta um erro ao encontrar valores inválidos.

    def test_convert_to_unix_time_happy_path(self):
        """
        Testa a conversão correta de campos datetime para Unix timestamp.
        """
        # Arrange
        timestamp = datetime(2024, 11, 30, 12, 0)  
        unix_timestamp = int(timestamp.timestamp())  

        input_row = {"timestamp_field": timestamp, "other_field": "value"}  
        expected_output = {"timestamp_field": unix_timestamp, "other_field": "value"}  

        # Act
        result = DataIngestion.convert_to_unix_time(input_row)

        # Assert
        assert result == expected_output

    def test_convert_to_unix_time_error_path(self):
        """
        Testa se a função levanta um ValueError ao encontrar um valor inválido.
        """
        # Arrange
        input_row = {"timestamp_field": "not_a_datetime", "other_field": None}

        # Act & Assert
        with pytest.raises(ValueError, match="Expected a datetime object in field 'timestamp_field'"):
            DataIngestion.convert_to_unix_time(input_row)

    # Testando a função `insert_to_clickhouse`:
    # 1. Caso de sucesso (Happy Path): Insere dados corretamente no banco.
    # 2. Caso de erro: Verifica se um erro é levantado ao tentar inserir uma lista vazia.

    def test_insert_to_clickhouse_happy_path(self):
        """
        Testa se os dados são inseridos corretamente no banco ClickHouse.
        """
        # Arrange
        rows = [(1234567890, '{"key": "value"}', "data_tag")]  

        mock_client = self.mock_s3
        mock_client.execute = MagicMock()  

        ingestion = DataIngestion("mock_bucket") 
        ingestion.client = mock_client  # Substitui o cliente real pelo mock

        # Act
        ingestion.insert_to_clickhouse(rows)

        # Assert
        mock_client.execute.assert_called_once_with(
            "INSERT INTO grupo5.data_ingestion (data_ingestao, data_linha, data_tag) VALUES",
            rows
        )

    @patch("etl.ingest_transform.get_run_logger")
    @patch("etl.ingest_transform.TremPassageirosModel")
    @patch("etl.ingest_transform.DataIngestion.convert_to_unix_time")
    def test_process_batch_happy_path(self, mock_convert, mock_model, mock_logger):
        """
        Testa se os dados de um lote são processados corretamente.
        """
        # Importa DataIngestion após aplicar os patches
        from etl.ingest_transform import DataIngestion

        # Arrange
        mock_batch = MagicMock()
        mock_batch.to_pylist.return_value = [{"field": "value"}]

        # Configurando os mocks
        mock_logger_instance = MagicMock()
        mock_logger.return_value = mock_logger_instance
        mock_convert.return_value = {"field": "value"}
        mock_model.return_value = MagicMock()

        ingestion = DataIngestion("mock_bucket")

        # Act
        rows = ingestion.process_batch(mock_batch, "trem_passageiros")

        # Assert
        assert len(rows) == 1
        assert rows[0][2] == "trem_passageiros"
        mock_model.assert_called_once_with(**{"field": "value"})
        mock_logger_instance.error.assert_not_called()
        mock_logger_instance.warning.assert_not_called()

    @patch("etl.ingest_transform.get_run_logger")
    @patch("etl.ingest_transform.DataIngestion.convert_to_unix_time")
    def test_process_batch_validation_error(self, mock_convert, mock_logger):
        """
        Testa se a função trata erros de validação corretamente.
        """
        # Arrange
        mock_batch = MagicMock()
        mock_batch.to_pylist.return_value = [{"field": "invalid_value"}]

        # Configurando os mocks
        mock_logger_instance = MagicMock()
        mock_logger.return_value = mock_logger_instance
        mock_convert.side_effect = ValueError("Validation Error")

        ingestion = DataIngestion("mock_bucket")

        # Act
        rows = ingestion.process_batch(mock_batch, "trem_passageiros")

        # Assert
        assert rows == []
        mock_logger_instance.error.assert_called_once_with("Data validation error: Validation Error")
        mock_logger_instance.warning.assert_not_called()

    @patch("etl.ingest_transform.get_run_logger")
    @patch("etl.ingest_transform.DataIngestion.convert_to_unix_time")
    def test_process_batch_unknown_tag(self, mock_convert, mock_logger):
        """
        Testa o comportamento ao receber um data_tag desconhecido.
        """
        # Arrange
        mock_batch = MagicMock()
        mock_batch.to_pylist.return_value = [{"field": "value"}]

        # Configurando os mocks
        mock_logger_instance = MagicMock()
        mock_logger.return_value = mock_logger_instance
        mock_convert.return_value = {"field": "value"}

        ingestion = DataIngestion("mock_bucket")

        # Act
        rows = ingestion.process_batch(mock_batch, "unknown_tag")

        # Assert
        assert rows == []
        mock_logger_instance.warning.assert_called_once_with("Unknown data_tag format: unknown_tag")
        mock_logger_instance.error.assert_not_called()

    @patch("etl.ingest_transform.get_run_logger")
    @patch("etl.ingest_transform.TremPassageirosModel")
    @patch("etl.ingest_transform.DataIngestion.convert_to_unix_time")
    def test_process_parquet_file_happy_path(self, mock_convert, mock_model, mock_logger):
        """
        Testa se a função processa um arquivo parquet corretamente.
        """

        # Arrange
        mock_file_key = "test.parquet"
        mock_parquet_data = MagicMock()
        mock_parquet_data.iter_batches.return_value = [MagicMock(), MagicMock()]  # Dois lotes para processamento

        # Configurando os mocks
        mock_logger_instance = MagicMock()
        mock_logger.return_value = mock_logger_instance
        mock_convert.side_effect = [{"field": "value1"}, {"field": "value2"}]
        mock_model.return_value = MagicMock()

        with patch("etl.ingest_transform.DataIngestion.read_parquet_file", return_value=mock_parquet_data):
            with patch("etl.ingest_transform.DataIngestion.process_batch", side_effect=[
                [(123, '{"field": "value1"}', "trem_passageiros")],
                [(456, '{"field": "value2"}', "trem_passageiros")]
            ]):
                ingestion = DataIngestion("mock_bucket")

                # Act
                rows = ingestion.process_parquet_file(mock_file_key)

        # Assert
        assert rows == [
            (123, '{"field": "value1"}', "trem_passageiros"),
            (456, '{"field": "value2"}', "trem_passageiros")
        ]
        mock_logger_instance.error.assert_not_called()
        mock_logger_instance.warning.assert_not_called()

    @patch("etl.ingest_transform.get_run_logger")
    @patch("etl.ingest_transform.DataIngestion.convert_to_unix_time")
    def test_process_parquet_file_error_handling(self, mock_convert, mock_logger):
        """
        Testa se a função lida corretamente com erros ao processar um lote.
        """
        # Arrange
        mock_file_key = "test.parquet"
        mock_parquet_data = MagicMock()
        mock_parquet_data.iter_batches.return_value = [MagicMock()]  # Apenas um lote

        # Configurando os mocks
        mock_logger_instance = MagicMock()
        mock_logger.return_value = mock_logger_instance
        mock_convert.return_value = {"field": "value"}

        with patch("etl.ingest_transform.DataIngestion.read_parquet_file", return_value=mock_parquet_data):
            with patch("etl.ingest_transform.DataIngestion.process_batch", side_effect=Exception("Batch Error")):
                ingestion = DataIngestion("mock_bucket")

                # Act & Assert
                with pytest.raises(Exception, match="Batch Error"):
                    ingestion.process_parquet_file(mock_file_key)

        # Dependendo da implementação, ajuste se o erro é logado
        mock_logger_instance.error.assert_not_called()
        mock_logger_instance.warning.assert_not_called()