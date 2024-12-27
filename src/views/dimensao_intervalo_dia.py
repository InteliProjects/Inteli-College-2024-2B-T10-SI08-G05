from prefect import task
from classe_create_dim import Dimension

@task(name="Create Table Dimensao Intevalo Dia")
def create_dimensao_intervalo_dia_table():
    dim_create_query = """
    CREATE TABLE IF NOT EXISTS grupo5.dimensao_intervalo_dia (
        id_dt_hora_minuto Int32,
        dt_hora_minuto Int64,
        hora_ini String,
        hora_fim String,
        intervalo_segundos Int32,
        hour Int32,
        minute Int32,
        day_of_week String
    )
    ENGINE = MergeTree()
    ORDER BY id_dt_hora_minuto;
    
    """
    dim_insert_query = """
    INSERT INTO grupo5.dimensao_intervalo_dia
    SELECT
        JSONExtractInt(data_linha, 'id_dt_hora_minuto') AS id_dt_hora_minuto,
        JSONExtractInt(data_linha, 'dt_hora_minuto') AS dt_hora_minuto,
        JSONExtractString(data_linha, 'hora_ini') AS hora_ini,
        JSONExtractString(data_linha, 'hora_fim') AS hora_fim,
        (toUnixTimestamp(parseDateTimeBestEffort(JSONExtractString(data_linha, 'hora_fim'))) -
        toUnixTimestamp(parseDateTimeBestEffort(JSONExtractString(data_linha, 'hora_ini')))) AS intervalo_segundos,
        JSONExtractInt(data_linha, 'hour') AS hour,
        JSONExtractInt(data_linha, 'minute') AS minute,
        JSONExtractString(data_linha, 'day_of_week') AS day_of_week
    FROM
        grupo5.data_ingestion
    WHERE
        data_tag = 'caixapreta/dmo_anl_vw_intervalos_dia.parquet';
    """

    dimension = Dimension(
        name="dimensao_intervalo_dia",
        create_query=dim_create_query,
        insert_query=dim_insert_query
    )

    result = dimension.create_and_populate()
    return result

