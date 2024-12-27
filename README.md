# Inteli - Instituto de Tecnologia e Liderança

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="https://capitaldigital.com.br/wp-content/uploads/2021/04/logo-inteli-300x134-1.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width=40% height=40%></a>
</p>
<br>

# Desenvolvimento de Pipeline de Big Data para Análise e Decisão Operacional

## Projeto Pérola Negra

### Integrantes:
- [Ana Martire](https://www.linkedin.com/in/ana-carolina-cremonezi-martire-2a7335268/)
- [Eduardo Oliveira](https://www.linkedin.com/in/eduardo-hos/)
- [Keylla Oliveira](https://www.linkedin.com/in/keylla-oliveira1206/)
- [Lucas Barbosa](https://www.linkedin.com/in/lucasdasilvabarbosa/)
- [Nicollas Isaac](https://www.linkedin.com/in/nicollas-isaac/)
- [Sophia Nóbrega](https://www.linkedin.com/in/sophianobrega/)

### Professores:
- [Afonso Brandão](https://www.linkedin.com/in/afonsolelis/)
- [Ana Cristina](https://www.linkedin.com/in/anacristinadossantos/)
- [Cristina Gramani](https://www.linkedin.com/in/cristinagramani/)
- [Egon Daxbacher](https://www.linkedin.com/in/egondaxbacher/)
- [Francisco Escobar](https://www.linkedin.com/in/francisco-escobar/)
- [José Romualdo](https://www.linkedin.com/in/jose-romualdo/)
- [Pedro Teberga](https://www.linkedin.com/in/pedroteberga/)
- [Renato Penha](https://www.linkedin.com/in/renato-penha/)

## Descrição do Projeto
  
Este projeto visa o desenvolvimento de um pipeline de Big Data para a Companhia Paulista de Trens Metropolitanos (CPTM). O objetivo é construir uma infraestrutura que permita a análise de grandes volumes de dados operacionais e administrativos da empresa, ajudando a otimizar processos, reduzir custos, aumentar a produtividade e oferecer suporte na tomada de decisões estratégicas.

A solução envolve a ingestão, processamento e análise dos dados, culminando na criação de infográficos e painéis de visualização para facilitar a comunicação dos resultados.

### Tecnologias Utilizadas  
- **Armazenamento**: AWS S3 (Data Lake)  
- **Processamento de Dados**: ClickHouse (banco de dados analítico escalável), Prefect (orquestração de workflows)  
- **API e Backend**: Flask (API)  
- **Front-end**: Streamlit (aplicativo interativo para visualização de dados)  
- **ETL**: Implementado manualmente com Python, utilizando Prefect para orquestração  
- **Containerização**: Docker (deploy e execução de serviços)  
- **Testes**: Pytest (testes automatizados para garantir qualidade)  

## 🗃 Histórico de Lançamentos

* **0.5.0 - 17/12/2023**
    * **Sprint 5**: Apresentação Final; Documentação da Solução; DataAPP - Versão Final Refinada.
    
* **0.4.0 - 06/12/2023**
    * **Sprint 4**: Criação de Infográfico e Relatório de Análise de Eficácia com Sugestões de Melhorias; DataAPP - Primeira Versão; Entregável de Negócios - 2.
    
* **0.3.0 - 22/11/2023**
    * **Sprint 3**: Documentação de Análise de Impacto Ético; Cubo de Dados Automatizado.
    
* **0.2.0 - 08/11/2023**
    * **Sprint 2**: Prototipação em Baixa Fidelidade da Visualização de Dados; Estrutura de Ingestão de Dados.
    
* **0.1.0 - 25/10/2023**
    * **Sprint 1**: Criação de Persona, História do Usuário e Mapa de Jornada do Usuário; Entregável de Negócios - 1; Descoberta de Dados com Data Model Canvas.

## 📁 Estrutura de Pastas

A estrutura de pastas deste repositório é organizada da seguinte forma:

- **📂 assets**: Contém arquivos gráficos, como imagens e vídeos usados no projeto.
- **📂 documentation**: Documentação do projeto, incluindo apresentações, design, negócios e UX.
  - 📝 **Apresentacao.md**: Apresentação do projeto.  
  - 📝 **negocios.md**: Documentação relacionada aos aspectos de negócios.  
  - 📝 **programacao.md**: Informações sobre programação e implementação.  
  - 📝 **README.md**: Documentação principal do projeto.  
  - 📝 **ux.md**: Design focado na experiência do usuário.  
- **📂 src**: Código-fonte do projeto.  
  - 📂 **analise_exploratoria**: Scripts e notebooks para análise exploratória de dados.  
  - 📂 **assets**: Arquivos auxiliares necessários para o código-fonte.  
  - 📂 **config**: Configurações gerais do projeto.  
  - 📂 **etl**: Scripts relacionados ao pipeline ETL.  
    - 📂 **etl_bronze**: Scripts para ingestão e tratamento inicial dos dados.  
- **📂 streamlit**: Contém o aplicativo de visualização interativo.  
  - 📝 **app.py**: Arquivo principal do aplicativo Streamlit.  
  - 📂 **pages**: Páginas individuais do Streamlit.  
- **📂 tests**: Testes automatizados utilizando Pytest.  
- **📂 views**: Arquivos para renderização de dados ou integração com o front-end.  
- **📂 htmlcov**: Relatórios de cobertura de testes.  
- 📝 **.coverage**: Arquivo gerado pela cobertura dos testes.  
- 📝 **.env**: Arquivo de variáveis de ambiente (não versionado).  
- 📝 **.env.example**: Exemplo de arquivo de configuração de variáveis de ambiente.  
- 🛠️ **docker-compose.yml**: Configuração do Docker Compose.  
- 🛠️ **Dockerfile**: Configuração para a construção de imagens Docker.  
- 🛠️ **prefect.yaml**: Configurações do Prefect para orquestração de workflows.  
- 📝 **pyproject.toml**: Configuração do Poetry e dependências do projeto.  
- 🛠️ **poetry.lock**: Arquivo de bloqueio de versões de dependências.  
- 📝 **relatorio.html**: Relatório de execução ou análise gerado pelo projeto.  
- 📝 **rest.http**: Arquivo para testar endpoints da API.  
- 📝 **README.md**: Explicação geral do projeto e guia para uso.  

De uma forma mais visual, a estrutura de pastas é:

```plaintext
📂 Projeto
├── 📂 assets
├── 📂 documentation
│   ├── 📝 Apresentacao.md
│   ├── 📝 negocios.md
│   ├── 📝 programacao.md
│   ├── 📝 README.md
│   ├── 📝 ux.md
├── 📂 src
│   ├── 📂 __pycache__
│   ├── 📂 .pytest_cache
│   ├── 📂 analise_exploratoria
│   ├── 📂 assets
│   ├── 📂 config
│   ├── 📂 etl
│   │   ├── 📂 etl_bronze
│   │   │   ├── ingest.cpython-312.pyc
│   │   └── ...
├── 📂 streamlit
│   ├── 📂 __pycache__
│   ├── 📂 pages
│   ├── 📝 app.py
├── 📂 tests
├── 📂 views
├── 📂 htmlcov
├── 📝 .coverage
├── 📝 .env
├── 📝 .env.example
├── 📝 .prefectignore
├── 📝 app.py
├── 🛠️ docker-compose.yml
├── 🛠️ Dockerfile
├── 🛠️ prefect.yaml
├── 🛠️ poetry.lock
├── 📝 pyproject.toml
├── 📝 relatorio.html
├── 📝 rest.http
└── 📝 README.md
```

## 🔧 Instalação

### Docker

Este projeto utiliza Docker para executar o pipeline ETL e o Data App (front-end). Abaixo estão as instruções para instalação, configuração e execução dos containers.

O repositório contém os seguintes arquivos para o Docker:

- **Dockerfile.etl**: Arquivo para criar a imagem Docker do ETL.
- **Dockerfile.datapp**: Arquivo para criar a imagem Docker do Data App.

#### ETL

**1. Construir a imagem Docker**

Para criar a imagem Docker do ETL, execute o seguinte comando no terminal, na pasta `src` do projeto:

```bash
docker build -t etl -f Dockerfile.etl .
```

Este comando cria uma imagem chamada `etl` a partir do arquivo `Dockerfile.etl`.

**2. Executar o container**

Após criar a imagem, inicie um container usando o comando abaixo:

```bash
docker run --name etlcont -p 5000:5000 -d etl
```

- `--name etlcont`: Nomeia o container como `etlcont`.
- `-p 5000:5000`: Mapeia a porta 5000 do host para a porta 5000 do container.
- `-d`: Executa o container em segundo plano.

**3. Verificar o status do container**

Para verificar se o container está rodando corretamente, use:

```bash
docker ps
```

Este comando exibe informações sobre os containers ativos. Verifique se o container `etlcont` está listado como ativo.

---

#### Data App

**1. Construir a imagem Docker**

Para criar a imagem Docker do Data App, execute o seguinte comando no terminal, na pasta `src` do projeto:

```bash
docker build -t data_app -f Dockerfile.datapp .
```

Este comando cria uma imagem chamada `data_app` a partir do arquivo `Dockerfile.datapp`.

**2. Executar o container**

Após criar a imagem, inicie um container usando o comando abaixo:

```bash
docker run --name data_app_container -p 8501:8501 -d data_app
```

- `--name data_app_container`: Nomeia o container como `data_app_container`.
- `-p 8501:8501`: Mapeia a porta 8501 do host para a porta 8501 do container (utilizada pelo Streamlit).
- `-d`: Executa o container em segundo plano.

**3. Verificar o status do container**

Para verificar se o container está rodando corretamente, use:

```bash
docker ps
```

Certifique-se de que o container `data_app_container` está listado e ativo.

**4. Acessar o Data App**

Após iniciar o container, você pode acessar o Data App no navegador através do endereço:

```
http://localhost:8501
```

---

#### Comandos Úteis

**Parar um container**

Se você precisar parar um container, use:

```bash
docker stop <nome-do-container>
```

Exemplo para o ETL:

```bash
docker stop etlcont
```

**Remover um container**

Para remover um container (após parar), use:

```bash
docker rm <nome-do-container>
```

Exemplo para o ETL:

```bash
docker rm etlcont
```

#### Deploy

Clique [aqui](https://dataapp-production.up.railway.app/) para acessar o deploy da aplicação online.

<br>

## 🔧 Como executar testes com percentual de cobertura

Para realizar os testes unitários do projeto, siga os passos abaixo:

1. Abra o terminal ou o cmd na pasta do projeto.  
2. Navegue para a pasta `src` com o comando: `cd src`.  
3. Instale as dependências utilizando: `poetry install`.  
4. Execute os testes com o comando: `poetry run pytest`.  
5. Para verificar a cobertura de código, execute:  
   `poetry run pytest --cov=nome_do_pacote --cov-report=xml`, substituindo "nome_do_pacote" pelo pacote desejado.

## 💻 Configuração de Desenvolvimento

As configurações e possíveis modificações necessárias para adaptar o projeto para futuras demandas podem ser encontradas no arquivo **documents/configuration.md**.

## 🎥 Vídeo da Solução

<video width="640" height="480" controls>
  <source src="https://res.cloudinary.com/ddyjqty9s/video/upload/v1734445305/pjwp7oab5cpioyfd2b45.mp4" type="video/mp4">
</video>

[Assista ao vídeo aqui](https://drive.google.com/file/d/1ebkrDqNPwL3rys52mEBw4Vk0zKs1IuF3/view?usp=sharing)


## 🗃 Histórico de Lançamentos

- **0.5.0** - 15/12/2023: Avaliação final do projeto e encerramento.
- **0.4.0** - 01/12/2023: Infográfico e análise de eficácia.
- **0.3.0** - 17/11/2023: Data Lake/Data Warehouse operacional.
- **0.2.0** - 03/11/2023: Estrutura de ingestão de dados com protótipos visuais.
- **0.1.0** - 20/10/2023: Entendimento de negócios e arquitetura inicial.

## 📋 Licença

**Desenvolvimento de Pipeline de Big Data para Análise e Decisão Operacional by [Inteli](https://www.inteli.edu.br/), Projeto CPTM: [Ana Martire](https://www.linkedin.com/in/ana-carolina-cremonezi-martire-2a7335268/), [Eduardo Oliveira](https://www.linkedin.com/in/eduardo-hos/), [Keylla Oliveira](https://www.linkedin.com/in/keylla-oliveira1206/), [Lucas Barbosa](https://www.linkedin.com/in/lucasdasilvabarbosa/), [Nicollas Isaac](https://www.linkedin.com/in/nicollas-isaac/), [Sophia Nóbrega](https://www.linkedin.com/in/sophianobrega/) is licensed under** [Attribution 4.0 International (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/).

## 🎓 Referências

- **ALESP.** Lei nº 7.861, de 28 de maio de 1992. 28 maio 1996. Disponível em: <https://www.al.sp.gov.br/repositorio/legislacao/lei/1992/lei-7861-28.05.1992.html>. Acesso em: 19 out. 2024.

- **ARRUDA, Ricardo.** O que são User Stories (Estórias de Usuário)? - Agile Expert. 14 maio 2021. Disponível em: <https://www.agilexpert.com.br/2021/05/14/o-que-sao-user-stories-historias-de-usuario/>. Acesso em: 17 out. 2024.

- **BABICH, N.** Putting Personas to Work in UX Design: What They Are and Why They’re Important. Welcome to the Adobe Blog, 29 set. 2017. Disponível em: <https://blog.adobe.com/en/publish/2017/09/29/putting-personas-to-work-in-ux-design-what-they-are-and-why-theyre-important>. Acesso em: 17 out. 2024.

- **CAETANO, Rodrigo.** Big data: armazenamento de dados inúteis tem custo e afeta o meio ambiente | Exame. 6 maio 2020. Disponível em: <https://exame.com/tecnologia/armazenamento-de-dados-inuteis-gera-custos-e-prejudica-o-meio-ambiente/>. Acesso em: 12 nov. 2024.

- **CAROLI, Paulo.** 3 Differences Between Design Sprint and Lean Inception You Need To Know. Disponível em: <https://caroli.org/3-differences-between-design-sprint-and-lean-inception-you-need-to-know/>. Acesso em: 20 ago. 2024.

- **CAROLI, Paulo.** Learn Lean Inception at Caroli.org. Disponível em: <https://caroli.org/lean-inception-how-to-align-people-and-build-the-right-product/>. Acesso em: 20 ago. 2024.

- **CAROLI, Paulo.** Lean Inception: How to Align People and Build the Right Product. Disponível em: <https://caroli.org/lean-inception-3/>. Acesso em: 20 ago. 2024.

- **CAROLI, Paulo.** Why did the Lean Inception creator get involved with Data Mesh? Disponível em: <https://caroli.org/why-did-the-lean-inception-creator-get-involved-with-data-mesh/>. Acesso em: 20 ago. 2024.

- **CARVALHO, Leandro S.** Data Product Canvas. Disponível em: <https://medium.com/@leandroscarvalho/data-product-canvas-cd91f24776b1>. Acesso em: 10 set. 2024.

- **CATHO PARA EMPRESAS.** Quanto custa um funcionário para a empresa? Disponível em: <https://paraempresas.catho.com.br/quanto-custa-um-funcionario-para-empresa/#:~:text=Somados%2C%20os%20encargos%20equivalem%20a,da%20empresa%20vai%20precisar%20desembolsar>. Acesso em: 8 dez. 2024.

- **CPTM.** 2022a. Disponível em: <https://www.cptm.sp.gov.br/a-companhia/Documents/Abordagem%20Estratégica%20CPTM.pdf>. Acesso em: 12 nov. 2024.

- **CPTM.** 2023a. ESG#CONSCIENTE. Disponível em: <https://www.cptm.sp.gov.br/esg-consciente/Paginas/default.aspx>. Acesso em: 12 nov. 2024.

- **CPTM.** Política de Proteção de Dados | CPTM. (s.d.). Disponível em: <https://www.cptm.sp.gov.br/LGPD/Paginas/Politica-LGPD.aspx>. Acesso em: 12 nov. 2024.

- **EUROSTAT.** Railway passenger transport statistics - quarterly and annual data. Disponível em: <https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Railway_passenger_transport_statistics_-_quarterly_and_annual_data>. Acesso em: 3 dez. 2024.

- **GLOBO ESPORTE.** Caso Celsinho: "Se você fica neutro em situações de injustiça, você escolhe o lado do opressor". Disponível em: <https://ge.globo.com/blogs/esporte-legal/post/2021/08/31/caso-celsinho-se-voce-fica-neutro-em-situacoes-de-injustica-voce-escolhe-o-lado-do-opressor.ghtml>. Acesso em: 19 nov. 2024.

- **GUSHIKEN, A.** Value Proposition Canvas: o que é e como funciona essa metodologia? G4 Educação, 23 out. 2023. Disponível em: <https://g4educacao.com/portal/value-proposition-canvas>. Acesso em: 17 out. 2024.

- **HILLSON, D.; SIMON, P.** Practical project risk management: the ATOM methodology. Tysons Corner, Va.: Management Concepts, 2012.

- **LAMA, D.** Dalai Lama. (s.d.). Pensador. Disponível em: <https://www.pensador.com/frase/MTc1MDUwMA/>. Acesso em: 14 out. 2024.

- **LUCIDCHART.** Diagrama de componentes UML. Disponível em: <https://www.lucidchart.com/pages/pt/diagrama-de-componentes-uml>. Acesso em: 10 out. 2024.

- **MIRO.** O que é wireframe? Disponível em: <https://miro.com/pt/wireframe/o-que-e-wireframe/>. Acesso em: 10 out. 2024.

- **PURE STORAGE.** What is Data Ethics? Disponível em: <https://www.purestorage.com/br/knowledge/what-is-data-ethics.html>. Acesso em: 20 nov. 2024.

- **RAILWAY SUPPLY.** Significant growth in rail passenger transport across Europe in 2023. Disponível em: <https://www.railway.supply/en/significant-growth-in-rail-passenger-transport-across-europe-in-2023/>. Acesso em: 3 dez. 2024.

- **STREAMLIT.** Streamlit documentation. Disponível em: <https://docs.streamlit.io/>. Acesso em: 4 dez. 2024.

- **STICKDORN, M.; SCHNEIDER, J.** This is service design thinking basics, tools, cases. [s.l.]: Amsterdam Bis Publ, 2015.

- **TALENT.COM.** Salário médio de Analista de Dados em Brasil 2024. Disponível em: <https://br.talent.com/salary?job=analista+de+dados#:~:text=Sal%C3%A1rio%20M%C3%A9dio%20de%20Analista%20De%20Dados%20em%20Brasil%202024>. Acesso em: 3 dez. 2024.

- **VOCÊ S/A.** Vale-refeição dura 10 dias por mês no Brasil, mostra pesquisa. Disponível em: <https://vocesa.abril.com.br/economia/vale-refeicao-dura-10-dias-por-mes-no-brasil-mostra-pesquisa>. Acesso em: 8 dez. 2024.

- **What is User Centered Design (UCD)?** The Interaction Design Foundation, 5 jun. 2016. Disponível em: <https://www.interaction-design.org/literature/topics/user-centered-design>. Acesso em: 17 out. 2024.
