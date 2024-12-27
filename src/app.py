from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from
import os
from dotenv import load_dotenv
from prefect import flow
from etl.ingest_transform import DataIngestion
from views.dimensao_trens_passageiros import create_dimensao_trens_passageiros_table
from views.dimensao_estacoes import create_dimensao_estacoes_table
from views.dimensao_intervalo_dia import create_dimensao_intervalo_dia_table
from views.dimensao_tipo_embarque import create_dimensao_tipo_embarque_table
from views.dimensao_movimentacao_tempo import create_dimensao_movimento_tempo_table
from clickhouse_driver import Client
from views.view_fluxo_entre_estacoes import create_view_fluxo_entre_estacoes
from views.view_heatmap_pessoas_por_linha import create_view_heatmap_pessoas_por_linha
from views.view_sensores_por_data import create_view_sensores_por_data
from views.view_media_intervalo_operacao_por_dia import create_view_media_intervalo_operacao_por_dia
from views.view_media_tempo_porta_aberta import create_view_media_tempo_porta_aberta
from views.view_movimento_classificado_por_bilhete import create_view_movimento_classificado_por_bilhete
from views.view_tipos_bilhete_abundantes import create_view_tipos_bilhete_abundantes
from views.view_tipos_bilhete_por_dia import create_view_tipos_bilhete_por_dia
from views.view_tipos_bilhete_por_semana import create_view_tipos_bilhete_por_semana

load_dotenv()

app = Flask(__name__)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API de Ingestão de Dados",
        "description": "API para iniciar a ingestão de dados no ClickHouse e registrar métricas no PostgreSQL.",
        "version": "1.0.0"
    },
    "securityDefinitions": {
        "ApiKeyAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "X-API-KEY",
            "description": "Chave de acesso para autenticação"
        }
    },
    "security": [{"ApiKeyAuth": []}],
}
swagger = Swagger(app, template=swagger_template)

API_KEY = os.getenv("API_KEY")

def require_api_key(f):
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get("X-API-KEY")
        print(f"Chave recebida: {api_key}") 
        if not api_key:
            return jsonify({"error": "Unauthorized - Missing API Key"}), 401
        if api_key.strip().lower() != API_KEY.strip().lower(): 
            return jsonify({"error": "Unauthorized - Invalid API Key"}), 401
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

def get_clickhouse_client():
    try:
        return Client(
            host=os.getenv('CLICKHOUSE_HOST'),
            port=int(os.getenv('CLICKHOUSE_PORT')),
            user=os.getenv('CLICKHOUSE_USER'),
            password=os.getenv('CLICKHOUSE_PASSWORD')
        )
    except Exception as e:
        raise Exception(f"Erro ao conectar ao ClickHouse: {str(e)}")

@app.route('/ingest_data', methods=['POST'])
@swag_from({
    'tags': ['Data Ingestion'],
    'summary': 'Inicia a ingestão de dados',
    'description': 'Inicia a ingestão de dados no ClickHouse e registra métricas no PostgreSQL.',
    'parameters': [
        {
            "name": "X-API-KEY",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Chave de acesso para autenticação"
        }
    ],
    'responses': {
        200: {'description': 'Ingestão realizada com sucesso.'},
        401: {'description': 'Unauthorized - Chave de acesso inválida.'},
    }
})

@require_api_key
def start_ingestion():
    try:
        bucket_name = "perola-negra"  
        ingestion = DataIngestion(bucket_name)  
        ingestion.run_ingestion(bucket_name)  
        return jsonify({"status": "sucesso", "mensagem": "Dados inseridos com sucesso no ClickHouse e métricas registradas no PostgreSQL!"}), 200
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": "Erro ao processar ingestão de dados.", "detalhes": str(e)}), 500

@app.route('/dimensao-trens-passageiros-flow', methods=['POST'])
@swag_from({
    'tags': ['Flows Dimensões'],
    'summary': 'Criação de view para passageiros',
    'description': 'Executa o fluxo para criar uma view com dados de passageiros.',
    'responses': {
        200: {'description': 'View criada com sucesso.'},
        500: {'description': 'Erro ao criar a view.'},
    }
})

