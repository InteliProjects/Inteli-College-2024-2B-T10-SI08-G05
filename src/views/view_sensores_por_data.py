from prefect import task
from classe_create_view import View

@task(name="Create View Sensores por Data")
def create_view_sensores_por_data():
    query = """
    CREATE OR REPLACE VIEW grupo5.view_sensores_por_data AS
    SELECT 
        toDate(open_time) AS data,
        line_id,
        sensor_status,
        command,
        COUNT(*) AS total_eventos,
        SUM(in_count) AS total_entradas,
        SUM(out_count) AS total_saidas
    FROM 
        grupo5.dimensao_trens_passageiros
    GROUP BY 
        data, line_id, sensor_status, command
    ORDER BY 
        data, line_id, sensor_status, command;
    """

    view = View(
        name="view_sensores_por_data",
        query=query
    )

    return view.create_view()
