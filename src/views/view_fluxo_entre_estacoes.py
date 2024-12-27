from prefect import task
from classe_create_view import View

@task(name="Create View Fluxo Entre Estacoes")
def create_view_fluxo_entre_estacoes():
    query = """
    CREATE OR REPLACE VIEW grupo5.view_fluxo_entre_estacoes AS
    SELECT 
        start_station_id AS estacao_inicio,
        end_station_id AS estacao_fim,
        SUM(in_count) AS total_entradas,
        SUM(out_count) AS total_saidas
    FROM 
        grupo5.dimensao_trens_passageiros
    GROUP BY 
        start_station_id, end_station_id
    ORDER BY 
        total_entradas DESC;
    """
    
    view = View(
        name="view_fluxo_entre_estacoes",
        query=query
    )

    return view.create_view()