@flow(name="dimensao-trens-passageiros-flow")
def trens_passageiros_flow():
    try:
        resultado = create_dimensao_trens_passageiros_table()
        return jsonify({"status": "sucesso", "mensagem": resultado})
    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)}), 500
    

@app.route('/dimensao-estacoes-flow', methods=['POST'])
@swag_from({
    'tags': ['Flows Dimensões'],
    'summary': 'Criação de view para passageiros',
    'description': 'Executa o fluxo para criar uma view com dados de passageiros.',
    'responses': {
        200: {'description': 'View criada com sucesso.'},
        500: {'description': 'Erro ao criar a view.'},
    }
})

@flow(name="dimensao-estacoes-flow")
def dimensao_estacoes_flow():
    try:
        resultado = create_dimensao_estacoes_table()
        return jsonify({"status": "sucesso", "mensagem": resultado})
    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)}), 500
    
@app.route('/dimensao-intervalo-dia-flow', methods=['POST'])
@swag_from({
    'tags': ['Flows Dimensões'],
    'summary': 'Criação de view para passageiros',
    'description': 'Executa o fluxo para criar uma view com dados de passageiros.',
    'responses': {
        200: {'description': 'View criada com sucesso.'},
        500: {'description': 'Erro ao criar a view.'},
    }
})

@flow(name="dimensao-intervalo-dia-flow")
def dimensao_intervalo_dia_flow():
    try:
        resultado = create_dimensao_intervalo_dia_table()
        return jsonify({"status": "sucesso", "mensagem": resultado})
    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)}), 500
    
@app.route('/dimensao-tipo-embarque-flow', methods=['POST'])
@swag_from({
    'tags': ['Flows Dimensões'],
    'summary': 'Criação de view para passageiros',
    'description': 'Executa o fluxo para criar uma view com dados de passageiros.',
    'responses': {
        200: {'description': 'View criada com sucesso.'},
        500: {'description': 'Erro ao criar a view.'},
    }
})

@flow(name="dimensao-tipo-embarque-flow")
def dimensao_tipo_embarque_flow():
    try:
        resultado = create_dimensao_tipo_embarque_table()
        return jsonify({"status": "sucesso", "mensagem": resultado})
    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)}), 500
    
@app.route('/sensores-por-data-view', methods=['POST'])
@swag_from({
    'tags': ['Flows das Views'],
    'summary': 'Criação de view para análise de sensores',
    'description': 'Executa o fluxo para criar uma view com dados de sensores estratégicos, permitindo gráficos com filtros por data.',
    'responses': {
        200: {'description': 'View criada com sucesso.'},
        500: {'description': 'Erro ao criar a view.'},
    }
})
@flow(name="sensores-por-data-flow")
def sensores_por_data_flow():
    try:
        resultado = create_view_sensores_por_data()
        return jsonify({"status": "sucesso", "mensagem": resultado})
    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)}), 500

    
@app.route('/dimensao-movimentacao-tempo-flow', methods=['POST'])
@swag_from({
    'tags': ['Flows Dimensões'],
    'summary': 'Criação de view para passageiros',
    'description': 'Executa o fluxo para criar uma view com dados de passageiros.',
    'responses': {
        200: {'description': 'View criada com sucesso.'},
        500: {'description': 'Erro ao criar a view.'},
    }
})

@flow(name="dimensao-movimentacao-tempo-flow")
def dimensao_movimento_tempo_flow():
    try:
        resultado = create_dimensao_movimento_tempo_table()
        return jsonify({"status": "sucesso", "mensagem": resultado})
    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)}), 500

@app.route('/fluxo-entre-estacoes-flow', methods=['POST'])
@swag_from({
    'tags': ['Flows das Views'],
    'summary': 'Criação de view para fluxo entre estações',
    'description': 'Executa o fluxo para criar uma view com o fluxo entre estações.',
    'responses': {
        200: {'description': 'View criada com sucesso.'},
        500: {'description': 'Erro ao criar a view.'},
    }
})

