from classe_db import DatabaseObject

class Dimension(DatabaseObject):
    def __init__(self, name: str, create_query: str, insert_query: str):
        super().__init__(name, create_query)
        self.insert_query = insert_query

    def create_and_populate(self):
        try:
            self.log("info", f"Iniciando criação e população da dimensão: {self.name}")
            create_result = self.execute_query() 
            self.client.execute(self.insert_query)
            self.log("info", f"Dados inseridos com sucesso na dimensão {self.name}")
            return f"{create_result}\nDados inseridos com sucesso na dimensão {self.name}!"
        except Exception as e:
            self.log("error", f"Erro ao criar ou popular a dimensão {self.name}: {str(e)}")
            raise

