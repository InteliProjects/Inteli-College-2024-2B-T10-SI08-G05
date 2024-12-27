from prefect import task
from classe_create_dim import Dimension

@task(name="Create Table Dimensao Trens Passageiros")
def create_dimensao_estacoes_table():
    dim_create_query = """
    CREATE TABLE IF NOT EXISTS grupo5.dimensao_estacoes (
        id_estacao Int32,
        tx_prefixo String,
        tx_nome String,
        cd_estacao_bu Int32,
        cluster Int32
    )
    ENGINE = MergeTree()
    ORDER BY id_estacao;
    """

    dim_insert_query = """
    INSERT INTO grupo5.dimensao_estacoes
    SELECT DISTINCT
        JSONExtractInt(data_linha, 'id_estacao') AS id_estacao,
        JSONExtractString(data_linha, 'tx_prefixo') AS tx_prefixo,
        JSONExtractString(data_linha, 'tx_nome') AS tx_nome,
        JSONExtractInt(data_linha, 'cd_estacao_bu') AS cd_estacao_bu,
        JSONExtractInt(data_linha, 'cluster') AS cluster
    FROM
        grupo5.data_ingestion
    WHERE
        data_tag = 'caixapreta/estacao.parquet';
    """

    dimension = Dimension(
        name="dimensao_estacoes",
        create_query=dim_create_query,
        insert_query=dim_insert_query
    )

    result = dimension.create_and_populate()
    return result