@flow(name="fluxo-entre-estacoes-flow")
def fluxo_entre_estacoes_flow():
    try:
        resultado = create_view_fluxo_entre_estacoes()
        return jsonify({"status": "sucesso", "mensagem": resultado})
    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)}), 500

@app.route('/heatmap-pessoas-por-linha-flow', methods=['POST'])
@swag_from({
    'tags': ['Flows das Views'],
    'summary': 'Criação de view para heatmap de pessoas por linha',
    'description': 'Executa o fluxo para criar uma view com o heatmap de movimentações de pessoas por linha e horário.',
    'responses': {
        200: {'description': 'View criada com sucesso.'},
        500: {'description': 'Erro ao criar a view.'},
    }
})

@flow(name="heatmap-pessoas-por-linha-flow")
def heatmap_pessoas_por_linha_flow():
    try:
        resultado = create_view_heatmap_pessoas_por_linha()
        return jsonify({"status": "sucesso", "mensagem": resultado})
    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)}), 500

@app.route('/media-intervalo-operacao-por-dia-flow', methods=['POST'])
@swag_from({
    'tags': ['Flows das Views'],
    'summary': 'Criação de view para média do intervalo de operação por dia',
    'description': 'Executa o fluxo para criar uma view com a média do intervalo de operação por dia e hora.',
    'responses': {
        200: {'description': 'View criada com sucesso.'},
        500: {'description': 'Erro ao criar a view.'},
    }
})

@flow(name="media-intervalo-operacao-por-dia-flow")
def media_intervalo_operacao_por_dia_flow():
    try:
        resultado = create_view_media_intervalo_operacao_por_dia()
        return jsonify({"status": "sucesso", "mensagem": resultado})
    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)}), 500
      
@app.route('/media-tempo-porta-aberta-flow', methods=['POST'])
@swag_from({
    'tags': ['Flows das Views'],
    'summary': 'Criação de view para média de tempo com porta aberta',
    'description': 'Executa o fluxo para criar uma view com a média de tempo que a porta fica aberta por data e linha.',
    'responses': {
        200: {'description': 'View criada com sucesso.'},
        500: {'description': 'Erro ao criar a view.'},
    }
})

@flow(name="media-tempo-porta-aberta-flow")
def media_tempo_porta_aberta_flow():
    try:
        resultado = create_view_media_tempo_porta_aberta()
        return jsonify({"status": "sucesso", "mensagem": resultado})
    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)}), 500

@app.route('/movimento-classificado-por-bilhete-flow', methods=['POST'])
@swag_from({
    'tags': ['Flows das Views'],
    'summary': 'Criação de view para movimento classificado por bilhete',
    'description': 'Executa o fluxo para criar uma view com os movimentos classificados por tipo de bilhete e lançamento.',
    'responses': {
        200: {'description': 'View criada com sucesso.'},
        500: {'description': 'Erro ao criar a view.'},
    }
})

@flow(name="movimento-classificado-por-bilhete-flow")
def movimento_classificado_por_bilhete_flow():
    try:
        resultado = create_view_movimento_classificado_por_bilhete()
        return jsonify({"status": "sucesso", "mensagem": resultado})
    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)}), 500
    
@app.route('/tipos-bilhete-abundantes-flow', methods=['POST'])
@swag_from({
    'tags': ['Flows das Views'],
    'summary': 'Criação de view para tipos de bilhete mais usados',
    'description': 'Executa o fluxo para criar uma view com os tipos de bilhete mais utilizados ordenados pelo total de uso.',
    'responses': {
        200: {'description': 'View criada com sucesso.'},
        500: {'description': 'Erro ao criar a view.'},
    }
})

@flow(name="tipos-bilhete-abundantes-flow")
def tipos_bilhete_abundantes_flow():
    try:
        resultado = create_view_tipos_bilhete_abundantes()
        return jsonify({"status": "sucesso", "mensagem": resultado})
    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)}), 500

