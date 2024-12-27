from prefect import task
from classe_create_view import View

@task(name="Create View Media Tempo Porta Aberta")
def create_view_media_tempo_porta_aberta():
    query = """
    CREATE OR REPLACE VIEW grupo5.view_media_tempo_porta_aberta AS
    SELECT
        CAST(open_time AS DATE) AS data,
        line_id AS linha,
        AVG(closed_time - open_time) AS media_tempo_porta_aberta_segundos
    FROM 
        grupo5.dimensao_trens_passageiros
    GROUP BY 
        CAST(open_time AS DATE), line_id
    ORDER BY 
        data, linha;
    """
    
    view = View(
        name="view_media_tempo_porta_aberta",
        query=query
    )

    return view.create_view()
