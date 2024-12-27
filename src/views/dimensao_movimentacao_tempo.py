from prefect import task
from classe_create_dim import Dimension

@task(name="Create Table Dimensao Movimentação Tempo")
def create_dimensao_movimento_tempo_table():
    dim_create_query = """
    CREATE TABLE IF NOT EXISTS grupo5.dimensao_movimento_tempo (
        id_dt_hora_minuto Int32,
        cod_bilh Int32,
        cd_estac_bu Int32,
        dt_validacao Date,
        total_validacoes Int32,
        tipo_dia String,
        diff_validacoes Int32
    )
    ENGINE = MergeTree()
    ORDER BY (id_dt_hora_minuto, dt_validacao);
    """
    dim_insert_query = """
    INSERT INTO grupo5.dimensao_movimento_tempo
    SELECT
        JSONExtractInt(data_linha, 'id_dt_hora_minuto') AS id_dt_hora_minuto,
        JSONExtractInt(data_linha, 'cod_bilh') AS cod_bilh,
        JSONExtractInt(data_linha, 'cd_estac_bu') AS cd_estac_bu,
        parseDateTimeBestEffort(JSONExtractString(data_linha, 'dt_validacao')) AS dt_validacao,
        JSONExtractInt(data_linha, 'total_validacoes') AS total_validacoes,
        JSONExtractString(data_linha, 'tipo_dia') AS tipo_dia,
        NULL AS diff_validacoes
    FROM
        grupo5.data_ingestion
    WHERE
        data_tag = 'caixapreta/mov_periodo.parquet';
    """

    dimension = Dimension(
        name="dimensao_movimentacao_tempo",
        create_query=dim_create_query,
        insert_query=dim_insert_query
    )

    result = dimension.create_and_populate()
    return result

