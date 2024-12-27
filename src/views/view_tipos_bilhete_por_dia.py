from prefect import task
from classe_create_view import View

@task(name="Create View Tipos Bilhete Por Dia")
def create_view_tipos_bilhete_por_dia():
    query = """
    CREATE OR REPLACE VIEW grupo5.view_tipos_bilhete_por_dia AS
    SELECT 
        te.tx_movimento AS tipo_bilhete,
        mt.dt_validacao AS data,
        COUNT(mt.cod_bilh) AS total_uso
    FROM 
        grupo5.dimensao_movimento_tempo mt
    JOIN 
        grupo5.dimensao_tipo_embarque te
        ON mt.cod_bilh = te.cod_bilh
    GROUP BY 
        te.tx_movimento, mt.dt_validacao
    ORDER BY 
        data, total_uso DESC;
    """
    
    view = View(
        name="view_tipos_bilhete_por_dia",
        query=query
    )

    return view.create_view()
