from prefect import task
from classe_create_dim import Dimension

@task(name="Create Table Dimensao Tipo Embarque")
def create_dimensao_tipo_embarque_table():
    dim_create_query = """
    CREATE TABLE IF NOT EXISTS grupo5.dimensao_tipo_embarque (
        cd_tipo_embarque Int32,
        tx_movimento String,
        cod_bilh Int32,
        cd_tipo_lancamento_fk Int32,
        tx_lancamento String
    )
    ENGINE = MergeTree()
    ORDER BY cd_tipo_embarque;
    
    """
    dim_insert_query = """
    INSERT INTO grupo5.dimensao_tipo_embarque
    SELECT
        JSONExtractInt(data_linha, 'cd_tipo_embarque') AS cd_tipo_embarque,
        JSONExtractString(data_linha, 'tx_movimento') AS tx_movimento,
        JSONExtractInt(data_linha, 'cod_bilh') AS cod_bilh,
        JSONExtractInt(data_linha, 'cd_tipo_lancamento_fk') AS cd_tipo_lancamento_fk,
        JSONExtractString(data_linha, 'tx_lancamento') AS tx_lancamento
    FROM
        grupo5.data_ingestion
    WHERE
        data_tag = 'caixapreta/tipo_embarque.parquet';
    """

    dimension = Dimension(
        name="dimensao_tipo_embarque",
        create_query=dim_create_query,
        insert_query=dim_insert_query
    )

    result = dimension.create_and_populate()
    return result

