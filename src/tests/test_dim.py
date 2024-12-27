import pytest
from unittest.mock import MagicMock, patch
from classe_create_dim import Dimension
import os

# Mock da fixture para variáveis de ambiente
@pytest.fixture(autouse=True)
def mock_env_vars():
    # Caso haja a necessidade de mockar as variáveis de ambiente
    with patch.dict(os.environ, {
        "AWS_ACCESS_KEY": "fake_access_key",
        "AWS_SECRET_KEY": "fake_secret_key",
        "AWS_SESSION_TOKEN": "fake_aws_session_token",
        "AWS_REGION": "us-east-1",
        "CLICKHOUSE_HOST": "localhost",
        "CLICKHOUSE_PORT": "9000",
        "CLICKHOUSE_USER": "user",
        "CLICKHOUSE_PASSWORD": "password",
        "POSTGRES_HOST": "localhost",
        "POSTGRES_PORT": "5432",
        "POSTGRES_DB": "mydb",
        "POSTGRES_USER": "postgres",
        "POSTGRES_PASSWORD": "postgres_password",
        "API_KEY": "fake_api_key"
    }):
        yield

# Mock do cliente para a classe Dimension
@pytest.fixture
def mock_client():
    return MagicMock()

def test_create_and_populate(mock_client):
    # Consultas de criação e inserção para o teste
    dim_create_query = "CREATE TABLE IF NOT EXISTS grupo5.dimensao_estacoes (id_estacao Int32, ...)"
    dim_insert_query = "INSERT INTO grupo5.dimensao_estacoes SELECT DISTINCT ..."

    # Instancia a classe com o mock do client
    dimension = Dimension(name="dimensao_estacoes", create_query=dim_create_query, insert_query=dim_insert_query)
    dimension.client = mock_client  # Atribui o mock do client à instância

    # Ação: Chama o método que deve criar a tabela e inserir os dados
    result = dimension.create_and_populate()

    # Verificação: Verifica se a consulta de inserção foi chamada
    mock_client.execute.assert_called_with(dim_insert_query)

    # Verifica se a mensagem de sucesso foi retornada
    assert "Dados inseridos com sucesso" in result

def test_create_and_populate_error(mock_client):
    # Consultas de criação e inserção para o teste
    dim_create_query = "CREATE TABLE IF NOT EXISTS grupo5.dimensao_estacoes (id_estacao Int32, ...)"
    dim_insert_query = "INSERT INTO grupo5.dimensao_estacoes SELECT DISTINCT ..."

    # Instancia a classe com o mock do client
    dimension = Dimension(name="dimensao_estacoes", create_query=dim_create_query, insert_query=dim_insert_query)
    dimension.client = mock_client  # Atribui o mock do client à instância

    # Simula um erro na execução da consulta
    dimension.client.execute.side_effect = Exception("Erro ao executar a consulta")

    # Verifica se a exceção é corretamente levantada quando ocorre erro
    with pytest.raises(Exception):
        dimension.create_and_populate()