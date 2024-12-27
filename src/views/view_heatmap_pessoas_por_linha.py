from prefect import task
from classe_create_view import View

@task(name="Create View Heatmap Pessoas Por Linha") 
def create_view_heatmap_pessoas_por_linha():
    query = """
    CREATE OR REPLACE VIEW grupo5.view_heatmap_pessoas_por_linha AS
    SELECT 
        line_id AS linha,
        station_id AS estacao,
        toDate(open_time) AS dia,  -- Extrai apenas o dia (sem hora)
        EXTRACT(hour FROM open_time) AS hora,  -- Extrai a hora
        SUM(in_count) AS total_entradas,
        SUM(out_count) AS total_saidas,
        SUM(in_count) + SUM(out_count) AS total_movimentacoes,
        SUM(in_count) - SUM(out_count) AS fluxo_liquido -- Entradas - Saídas
    FROM 
        grupo5.dimensao_trens_passageiros
    GROUP BY 
        line_id, 
        station_id,
        toDate(open_time),  
        EXTRACT(hour FROM open_time) 
    ORDER BY 
        linha, 
        estacao, 
        dia, 
        hora;
    """

    view = View(
        name="view_heatmap_pessoas_por_linha",
        query=query
    )
    
    return view.create_view()
