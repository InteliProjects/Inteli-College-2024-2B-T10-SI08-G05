from prefect import task
from classe_create_view import View

@task(name="Create View Movimento Classificado Por Bilhete")
def create_view_movimento_classificado_por_bilhete():
    query = """
    CREATE OR REPLACE VIEW grupo5.view_movimento_classificado_por_bilhete AS
    SELECT 
        mt.cod_bilh AS codigo_bilhete,
        te.tx_movimento AS tipo_bilhete,
        te.tx_lancamento AS classificacao_lancamento,
        COUNT(mt.id_dt_hora_minuto) AS total_movimentos
    FROM 
        grupo5.dimensao_movimento_tempo mt
    JOIN 
        grupo5.dimensao_tipo_embarque te
    ON 
        mt.cod_bilh = te.cod_bilh
    GROUP BY 
        mt.cod_bilh, te.tx_movimento, te.tx_lancamento
    ORDER BY 
        total_movimentos DESC;
    """
    
    view = View(
        name="view_movimento_classificado_por_bilhete",
        query=query
    )
    
    return view.create_view()