@app.route('/tipos-bilhete-por-dia-flow', methods=['POST'])
@swag_from({
    'tags': ['Flows das Views'],
    'summary': 'Criação de view para tipos de bilhete por dia',
    'description': 'Executa o fluxo para criar uma view com os tipos de bilhete usados por dia, ordenados pelo total de uso.',
    'responses': {
        200: {'description': 'View criada com sucesso.'},
        500: {'description': 'Erro ao criar a view.'},
    }
})

@flow(name="tipos-bilhete-por-dia-flow")
def tipos_bilhete_por_dia_flow():
    try:
        resultado = create_view_tipos_bilhete_por_dia()
        return jsonify({"status": "sucesso", "mensagem": resultado})
    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)}), 500
    
@app.route('/tipos-bilhete-por-semana-flow', methods=['POST'])
@swag_from({
    'tags': ['Flows das Views'],
    'summary': 'Criação de view para tipos de bilhete por semana',
    'description': 'Executa o fluxo para criar uma view com os tipos de bilhete usados por semana, agrupados por tipo de dia e data.',
    'responses': {
        200: {'description': 'View criada com sucesso.'},
        500: {'description': 'Erro ao criar a view.'},
    }
})

@flow(name="tipos-bilhete-por-semana-flow")
def tipos_bilhete_por_semana_flow():
    try:
        resultado = create_view_tipos_bilhete_por_semana()
        return jsonify({"status": "sucesso", "mensagem": resultado})
    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)}), 500

@app.route('/dados/view_fluxo_entre_estacoes', methods=['GET'])
@swag_from({
    'tags': ['Consultas'],
    'summary': 'Obter dados de fluxo entre estações',
    'description': 'Consulta os dados da view `view_fluxo_entre_estacoes` no ClickHouse.',
    'parameters': [
        {
            "name": "X-API-KEY",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Chave de acesso para autenticação"
        }
    ],
    'responses': {
        200: {'description': 'Dados retornados com sucesso.'},
        401: {'description': 'Unauthorized - API Key ausente ou inválida.'},
        500: {'description': 'Erro ao obter os dados.'},
    }
})

