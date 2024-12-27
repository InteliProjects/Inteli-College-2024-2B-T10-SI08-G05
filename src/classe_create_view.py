from classe_db import DatabaseObject

class View(DatabaseObject):
    def __init__(self, name: str, query: str):
        super().__init__(name, query)

    def create_view(self):
        try:
            self.logger.info(f"Iniciando criação da view: {self.name}")
            create_result = self.execute_query()
            self.logger.info(f"View {self.name} criada com sucesso!")
            return f"{create_result}\nView {self.name} criada com sucesso!"
        except Exception as e:
            self.logger.error(f"Erro ao criar a view {self.name}: {str(e)}")
            raise