import pytest
from config.connections import get_clickhouse_client

class ViewTester:
    """classe para realizar os testes em views do ClickHouse"""
    
    def __init__(self, client):
        self.client = client

    def check_view_exists(self, view_name):
        """verifica se a view existe no banco"""
        # Arrange
        query = f"EXISTS TABLE grupo5.{view_name}"
        
        # Act
        result = self.client.execute(query)
        
        # Assert
        return result[0][0] == 1  # retorna True se a view existe


@pytest.fixture(scope="module")
def view_tester():
    """o fixture que retorna uma instância do ViewTester"""
    client = get_clickhouse_client()
    tester = ViewTester(client)
    yield tester


class TestViews:
    """classe para agrupar os testes de views"""
    
    def test_view_fluxo_entre_estacoes(self, view_tester):
        # Arrange
        view_name = "view_fluxo_entre_estacoes"
        
        # Act & Assert
        assert view_tester.check_view_exists(view_name), \
            f"A view `{view_name}` não foi criada."

    def test_view_heatmap_pessoas_por_linha(self, view_tester):
        # Arrange
        view_name = "view_heatmap_pessoas_por_linha"
        
        # Act & Assert
        assert view_tester.check_view_exists(view_name), \
            f"A view `{view_name}` não foi criada."

    def test_view_media_intervalo_operacao_por_dia(self, view_tester):
        # Arrange
        view_name = "view_media_intervalo_operacao_por_dia"
        
        # Act & Assert
        assert view_tester.check_view_exists(view_name), \
            f"A view `{view_name}` não foi criada."

    def test_view_media_tempo_porta_aberta(self, view_tester):
        # Arrange
        view_name = "view_media_tempo_porta_aberta"
        
        # Act & Assert
        assert view_tester.check_view_exists(view_name), \
            f"A view `{view_name}` não foi criada."

    def test_view_movimento_classificado_por_bilhete(self, view_tester):
        # Arrange
        view_name = "view_movimento_classificado_por_bilhete"
        
        # Act & Assert
        assert view_tester.check_view_exists(view_name), \
            f"A view `{view_name}` não foi criada."

    def test_view_sensores_por_data(self, view_tester):
        # Arrange
        view_name = "view_sensores_por_data"
        
        # Act & Assert
        assert view_tester.check_view_exists(view_name), \
            f"A view `{view_name}` não foi criada."

    def test_view_tipos_bilhete_abundantes(self, view_tester):
        # Arrange
        view_name = "view_tipos_bilhete_abundantes"
        
        # Act & Assert
        assert view_tester.check_view_exists(view_name), \
            f"A view `{view_name}` não foi criada."

    def test_view_tipos_bilhete_por_dia(self, view_tester):
        # Arrange
        view_name = "view_tipos_bilhete_por_dia"
        
        # Act & Assert
        assert view_tester.check_view_exists(view_name), \
            f"A view `{view_name}` não foi criada."

    def test_view_tipos_bilhete_por_semana(self, view_tester):
        # Arrange
        view_name = "view_tipos_bilhete_por_semana"
        
        # Act & Assert
        assert view_tester.check_view_exists(view_name), \
            f"A view `{view_name}` não foi criada."
