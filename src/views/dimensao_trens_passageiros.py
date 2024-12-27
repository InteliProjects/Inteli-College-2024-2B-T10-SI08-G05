from prefect import task
from classe_create_dim import Dimension

@task(name="Create Table Dimensao Trens Passageiros")
def create_dimensao_trens_passageiros_table():
    dim_create_query = """
    CREATE TABLE IF NOT EXISTS grupo5.dimensao_trens_passageiros (
        no Int32,
        open_time DateTime,
        closed_time DateTime,
        line_id Int32,
        train_id Int32,
        start_station_id Int32,
        station_id Int32,
        next_station_id Int32,
        end_station_id Int32,
        carriage_id Int32,
        door_id Int32,
        in_count Int32,
        out_count Int32,
        command Int32,
        sensor_status Int32
    )
    ENGINE = MergeTree()
    ORDER BY no;
    """
    
    dim_insert_query = """
    INSERT INTO grupo5.dimensao_trens_passageiros
    SELECT
        JSONExtractInt(data_linha, 'No') AS no,
        parseDateTimeBestEffort(trim(JSONExtractString(data_linha, 'Open_Time'))) AS open_time,
        parseDateTimeBestEffort(trim(JSONExtractString(data_linha, 'Closed_Time'))) AS closed_time,
        JSONExtractInt(data_linha, 'Line_ID') AS line_id,
        JSONExtractInt(data_linha, 'Train_ID') AS train_id,
        JSONExtractInt(data_linha, 'StartStation_ID') AS start_station_id,
        JSONExtractInt(data_linha, 'Station_ID') AS station_id,
        JSONExtractInt(data_linha, 'NextStation_ID') AS next_station_id,
        JSONExtractInt(data_linha, 'EndStation_ID') AS end_station_id,
        JSONExtractInt(data_linha, 'Carriage_ID') AS carriage_id,
        JSONExtractInt(data_linha, 'Door_ID') AS door_id,
        JSONExtractInt(data_linha, 'IN') AS in_count,
        JSONExtractInt(data_linha, 'OUT') AS out_count,
        JSONExtractInt(data_linha, 'Command') AS command,
        JSONExtractInt(data_linha, 'SensorSts') AS sensor_status
    FROM
        grupo5.data_ingestion
    WHERE
        data_tag = 'caixapreta/trem_passageiros.parquet';
    """

    dimension = Dimension(
            name="dimensao_trens_passageiros",
            create_query=dim_create_query,
            insert_query=dim_insert_query
        )

    result = dimension.create_and_populate()
    return result
