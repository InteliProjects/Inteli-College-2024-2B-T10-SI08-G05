# Explorando Testes 🐟

Bem-vindo ao grande recife do nosso projeto onde testamos tudo no ETL! Assim como Nemo explora o vasto oceano, você está prestes a navegar pelo código, verificar testes e medir a cobertura para garantir que tudo esteja funcionando como esperado. 🌊

## 🗂 Estrutura do Projeto
Antes de mergulharmos nos testes, aqui está uma visão geral da estrutura do nosso recife:

```
src/
├── etl/               # O coração do oceano (nosso módulo principal de ETL)
│   ├── ingest_transform.py
├── tests/             # O lar dos peixes-palhaço (testes que garantem a harmonia do recife)
│   ├── test_etl.py
├── htmlcov/           # Relatórios em HTML (para monitorar o oceano de código)
└── streamlit/         # Interface para visualização
```

O diretório principal para o código é o `etl/`, enquanto os testes estão em `tests/`. Nosso objetivo é garantir que os testes cubram todo o código no diretório `etl/`.

---

## 🧪 Testando o Código
Como Nemo confia em seu pai Marlin para mantê-lo seguro, nós confiamos no `pytest` para validar nosso código.

### 1. Preparando o Ambiente
Certifique-se de que você está no diretório `src` antes de começar:

```bash
cd src
```

Agora, execute os testes com o seguinte comando:

```bash
poetry run pytest
```

Se tudo estiver funcionando, você verá um relatório dos testes no terminal, como se Nemo estivesse nadando com segurança.

---

## 📊 Medindo a Cobertura do Código
Para garantir que cada linha do nosso oceano de código seja explorada, vamos usar o `pytest-cov` para medir a cobertura.

### 2. Executando Testes com Cobertura
No diretório `src`, rode o comando abaixo para gerar a cobertura de teste diretamente no terminal:

```bash
poetry run pytest --cov=etl --cov-report=term-missing
```

- **`--cov=etl`**: Diz ao `pytest` que queremos medir a cobertura do módulo `etl`.
- **`--cov-report=term-missing`**: Exibe no terminal as linhas do código que não foram cobertas pelos testes.

O relatório mostrará algo como:

```
Name                Stmts   Miss  Cover   Missing
-------------------------------------------------
etl/ingest_transform.py     50      5    90%   34-38
```

Nessa saída:
- **Stmts**: Número total de declarações no arquivo.
- **Miss**: Quantas declarações não foram cobertas.
- **Cover**: Percentual de cobertura.
- **Missing**: Linhas não cobertas pelos testes.

### 3. Gerando Relatório em HTML 🐠
Se quiser visualizar o relatório em um formato bonito e colorido, use o comando:

```bash
poetry run pytest --cov=etl --cov-report=html
```

Isso criará um diretório chamado `htmlcov`. Abra o arquivo `index.html` em seu navegador para explorar os recifes de cobertura de código.

```bash
start htmlcov/index.html  # Para Windows
topen htmlcov/index.html  # Para macOS
xdg-open htmlcov/index.html  # Para Linux
```

### 4. Gerando Relatório em XML 🐚
Se precisar de um relatório em formato XML (para ferramentas de integração contínua, por exemplo), use:

```bash
poetry run pytest --cov=etl --cov-report=xml
```

O arquivo `coverage.xml` será criado no diretório `src`.

---

## 🛠 Dicas Importantes para o Recife
1. Certifique-se de que os testes em `tests/test_etl.py` importam e testam as funções do módulo `etl`.
2. Sempre execute os comandos no diretório `src` para evitar problemas.
3. Use o relatório em HTML para identificar facilmente as partes do código que precisam de mais atenção.

---

## 🌊 Conclusão
Parabéns! Agora você sabe como navegar pelos testes e relatórios de cobertura no projeto Pérola Negra. Assim como Nemo explorou o oceano, você explorou cada linha de código para garantir que tudo esteja funcionando perfeitamente. Continue a nadar, a nadar, a nadar! 🐟