@require_api_key
def get_view_fluxo_entre_estacoes():
    try:
        client = get_clickhouse_client()
        query = "SELECT estacao_inicio, estacao_fim, total_entradas, total_saidas FROM grupo5.view_fluxo_entre_estacoes;"
        result = client.execute(query)
        columns = ["estacao_inicio", "estacao_fim", "total_entradas", "total_saidas"]
        data = [dict(zip(columns, row)) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": "Erro ao obter os dados.", "detalhes": str(e)}), 500

@app.route('/dados/view_heatmap_pessoas_por_linha', methods=['GET'])
@swag_from({
    'tags': ['Consultas'],
    'summary': 'Obter dados de heatmap de pessoas por linha',
    'description': 'Consulta os dados da view `view_heatmap_pessoas_por_linha` no ClickHouse.',
    'parameters': [
        {
            "name": "X-API-KEY",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Chave de acesso para autenticação"
        }
    ],
    'responses': {
        200: {'description': 'Dados retornados com sucesso.'},
        401: {'description': 'Unauthorized - API Key ausente ou inválida.'},
        500: {'description': 'Erro ao obter os dados.'},
    }
})

@require_api_key
def get_view_heatmap_pessoas_por_linha():
    try:
        client = get_clickhouse_client()
        query = """
            SELECT 
                linha, 
                estacao, 
                dia, 
                hora, 
                SUM(total_entradas) AS total_entradas, 
                SUM(total_saidas) AS total_saidas, 
                SUM(total_movimentacoes) AS total_movimentacoes, 
                SUM(fluxo_liquido) AS fluxo_liquido 
            FROM grupo5.view_heatmap_pessoas_por_linha
            GROUP BY linha, estacao, dia, hora
            ORDER BY dia, hora;
        """
        result = client.execute(query)
        columns = ["linha", "estacao", "dia", "hora", "total_entradas", "total_saidas", "total_movimentacoes", "fluxo_liquido"]
        data = [dict(zip(columns, row)) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": "Erro ao obter os dados.", "detalhes": str(e)}), 500

@app.route('/dados/view_media_intervalo_operacao_por_dia', methods=['GET'])
@swag_from({
    'tags': ['Consultas'],
    'summary': 'Obter dados de intervalo médio por dia',
    'description': 'Consulta os dados da view `view_media_intervalo_operacao_por_dia` no ClickHouse.',
    'parameters': [
        {
            "name": "X-API-KEY",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Chave de acesso para autenticação"
        }
    ],
    'responses': {
        200: {'description': 'Dados retornados com sucesso.'},
        401: {'description': 'Unauthorized - API Key ausente ou inválida.'},
        500: {'description': 'Erro ao obter os dados.'},
    }
})

@require_api_key
def get_view_media_intervalo_operacao_por_dia():
    try:
        client = get_clickhouse_client()
        query = "SELECT data, hora, dia_da_semana, media_intervalo_operacao_segundos FROM grupo5.view_media_intervalo_operacao_por_dia;"
        result = client.execute(query)
        columns = ["data", "hora", "dia_da_semana", "media_intervalo_operacao_segundos"]
        data = [dict(zip(columns, row)) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": "Erro ao obter os dados.", "detalhes": str(e)}), 500


@app.route('/dados/view_media_tempo_porta_aberta', methods=['GET'])
@swag_from({
    'tags': ['Consultas'],
    'summary': 'Obter dados de tempo médio de portas abertas',
    'description': 'Consulta os dados da view `view_media_tempo_porta_aberta` no ClickHouse.',
    'parameters': [
        {
            "name": "X-API-KEY",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Chave de acesso para autenticação"
        }
    ],
    'responses': {
        200: {'description': 'Dados retornados com sucesso.'},
        401: {'description': 'Unauthorized - API Key ausente ou inválida.'},
        500: {'description': 'Erro ao obter os dados.'},
    }
})

@require_api_key
def get_view_media_tempo_porta_aberta():
    try:
        client = get_clickhouse_client()
        query = "SELECT data, linha, media_tempo_porta_aberta_segundos FROM grupo5.view_media_tempo_porta_aberta;"
        result = client.execute(query)
        columns = ["data", "linha", "media_tempo_porta_aberta_segundos"]
        data = [dict(zip(columns, row)) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": "Erro ao obter os dados.", "detalhes": str(e)}), 500


@app.route('/dados/view_movimento_classificado_por_bilhete', methods=['GET'])
@swag_from({
    'tags': ['Consultas'],
    'summary': 'Obter dados de movimento classificado por bilhete',
    'description': 'Consulta os dados da view `view_movimento_classificado_por_bilhete` no ClickHouse.',
    'parameters': [
        {
            "name": "X-API-KEY",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Chave de acesso para autenticação"
        }
    ],
    'responses': {
        200: {'description': 'Dados retornados com sucesso.'},
        401: {'description': 'Unauthorized - API Key ausente ou inválida.'},
        500: {'description': 'Erro ao obter os dados.'},
    }
})

@require_api_key
def get_view_movimento_classificado_por_bilhete():
    try:
        client = get_clickhouse_client()
        query = "SELECT codigo_bilhete, tipo_bilhete, classificacao_lancamento, total_movimentos FROM grupo5.view_movimento_classificado_por_bilhete;"
        result = client.execute(query)
        columns = ["codigo_bilhete", "tipo_bilhete", "classificacao_lancamento", "total_movimentos"]
        data = [dict(zip(columns, row)) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": "Erro ao obter os dados.", "detalhes": str(e)}), 500


@app.route('/dados/view_tipos_bilhete_abundantes', methods=['GET'])
@swag_from({
    'tags': ['Consultas'],
    'summary': 'Obter dados de tipos de bilhete abundantes',
    'description': 'Consulta os dados da view `view_tipos_bilhete_abundantes` no ClickHouse.',
    'parameters': [
        {
            "name": "X-API-KEY",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Chave de acesso para autenticação"
        }
    ],
    'responses': {
        200: {'description': 'Dados retornados com sucesso.'},
        401: {'description': 'Unauthorized - API Key ausente ou inválida.'},
        500: {'description': 'Erro ao obter os dados.'},
    }
})

@require_api_key
def get_view_tipos_bilhete_abundantes():
    try:
        client = get_clickhouse_client()
        query = "SELECT tipo_bilhete, total_uso FROM grupo5.view_tipos_bilhete_abundantes;"
        result = client.execute(query)
        columns = ["tipo_bilhete", "total_uso"]
        data = [dict(zip(columns, row)) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": "Erro ao obter os dados.", "detalhes": str(e)}), 500


@app.route('/dados/view_tipos_bilhete_por_dia', methods=['GET'])
@swag_from({
    'tags': ['Consultas'],
    'summary': 'Obter dados de tipos de bilhete por dia',
    'description': 'Consulta os dados da view `view_tipos_bilhete_por_dia` no ClickHouse.',
    'parameters': [
        {
            "name": "X-API-KEY",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Chave de acesso para autenticação"
        }
    ],
    'responses': {
        200: {'description': 'Dados retornados com sucesso.'},
        401: {'description': 'Unauthorized - API Key ausente ou inválida.'},
        500: {'description': 'Erro ao obter os dados.'},
    }
})

@require_api_key
def get_view_tipos_bilhete_por_dia():
    try:
        client = get_clickhouse_client()
        query = "SELECT tipo_bilhete, data, total_uso FROM grupo5.view_tipos_bilhete_por_dia;"
        result = client.execute(query)
        columns = ["tipo_bilhete", "data", "total_uso"]
        data = [dict(zip(columns, row)) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": "Erro ao obter os dados.", "detalhes": str(e)}), 500


@app.route('/dados/view_tipos_bilhete_por_semana', methods=['GET'])
@swag_from({
    'tags': ['Consultas'],
    'summary': 'Obter dados de tipos de bilhete por semana',
    'description': 'Consulta os dados da view `view_tipos_bilhete_por_semana` no ClickHouse.',
    'parameters': [
        {
            "name": "X-API-KEY",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Chave de acesso para autenticação"
        }
    ],
    'responses': {
        200: {'description': 'Dados retornados com sucesso.'},
        401: {'description': 'Unauthorized - API Key ausente ou inválida.'},
        500: {'description': 'Erro ao obter os dados.'},
    }
})

@require_api_key
def get_view_tipos_bilhete_por_semana():
    try:
        client = get_clickhouse_client()
        query = "SELECT tipo_bilhete, data, tipo_dia, total_uso FROM grupo5.view_tipos_bilhete_por_semana;"
        result = client.execute(query)
        columns = ["tipo_bilhete", "data", "tipo_dia", "total_uso"]
        data = [dict(zip(columns, row)) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": "Erro ao obter os dados.", "detalhes": str(e)}), 500
    
@app.route('/dados/view-sensores-por-data', methods=['GET'])
@swag_from({
    'tags': ['Consultas'],
    'summary': 'Obter dados da view de sensores por data',
    'description': 'Consulta os dados da view `view_sensores_por_data` no ClickHouse.',
    'parameters': [
        {
            "name": "X-API-KEY",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Chave de acesso para autenticação"
        }
    ],
    'responses': {
        200: {'description': 'Dados retornados com sucesso.'},
        401: {'description': 'Unauthorized - API Key ausente ou inválida.'},
        500: {'description': 'Erro ao obter os dados.'},
    }
})
@require_api_key
def get_view_sensores_por_data():
    try:
        client = get_clickhouse_client()
        query = """
        SELECT 
            data, 
            line_id,
            sensor_status, 
            command, 
            total_eventos, 
            total_entradas, 
            total_saidas 
        FROM 
            grupo5.view_sensores_por_data;
        """
        result = client.execute(query)
        columns = ["data", "line_id", "sensor_status", "command", "total_eventos", "total_entradas", "total_saidas"]
        data = [dict(zip(columns, row)) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": "Erro ao obter os dados.", "detalhes": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)