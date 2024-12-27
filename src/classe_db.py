from config.connections import get_clickhouse_client
import logging

class DatabaseObject:
    def __init__(self, name: str, query: str):
        self.name = name
        self.query = query
        self.client = get_clickhouse_client()

    def log(self, message: str, level: str = "info"):
        logger = logging.getLogger(self.name)
        if level == "info":
            logger.info(message)
        elif level == "error":
            logger.error(message)
        else:
            logger.debug(message)

    def execute_query(self):
        try:
            self.client.execute(self.query)
            self.log(f"Query executada com sucesso: {self.query}")
            return f"Query para {self.name} executada com sucesso!"
        except Exception as e:
            self.log(f"Erro ao executar query: {str(e)}", level="error")
            raise

