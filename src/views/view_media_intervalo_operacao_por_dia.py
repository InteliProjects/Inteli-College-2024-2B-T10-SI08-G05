from prefect import task
from classe_create_view import View

@task(name="Create View Media Intervalo Operacao Por Dia")
def create_view_media_intervalo_operacao_por_dia():
    query = """
    CREATE OR REPLACE VIEW grupo5.view_media_intervalo_operacao_por_dia AS
    SELECT
        DATE(dt_hora_minuto) AS data,
        hour AS hora,
        day_of_week AS dia_da_semana,
        AVG(intervalo_segundos) AS media_intervalo_operacao_segundos
    FROM 
        grupo5.dimensao_intervalo_dia
    GROUP BY 
        DATE(dt_hora_minuto), hour, day_of_week
    ORDER BY 
        data, hora;
    """
    
    view = View(
        name="view_media_intervalo_operacao_por_dia",
        query=query
    )

    return view.create_view()

