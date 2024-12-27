<div style="text-align: justify;">

# Documentação da parte de Negócios do Projeto Big Data - Módulo 8 - Inteli

## Grupo Pérola Negra - Solução DataApp com Dashbord

### Integrantes do Grupo:

- [Ana Martire](https://www.linkedin.com/in/ana-carolina-cremonezi-martire-2a7335268/)
- [Eduardo Oliveira](https://www.linkedin.com/in/eduardo-hos/)
- [Keylla Oliveira](https://www.linkedin.com/in/keylla-oliveira1206/)
- [Lucas Barbosa](https://www.linkedin.com/in/lucasdasilvabarbosa/)
- [Nicollas Isaac](https://www.linkedin.com/in/nicollas-isaac/)
- [Sophia Nóbrega](https://www.linkedin.com/in/sophianobrega/)

# Sumário

- [1. Introdução](#1-introdução)
  - [1.1. Parceiro de Negócios](#11-parceiro-de-negócios)
  - [1.2. Definição do Problema](#12-definição-do-problema)
    - [1.2.1. Problema](#121-problema)

- [2. Objetivos](#2-objetivos)
  - [2.1. Objetivos Gerais](#21-objetivos-gerais)
  - [2.2. Objetivos Específicos](#22-objetivos-específicos)
  - [2.3. Justificativa](#23-justificativa)

- [3. Lean Inception](#3-lean-inception)
  - [3.1. Matriz É/Não é, Faz/Não faz](#31-matriz-énão-é-faznão-faz)
  - [3.2. Product Goal (Objetivos do Produto)](#32-product-goal-objetivos-do-produto)
  - [3.3. Product Vision (Visão do Produto)](#33-product-vision-visão-do-produto)
  - [3.4. Canvas MVP](#34-canvas-mvp)

- [4. Compreensão do Problema](#4-compreensão-do-problema)
  - [4.1. Canvas Proposta de Valor](#41-canvas-proposta-de-valor)
    - [4.1.1. Perfil do Cliente](#411-perfil-do-cliente)
    - [4.1.2. Mapa de Valor](#412-mapa-de-valor)
  - [4.2. Matriz de Risco](#42-matriz-de-risco)
    - [Sprint I](#Sprint-I)
    - [Sprint II](#Sprint-II)
    - [Sprint III](#Sprint-III)
    - [Sprint IV](#Sprint-IV)
    - [Sprint V](#Sprint-V)
    - [Conclusão](#conclusão)
  - [4.3. Total Addressable Market (TAM)](#43-total-addressable-market-tam)
  - [4.4. Service Addressable Market (SAM)](#44-service-addressable-market-sam)
  - [4.5. Service Obtainable Market (SOM)](#45-service-obtainable-market-som)

- [5. Análise Financeira](#5-análise-financeira)
  - [5.1. Custos de Implementação e Manutenção](#51-custos-de-implementação-e-manutenção)
  - [5.2. Custos de Desenvolvimento](#52-Custos-de-Desenvolvimento)
  - [5.3. ROI (Return On Investment)](#53-ROI-Return-On-Investment)
  - [5.4. Conclusão](#54-Conclusão)

- [6. Plano de Comunicação](#6-plano-de-comunicação)
  - [6.1. Objetivo](#61-objetivo)
  - [6.2. Stakeholders](#62-stakeholders)
  - [6.3. Mensagens-Chave](#63-mensagens-chave)
  - [6.4. Canais de Comunicação](#64-canais-de-comunicação)
  - [6.5. Plano de Implementação](#65-plano-de-implementação)
  - [6.6. Medidas de Sucesso](#66-medidas-de-sucesso)
  - [6.7. Feedback e Ajustes](#67-feedback-e-ajustes)

- [7. Conclusões](#7-conclusões)

- [8. Referências](#8-referências)

<br>

# 1. Introdução

&emsp;&emsp;Este projeto está sendo desenvolvido por alunos do quarto semestre do curso de Sistemas de Informação do Inteli, no âmbito do módulo 8 da graduação em 2024. A faculdade Inteli adota uma metodologia de aprendizado baseada em projetos (PBL - Problem-Based Learning), na qual os alunos aplicam o conhecimento teórico em situações práticas e reais. Este projeto, em particular, marca o encerramento do segundo ano de estudos dos alunos e envolve 34 estudantes. Sob a orientação do pós-doutor Renato Penha, e com o suporte de um corpo docente altamente qualificado, composto por professores com doutorado ou, no mínimo, mestrado, os alunos estão desafiados a criar uma solução real para um problema complexo.

## 1.1. Parceiro de Negócios

&emsp;&emsp;A Companhia Paulista de Trens Metropolitanos (CPTM) é uma sociedade de economia mista, criada pela Lei nº 7.861, de 28 de maio de 1992, sob a autorização do Poder Executivo do Estado de São Paulo. Regida pelo Artigo 158 da Constituição do Estado, a CPTM é responsável pela exploração dos serviços de transporte de passageiros sobre trilhos ou guiados nas regiões metropolitanas, aglomerações urbanas e microrregiões do Estado de São Paulo [(Alesp, 1996)](https://www.al.sp.gov.br/repositorio/legislacao/lei/1992/lei-7861-28.05.1992.html). A empresa opera 57 estações, distribuídas em 5 linhas, que cobrem uma extensão de 196 quilômetros, transportando diariamente mais de 1,5 milhão de passageiros.

&emsp;&emsp;O papel da CPTM vai além do transporte de passageiros; ela tem uma importância estratégica para a mobilidade urbana e a qualidade de vida dos habitantes da maior metrópole do Brasil. Neste contexto, o projeto proposto para os alunos visa apoiar a empresa na análise de grandes volumes de dados operacionais, otimizando suas operações e contribuindo para a melhoria contínua dos seus serviços.

## 1.2. Definição do Problema

&emsp;&emsp;O grande volume de dados gerados pelas operações diárias da CPTM, provenientes de sistemas de controle e monitoramento, cria desafios consideráveis para a empresa, especialmente no que diz respeito à análise e interpretação dessas informações. A empresa enfrenta limitações tecnológicas e de infraestrutura que dificultam a extração de insights valiosos para a tomada de decisões estratégicas e operacionais.

### 1.2.1. Problema

&emsp;&emsp;O problema principal que o projeto aborda é a falta de recursos eficientes para analisar grandes volumes de dados gerados pelas operações da CPTM. A ausência de um pipeline de Big Data adequado para integrar, transformar e analisar esses dados impede a identificação de padrões relevantes e o uso de dados preditivos para otimizar as operações. Isso afeta diretamente a capacidade da empresa de melhorar a eficiência, reduzir custos e prever necessidades de manutenção e recursos operacionais.

<br>

# 2. Objetivos
&emsp;&emsp;Para a definição do projeto, é essencial estabelecer tanto os objetivos gerais quanto os específicos. A seguir, estão descritos os objetivos definidos para este projeto.

## 2.1. Objetivos Gerais

&emsp;&emsp;O objetivo geral deste projeto é desenvolver um pipeline de Big Data que permita à CPTM realizar análises estatísticas e descritivas em seus dados operacionais e administrativos. A solução proposta deverá ser capaz de lidar com grandes volumes de dados, proporcionando insights que melhorem a tomada de decisão da empresa, a gestão de recursos e a eficiência das suas operações. O projeto visa garantir que a CPTM possa explorar todo o potencial de seus dados, utilizando ferramentas modernas de processamento e análise em cloud, com foco em softwares de código aberto.

## 2.2. Objetivos Específicos

&emsp;&emsp;O projeto busca atingir objetivos específicos como: 

&emsp;&emsp;1. Construir uma infraestrutura de Data Lake na AWS S3 para armazenamento eficiente de dados.

&emsp;&emsp;2. Desenvolver um sistema de ingestão de dados em batch e streaming, integrando dados de diversas fontes.

&emsp;&emsp;3. Implementar um processo de ETL (extração, transformação e carga) utilizando AWS Glue ou AWS Lambda para preparar os dados para análise.

&emsp;&emsp;4. Utilizar o EMR (Elastic MapReduce) com Apache Spark e Hadoop para análises estatísticas e descritivas.

&emsp;&emsp;5. Criar infográficos, utilizando AWS QuickSight ou ferramentas open-source, para a visualização dos resultados.

&emsp;&emsp;6. Garantir que a solução seja escalável e adaptável às futuras necessidades da CPTM.

## 2.3. Justificativa

&emsp;&emsp;A realização deste projeto é essencial para que a CPTM consiga superar suas limitações atuais na análise de dados e aproveite melhor os recursos tecnológicos disponíveis no mercado. A implementação de um pipeline de Big Data irá permitir à empresa otimizar seus processos operacionais, melhorar o planejamento estratégico e obter uma visão preditiva mais precisa, que pode resultar em redução de custos e aumento da eficiência. A adoção de tecnologias de cloud computing e Big Data também colocará a CPTM em um patamar mais competitivo, alinhado às melhores práticas de gestão de grandes volumes de dados em empresas de transporte público em todo o mundo.

<br>

# 3. Lean Inception

&emsp;&emsp;A metodologia **Lean Inception** é uma abordagem colaborativa usada para alinhar equipes na criação de produtos, combinando conceitos de **Design Thinking** e **Lean Startup** para definir e planejar o escopo do Produto Mínimo Viável (MVP). De acordo com Paulo Caroli, autor da metodologia, "Lean Inception é essencial para alinhar expectativas e criar um plano de ação claro para entregar valor incremental ao longo do desenvolvimento" (Caroli, 2024). Em projetos de grande escala como o da CPTM (Companhia Paulista de Trens Metropolitanos), onde há um alto volume de dados operacionais e múltiplos stakeholders, a Lean Inception torna-se um processo necessario para garantir que todos os envolvidos estejam em congruência, especialmente em um ambiente complexo de análise de dados e otimização de operações.

&emsp;&emsp;No contexto da CPTM, a Lean Inception foi utilizada para alinhar áreas chave, como o **Centro de Controle Operacional (CCO)**, a **gerência de manutenção**, e a **diretoria de operações**. O foco foi desenvolver uma solução de Big Data que centralize e analise dados operacionais e administrativos, permitindo otimizar o planejamento de manutenção e melhorar a eficiência operacional com base em dados. Ao aplicar a Lean Inception, foi possível estabelecer objetivos claros e delimitar o escopo do produto, utilizando ferramentas como a matriz "É/Não é, Faz/Não faz", Objetivo do produto, Visão do Produto e Canvas MVP.

## 3.1. Matriz É/Não é, Faz/Não faz

&emsp;&emsp;Uma das ferramentas centrais na Lean Inception é a matriz **É/Não é, Faz/Não faz**, que permite delimitar claramente o que o produto será e o que não será, além de listar as funcionalidades que ele entregará ou não. No caso do projeto da CPTM, essa matriz ajudou a esclarecer e alinhar as expectativas de todos os stakeholders, principalmente em relação à capacidade de processamento de dados e às funcionalidades esperadas para melhorar as operações da companhia. Veja ela a seguir:


<div align="center">
<p><b>Figura 1</b> - Matriz É/Não é, Faz/Não faz</p>
<img src="https://res.cloudinary.com/dmornatkl/image/upload/v1729352513/e-naoe-faz-nfaz_grag89.png" width="80%"></a>

<sup><b>Fonte:</b> Material produzido pelo Grupo Pérola Negra (2024)</sup>
</div>

&emsp;&emsp;Com essa ferramenta, foi possível garantir que o pipeline de Big Data desenvolvido atenda às necessidades operacionais, sem prometer funcionalidades fora do escopo, mantendo o foco em entregas práticas e relevantes.

## 3.2. Product Goal (Objetivos do Produto)

&emsp;&emsp;O **Product Goal** define claramente o que o produto pretende alcançar. Ele serve como um guia central para o time de desenvolvimento e os stakeholders, garantindo que todos saibam quais resultados o produto deve entregar para ser considerado um sucesso. No projeto da CPTM, o objetivo principal é melhorar a eficiência operacional e o planejamento de manutenção por meio de uma solução centralizada de análise de dados.

&emsp;&emsp;O desenvolvimento desse pipeline de Big Data visa fornecer um sistema capaz de centralizar dados de diferentes áreas operacionais e administrativas, garantindo que as decisões estratégicas sejam fundamentadas em insights obtidos a partir de análises estatísticas descritivas. Esse alinhamento de dados permitirá à CPTM não apenas monitorar a eficiência das operações, mas também otimizar recursos, como o estoque de materiais consumíveis. Veja eles a seguir na figura:

<div align="center">
<p><b>Figura 2</b> - Product Goal</p>
<img src="https://res.cloudinary.com/dmornatkl/image/upload/v1729352512/product-goals_effiuk.png" width="80%"></a>

<sup><b>Fonte:</b> Material produzido pelo Grupo Pérola Negra (2024)</sup>
</div>

- **Centralização de Dados:** Criar uma ferramenta única que centralize dados operacionais e administrativos em um ambiente seguro e acessível.
- **Armazenamento e Processamento:** Proporcionar uma infraestrutura para armazenamento em grande escala de dados, com processamento eficiente por meio de tecnologias como AWS EMR e Apache Spark.
- **Análise de Dados:** Executar análises estatísticas descritivas que ajudem a melhorar as operações e fornecer insights para o planejamento de manutenção.
- **Visualizações e Relatórios:** Facilitar a tomada de decisões por meio de visualizações claras e relatórios detalhados criados com ferramentas como AWS QuickSight ou alternativas open-source.

## 3.3. Product Vision (Visão do Produto)

&emsp;&emsp;A **Product Vision** descreve a visão de futuro para o produto e como ele beneficiará os usuários finais. Ela fornece uma orientação clara e inspiradora para a equipe, assegurando que o produto entregue o máximo de valor possível. No caso da CPTM, o foco está em criar um pipeline de Big Data que possibilite o processamento e a análise centralizada de dados operacionais e administrativos, ajudando a empresa a tomar decisões mais embasadas.

&emsp;&emsp;A visão do produto para o projeto da CPTM é fornecer uma plataforma que centralize dados de diferentes áreas, processando-os de forma eficiente para gerar insights estratégicos que otimizem as operações diárias da empresa. A principal diferença do produto em comparação a outras soluções no mercado é seu foco em análises descritivas, ao invés de IA ou Machine Learning, o que torna o produto mais acessível, direto e fácil de implementar nas operações diárias da CPTM. Veja na figura 3 a seguir a tela usada para montar a visão do produto.

<div align="center">
<p><b>Figura 3</b> - Product Vision</p>
<img src="https://res.cloudinary.com/dmornatkl/image/upload/v1729352513/product-vision_oms3td.png" width="80%"></a>

<sup><b>Fonte:</b> Material produzido pelo Grupo Pérola Negra (2024)</sup>
</div>

&emsp;&emsp;Ao focar em uma solução que centralize dados operacionais e administrativos e ofereça insights, a visão do produto reforça o compromisso de fornecer uma plataforma que seja acessível, eficiente e capaz de transformar o processo de tomada de decisões dentro da companhia.

## 3.4. Canvas MVP

&emsp;&emsp;O **Canvas MVP** é uma ferramenta que estrutura as principais componentes do MVP, como proposta de valor, segmentos de clientes, jornada do usuário e métricas, facilitando o planejamento e o acompanhamento do desenvolvimento. No projeto da CPTM, o Canvas MVP foi desenvolvido para garantir que o produto entregue soluções práticas e mensuráveis para os desafios operacionais identificados, como a centralização e análise de grandes volumes de dados. Veja ele a seguir:

<div align="center">
<p><b>Figura 4</b> - Canvas MVP</p>
<img src="https://res.cloudinary.com/dmornatkl/image/upload/v1729352513/canvas-mvp_n8qa95.png" width="80%"></a>

<sup><b>Fonte:</b> Material produzido pelo Grupo Pérola Negra (2024)</sup>
</div>

&emsp;&emsp;O Canvas MVP estruturou o desenvolvimento do MVP de maneira que garantisse as funcionalidades prioritárias, os segmentos de clientes e as métricas alinhadas com os objetivos estratégicos da CPTM. Com o MVP bem definido, a equipe consegue direcionar esforços para entregar uma solução viável que gera valor imediato, facilitando o monitoramento das operações.

<br>

# 4. Compreensão do Problema

&emsp;&emsp;Esta seção se concentra na avaliação detalhada do ambiente e escopo geral do projeto, visando compreender as necessidades, aspirações e desafios enfrentados pelo parceiro, a CPTM. Além disso, busca-se examinar o desempenho atual do negócio, considerando a perspectiva do projeto em questão. Para isso, são coletados dados relevantes para o negócio, com o objetivo de identificar oportunidades de aprimoramento dentro do escopo do projeto e elaborar planos de ação estratégicos com uma visão de longo prazo para a implementação.

&emsp;&emsp;Dentro dessa análise, são considerados fatores como matriz de risco para identificar, avaliar e mitigar potenciais riscos que podem afetar negativamente o projeto e canvas de proposta de valor para compreender como o projeto se alinha aos objetivos e necessidades da CPTM. Essas ferramentas proporcionam uma compreensão abrangente do contexto empresarial, permitindo uma tomada de decisão informada e estratégica para o sucesso do projeto.

## 4.1. Canvas Proposta de Valor
&emsp;&emsp;De acordo com o grupo G4 educação: “O Value Proposition Canvas ou Proposta de Valor Canvas é uma ferramenta que permite aos empreendedores e empresários desenhar, testar e visualizar o valor do produto para os clientes, de uma forma intuitiva." Ao lado direito da imagem há o perfil do cliente, que apresenta os ganhos que ele terá com o produto, as dores atuais, e as tarefas dele no produto. Ao lado esquerdo há o mapa de valor, onde é apresentado o produto, seus criadores de ganho, e o alívio das dores do cliente. [(Gushiken, 2024)](https://g4educacao.com/portal/value-proposition-canvas)


<div align="center">
<p><b>Figura 5</b> - Value Proposition Canvas</p>
<img src="https://res.cloudinary.com/dzpxdd08y/image/upload/v1729542523/Value_Proposition_Canvas_rl8nha.png" width="100%" >
<sup>Fonte: Material produzido pelo Grupo Pérola Negra (2024)</sup>
</div>
<br>


### 4.1.1. Perfil do Cliente

&emsp;&emsp;Na análise do perfil do cliente, as principais tarefas esperadas do projeto são a <b>otimização da gestão dos dados</b>, a <b>melhoria da eficiência operacional</b> e a <b>prevenção de problemas</b>. A CPTM busca centralizar e organizar seus dados para facilitar o acesso e a tomada de decisões, além de automatizar processos repetitivos para melhorar a produtividade. Outro objetivo é implementar uma solução de monitoramento contínuo, capaz de antecipar falhas e evitar interrupções nos serviços.

&emsp;&emsp;O cliente tem algumas dores que quer que sejam sanadas com o projeto. Elas são a <b>lentidão nas tomadas de decisão</b>, a <b>baixa eficiência operacional</b> e a <b>pouca otimização de processos</b>. A falta de estrutura para processar e analisar grandes volumes de dados compromete a eficiência e gera atrasos na resposta a falhas. Além disso, a ausência de dados organizados dificulta decisões rápidas e informadas, enquanto a falta de uma visão consolidada prejudica a otimização coordenada das operações e a alocação eficiente de recursos.

&emsp;&emsp;Os "ganhos" demontrados na figura do Value Proposition Canvas são o que a CPTM espera que aconteça com a solução que o grupo <i>Pérola Negra</i> desenvolveu. Eles estão diretamente ligados às "dores" descritas acima. Então, os ganhos que o cliente espera ter com o projeto são a <b>agilidade na tomada de decisões</b>, a <b>prevenção de falhas</b> e a <b>otimização de processos</b>. A CPTM espera que o projeto traga agilidade nas decisões, com dados acessíveis em tempo real, prevenção de falhas, através de monitoramento contínuo, e otimização de processos, eliminando gargalos e melhorando o uso de recursos. Esses ganhos "colidem" diretamente com as dores, ou seja, esses ganhos abordam de forma direta as principais dificuldades enfrentadas pela CPTM.

### 4.1.2. Mapa de Valor

&emsp;&emsp;Partindo agora para o mapa de valor, a parte esquerda da imagem, é possível notar que o produto que o grupo entregará à CPTM é o <b>desenvolvimento de um pipeline de Big Data para análise e processamento eficiente de grandes volumes de dados</b>. O pipeline visa centralizar e estruturar os dados da CPTM, proporcionando um processamento ágil e organizado. Essa solução oferece uma base sólida para automação de análises e geração de insights em tempo real, com uma estrutura escalável e adaptada para integrar diferentes fontes de dados. Além disso, facilita a criação de dashboards automatizados, fornecendo uma visão clara dos indicadores chave, apoiando a tomada de decisões e o monitoramento contínuo. Assim, o projeto não só entrega uma solução tecnológica, mas também uma ferramenta estratégica para otimizar a gestão dos dados e a eficiência operacional.

&emsp;&emsp;A seção de alívio das dores destaca os aspectos da solução que são projetados para resolver diretamente os desafios enfrentados pelo cliente. No caso da CPTM, a solução oferece <b>dashboards automatizados</b>, que permitem acesso rápido a informações críticas, proporcionando agilidade na tomada de decisões, e o p<b>rocessamento eficiente dos dados</b>, que melhora a eficiência operacional, eliminando gargalos e reduzindo o tempo de resposta. Esses "pain killers", como são chamados em inglês, resolvem todas as dores que o cliente possui, as quais já foram citadas anteriormente.

&emsp;&emsp;Por fim, os criadores de ganho mostram o que a CPTM vai ganhar com os alívios das dores. Com a implementação do pipeline de Big Data, a empresa terá <b>maior eficiência operacional</b>, <b>reduzindo custos</b> e otimizando recursos através da automação de processos. Além disso, o acesso a <b>insights em tempo real</b> permitirá uma resposta mais rápida a incidentes e desafios operacionais, <b>antecipando possíveis falhas</b> e melhorando a tomada de decisões estratégicas.

<br>

&emsp;&emsp;O desenvolvimento de um Value Proposition Canvas é essencial para entender as necessidades do cliente e alinhar a solução com suas expectativas. Ele permite identificar de forma clara as principais dores e tarefas do cliente, os ganhos esperados, e como a solução proposta pode aliviá-las de maneira eficaz. Essa ferramenta estratégica ajuda a garantir que o produto ou serviço oferecido esteja diretamente conectado aos desafios reais enfrentados pelo cliente, fornecendo uma abordagem estruturada para criar valor. Além disso, facilita a comunicação da proposta entre a equipe e as partes interessadas, promovendo um entendimento comum e orientando o desenvolvimento de soluções que entreguem resultados concretos.

<br>

## 4.2. Matriz de Risco
&emsp;&emsp;A matriz de risco é uma ferramenta utilizada para a identificação, análise e priorização de riscos em projetos. Ela permite visualizar de forma clara e objetiva o impacto e a probabilidade de diferentes riscos, ajudando as equipes a focar naqueles que podem causar maiores prejuízos ou interrupções. Por meio de uma avaliação quantitativa ou qualitativa, a matriz de risco facilita a tomada de decisões, permitindo que medidas preventivas ou corretivas sejam implementadas de maneira rápida e eficaz.

&emsp;&emsp;Segundo Hillson, a matriz de risco é fundamental para a gestão proativa de riscos, uma vez que possibilita a priorização baseada em critérios claros e mensuráveis, como a probabilidade de ocorrência e a gravidade do impacto. Esta ferramenta ajuda a minimizar incertezas e a maximizar as chances de sucesso em projetos complexos, garantindo que os recursos sejam direcionados de forma eficiente para mitigar riscos críticos. [(Hillson; Simon, 2024)](https://books.google.com.br/books?id=4XznDwAAQBAJ&printsec=copyright&redir_esc=y#v=onepage&q&f=false)

&emsp;&emsp;No projeto da Companhia Paulista de Trens Metropolitanos (CPTM), a matriz de risco é se faz necessaria para gerenciar os desafios de uma iniciativa conduzida por 34 alunos do curso de Sistemas de Informação da Inteli. Com foco na criação de uma plataforma de dados para otimizar a gestão operacional e de manutenção, a ferramenta ajuda a identificar e priorizar riscos, como atrasos e falhas de comunicação com os stakeholders, além de aproveitar oportunidades, como feedbacks da CPTM e a colaboração técnica entre grupos. Essa abordagem garante que o projeto siga dentro do prazo e atenda às expectativas de todos stakeholders envolvidos. 

### Sprint I 

<div align="center">
<p><b>Quadro 1</b> - Matriz de Risco 1</p>
<img src="https://res.cloudinary.com/dmornatkl/image/upload/v1729642495/Matriz_de_Risco_-_G5_-_m8_djfdj0.png" width="100%"></a>

<sup><b>Fonte:</b> Material produzido pelo Grupo Pérola Negra (2024)</sup>
</div>

&emsp;&emsp;Com a ciência da matriz de risco, agora é apresentado os responsáveis pelo gerenciamento dos riscos. A seguir, são detalhadas as oportunidades e ameaças identificadas, cada uma com sua respectiva probabilidade, impacto, responsável e plano de ação. Veja tudo a seguir:

&emsp;&emsp;Responsáveis no Projeto CPTM:

- **Time de Desenvolvimento:** Grupo Pérola Negra
- **Product Owner (PO):** Pessoas rotativas do grupo Pérola Negra
- **Scrum Master:** Pessoas rotativas do Grupo Pérola Negra
- **Orientador:** Renato Penha - Orientador da Turma 10 de Sistemas de Informação
- **Coordenador do Curso:** Egon - Coordenador do curso de Sistemas de Informação
- **Líder do Projeto:** Roberto Morina
- **Ponto Focal Backup:** Sarah de Sá Fernandes
- **Líder Técnico:** Roberto Morina
- **Líder de Negócio:** Sarah de Sá Fernandes
- **Líder Executivo:** Maicon Satiro de Oliveira

#### Oportunidades

1. **Colaboração intergrupal para conhecimento de bases**
   - Impacto: Alto  
   - Probabilidade: 70%  
   - Descrição: Possibilidade de formar parcerias com outros grupos para compartilhar conhecimento técnico sobre as bases de dados.  
   - Responsável: Time de Desenvolvimento 
   - Plano de Ação: Organizar Daylies colaborativas e encontros regulares para troca de conhecimento entre os grupos.

2. **Feedback valioso da CPTM**  
   - Impacto: Muito Alto  
   - Probabilidade: 50%  
   - Descrição: A chance de receber insights detalhados da CPTM para melhorar o projeto.  
   - Responsável: Líder de Negócio e de Projeto
   - Plano de Ação: Manter reuniões periódicas com stakeholders da CPTM para coletar feedback contínuo.

3. **Otimização de processos**  
   - Impacto: Muito Alto  
   - Probabilidade: 70%  
   - Descrição: Identificação de falhas no tratamento de dados pode gerar melhorias no processo.  
   - Responsável: Líder Técnico  
   - Plano de Ação: Implementar revisões semanais no processo de tratamento de dados para detectar e corrigir ineficiências.

4. **Fortalecimento da liderança**  
   - Impacto: Alto  
   - Probabilidade: 50%  
   - Descrição: Membros podem assumir papéis de liderança para organizar melhor o trabalho e fechar o escopo.  
   - Responsável: Scrum Master  
   - Plano de Ação: Alternar responsabilidades de liderança entre os membros do grupo para desenvolver habilidades de gestão.

5. **Capacitação técnica interna**  
   - Impacto: Moderado  
   - Probabilidade: 50%  
   - Descrição: Oportunidade para o grupo expandir seu conhecimento técnico.  
   - Responsável: Time de Desenvolvimento  
   - Plano de Ação: Agendar treinamentos técnicos em AWS, Apache Spark e Hadoop com foco nas ferramentas utilizadas no projeto.

6. **Aprendizado em gestão de risco**  
   - Impacto: Muito Alto  
   - Probabilidade: 90%  
   - Descrição: A gestão dos riscos neste projeto pode melhorar a capacidade do grupo de lidar com incertezas em futuros projetos.  
   - Responsável: Scrum Master 
   - Plano de Ação: Atualizar constantemente a matriz de risco e implementar boas práticas de gerenciamento de riscos.

#### Ameaças

1. **Não compreensão dos dados fornecidos**  
   - Impacto: Muito Alto  
   - Probabilidade: 70%  
   - Descrição: Dificuldade de interpretar corretamente os dados recebidos da CPTM pode atrasar o andamento do projeto.  
   - Responsável: Time de Desenvolvimento  
   - Plano de Ação: Realizar sessões de alinhamento com a equipe técnica da CPTM para garantir clareza nos dados.

2. **Falta de participação nas dailies**  
   - Impacto: Alto  
   - Probabilidade: 30%  
   - Descrição: Membros do grupo podem não participar ativamente das reuniões diárias, prejudicando o progresso.  
   - Responsável: Scrum Master  
   - Plano de Ação: Reforçar a importância das dailies e aplicar técnicas de gamificação para aumentar o engajamento.

3. **Atraso na entrega das atividades**  
   - Impacto: Muito Alto  
   - Probabilidade: 30%  
   - Descrição: Problemas de organização interna podem resultar em atrasos.  
   - Responsável: Product Owner  
   - Plano de Ação: Implementar o uso de ferramentas de gestão como o Jira para acompanhamento rigoroso das atividades, e se cabível negociar data de entrega com Orientador.

4. **Falta de experiência técnica**  
   - Impacto: Alto  
   - Probabilidade: 70%  
   - Descrição: O grupo pode enfrentar dificuldades técnicas para lidar com as ferramentas e dados.  
   - Responsável: Time de Desenvolvimento  
   - Plano de Ação: Identificar gaps de conhecimento e promover treinamentos adicionais com professores.

5. **Retrabalho devido a decisões erradas**  
   - Impacto: Moderado  
   - Probabilidade: 30%  
   - Descrição: Decisões incorretas no tratamento de dados podem resultar em retrabalho significativo.  
   - Responsável: Time de Desenvolvimento  
   - Plano de Ação: Revisar constantemente as decisões e ajustar os processos conforme o feedback das revisões.

6. **Falta de alinhamento interno**  
   - Impacto: Muito Alto  
   - Probabilidade: 50%  
   - Descrição: Desalinhamento entre membros pode afetar o desempenho geral.  
   - Responsável: Time de Desenvolvimento  
   - Plano de Ação: Realizar reuniões de alinhamento e refinamento interno semanalmente para discutir as responsabilidades de cada membro.

7. **Prazo insuficiente**  
   - Impacto: Moderado  
   - Probabilidade: 70%  
   - Descrição: O tempo necessário para concluir as soluções pode ser maior que o disponível.  
   - Responsável: Orientador  
   - Plano de Ação: Reavaliar constantemente o cronograma e ajustar as metas para garantir que as entregas essenciais sejam priorizadas de acordo com o plano de trabalho.

8. **Falta de suporte da CPTM**  
   - Impacto: Muito Alto  
   - Probabilidade: 10%  
   - Descrição: Caso a CPTM não forneça o suporte necessário, o projeto pode ser comprometido.  
   - Responsável: Líder do Projeto com Coordenador do Curso
   - Plano de Ação: Estabelecer um canal de comunicação direto com a equipe da CPTM para garantir suporte contínuo.

9. **Perda de foco no MVP**  
   - Impacto: Alto  
   - Probabilidade: 50%  
   - Descrição: Falta de clareza sobre o objetivo principal pode levar a um MVP mal definido.  
   - Responsável: Coordenador de Escopo  
   - Plano de Ação: Realizar workshops para garantir que todos entendam claramente o foco do MVP e suas prioridades.

10. **Sobrecarga de trabalho**  
      - Impacto: Moderado  
      - Probabilidade: 50%  
      - Descrição: A equipe pode se sobrecarregar com as atividades.  
      - Responsável: Scrum Master  
      - Plano de Ação: Monitorar a carga de trabalho de cada membro e redistribuir tarefas quando necessário.

11. **Comunicação ineficaz com stakeholders**  
      - Impacto: Alto  
      - Probabilidade: 10%  
      - Descrição: Falhas de comunicação com stakeholders podem causar desalinhamento.  
      - Responsável: Product Owner  
      - Plano de Ação: Estabelecer um plano de comunicação claro com a CPTM e aproveitar datas de entrega para realizar reuniões de alinhamento.

### Sprint II

<div align="center">
<p><b>Quadro 2</b> - Matriz de Risco 2</p>
<img src="https://res.cloudinary.com/dyioydhrw/image/upload/v1731026644/Matriz_de_Risco_-_G5_-_m8_yytm3h.png" width="100%"></a>

<sup><b>Fonte:</b> Material produzido pelo Grupo Pérola Negra (2024)</sup>
</div>

#### Ameaças

1. **Conflitos entre a equipe**
   - Impacto: Moderado
   - Probabilidade: 30%
   - Descrição: Desentendimentos entre membros da equipe podem afetar a produtividade e a união do time.
   - Responsável: Scrum Master
   - Plano de Ação: Promover sessões de feedback e conversas conjuntas para resolver conflitos de maneira rápida.

2. **Problemas de conectividade com Object Storage**
   - Impacto: Alto
   - Probabilidade: 50%
   - Descrição: Falhas na conexão podem atrasar a extração de dados e interromper o ETL.
   - Responsável: Time de Desenvolvimento
   - Plano de Ação: Implementar soluções de backup de conexão e monitoramento contínuo.

3. **Erros na transformação de dados**
   - Impacto: Muito Alto
   - Probabilidade: 50%
   - Descrição: Erros ao limpar e transformar dados podem resultar em informações inconsistentes para o carregamento no Data Warehouse.
   - Responsável: Time de Desenvolvimento
   - Plano de Ação: Implementar validação durante a etapa de transformação para garantir a integridade dos dados.

4. **Prazo insuficiente para desenvolvimento**
   - Impacto: Moderado
   - Probabilidade: 70%
   - Descrição: Falta de tempo adequado para concluir todas as tarefas pode levar a um trabalho apressado e de menor qualidade.
   - Responsável: PO
   - Plano de Ação: Priorizar tarefas críticas e ajustar o escopo durante a daily, se necessário.

5. **Falta de experiência técnica**
   - Impacto: Alto
   - Probabilidade: 70%
   - Descrição: A equipe pode não ter experiência e conhecimento suficiente em algumas tecnologias, o que pode atrasar o trabalho e comprometer a qualidade do resultado.
   - Responsável: Time de Desenvolvimento
   - Plano de Ação: Identificar áreas de deficiência técnica e providenciar o suporte e estudo necessários.

#### Oportunidades

1. **Possibilidade de otimização de processos**
   - Impacto: Alto
   - Probabilidade: 50%
   - Descrição: Melhorias na etapa de transformação podem resultar em um processo mais escalável.
   - Responsável: Time de Desenvolvimento 
   - Plano de Ação: Avaliar regularmente o desempenho do processo e implementar melhorias caso necessário.

2. **Capacitação técnica interna**
   - Impacto: Moderado
   - Probabilidade: 30%
   - Descrição: O projeto oferece a oportunidade para que a equipe desenvolva novas habilidades técnicas, especialmente em ETL.
   - Responsável: Scrum Master e Equipe
   - Plano de Ação: Realizar os autoestudos e estar presente nas aulas, buscando atendimento individual com o professor, se necessário.

3. **Capacitação em modelagem UML e Arquitetura**
   - Impacto: Alto
   - Probabilidade: 70%
   - Descrição: O projeto oferece à equipe a chance de aprimorar suas habilidades em modelagem UML e Arquitetura, o que pode ser muito útil em projetos que exijam a documentação de arquiteturas de sistemas.
   - Responsável: Time de Desenvolvimento
   - Plano de Ação: Realizar os autoestudos específicos em UML e práticas de modelagem para garantir a precisão e qualidade do diagrama.

### Sprint III 

<div align="center">
<p><b>Quadro 3</b> - Matriz de Risco 3</p>
<img src="https://res.cloudinary.com/ddyjqty9s/image/upload/v1734380943/MatrizRiscoS3.png" width="100%"></a>

<sup><b>Fonte:</b> Material produzido pelo Grupo Pérola Negra (2024)</sup>
</div>

#### Ameaças

1. **Prazo insuficiente para o desenvolvimento**  
   - Impacto: Muito Alto  
   - Probabilidade: 90%  
   - Descrição: O curto prazo pode prejudicar a entrega ou qualidade das entregas.  
   - Responsável: Product Owner  
   - Plano de Ação: Priorizar o planejamento e a realização de tarefas sem atrasos..

2. **Falta de experiência técnica**  
   - Impacto: Alto  
   - Probabilidade: 90%  
   - Descrição: A falta de conhecimento técnico pode prejudicar as entregas.  
   - Responsável: Time de Desenvolvimento  
   - Plano de Ação: Realizar estudos além dos propostos em sala para entender as tecnologias e fluxos que serão utilizados.

3. **Problemas de conectividade com Object Storage**  
   - Impacto: Muito Alto  
   - Probabilidade: 50%  
   - Descrição: Dificuldades técnicas de conectividade podem atrasar as entregas.  
   - Responsável: Time de Desenvolvimento  
   - Plano de Ação: Fazer testes constantes com a conectividade, e sempre alinhar com os professores.

4. **Conflitos entre a equipe**  
   - Impacto: Moderado  
   - Probabilidade: 30%  
   - Descrição: Falta de alinhamento pode gerar conflitos e afetar as entregas.  
   - Responsável: Scrum Master  
   - Plano de Ação: Durante os encontros ajudar a mediar as discussões.


5. **Falta da presença do grupo completo em momentos importantes**  
   - **Impacto:** Moderado  
   - **Probabilidade:** 50%  
   - **Descrição:** A ausência de membros durante os encontros prejudica o grupo no alinhamento e no planejamento das tarefas.  
   - **Responsável:** Scrum Master  
   - **Plano de Ação:** Garantir o comprometimento do grupo com os encontros diários e marcar a presença dos membros.

6. **Problemas com tecnologias novas (Prefect)**  
   - **Impacto:** Muito Alto  
   - **Probabilidade:** 70%  
   - **Descrição:** A introdução de uma tecnologia nova no projeto, pode dificultar e muito o desenvolvimento da entrega em especial quando se trata de uma tecnologia como Prefect, que não se encontra um número elevado de documentos/materiais para ajuda e estudo.  
   - **Responsável:** Time de Desenvolvimento  
   - **Plano de Ação:** Buscar conhecer sobre a tecnologia e entender quais serão os usos dentro do projeto.

7. **Erros na transformação de dados**  
   - **Impacto:** Muito Alto  
   - **Probabilidade:** 50%  
   - **Descrição:** Falhas no processo de transformação dos dados podem gerar um trabalho não planejado, e um atraso nas entregas.  
   - **Responsável:** Time de Desenvolvimento  
   - **Plano de Ação:** Planejar todas as entregas com antecedência, e sempre alinhar as dificuldades com o grupo.

#### Oportunidades

1. **Aprendizagem com relação à visualização dos dados**  
   - Impacto: Moderado  
   - Probabilidade: 90%  
   - Descrição: Oportunidade de entender melhor sobre as técnicas de visualização para análise e apresentação dos dados, utilizando tecnologias novas como streamlit.  
   - Responsável: Time de Desenvolvimento  
   - Plano de Ação: Estudar ferramentas de visualização.

2. **Melhoria na convivência e trabalho em equipe do grupo**  
   - Impacto: Alto  
   - Probabilidade: 50%  
   - Descrição: Possibilidade de alinhar a equipe e fortalecer a colaboração entendendo melhor os erros e acertos das sprints anteriores.  
   - Responsável: Scrum Master  
   - Plano de Ação: Fazer sessões de feedback e dinâmicas de grupo para melhorar a comunicação.

3. **Capacitação técnica interna**  
   - Impacto: Moderado  
   - Probabilidade: 50%  
   - Descrição: Aumento do conhecimento técnico do grupo.  
   - Responsável: Time de Desenvolvimento  
   - Plano de Ação: Estudar além das aulas e autoestudos as tecnologias que serão necessárias.

### Sprint IV

<div align="center">
<p><b>Quadro 4</b> - Matriz de Risco 4</p>
<img src="https://res.cloudinary.com/ddyjqty9s/image/upload/v1734399067/MatrizRiscoSprint4.png" width="100%"></a>

<sup><b>Fonte:</b> Material produzido pelo Grupo Pérola Negra (2024)</sup>
</div>

#### Ameaças

1. **Prazo insuficiente para o desenvolvimento**  
   - Impacto: Muito Alto  
   - Probabilidade: 90%  
   - Descrição: O curto prazo pode prejudicar a entrega ou qualidade das entregas.  
   - Responsável: Product Owner  
   - Plano de Ação: Priorizar o planejamento e a realização de tarefas sem atrasos.

2. **Falta de experiência técnica**  
   - Impacto: Alto  
   - Probabilidade: 90%  
   - Descrição: A falta de conhecimento técnico pode prejudicar as entregas.  
   - Responsável: Time de Desenvolvimento  
   - Plano de Ação: Realizar estudos além dos propostos em sala para entender as tecnologias e fluxos que serão utilizados.

3. **Problemas devido à refatoração e retrabalho**  
   - Impacto: Muito Alto  
   - Probabilidade: 50%  
   - Descrição: Falta de comprometimento no planejamento pode ocasionar em situações de diversos membros fazendo itens semelhantes e deixando de se dedicar a outros itens importantes.  
   - Responsável: Product Owner  
   - Plano de Ação: Realizar os encontros com a equipe comprometida, e alinhar sempre todas as tarefas sendo realizadas.

4. **Falta de comprometimento em relação às entregas e atividades**  
   - Impacto: Alto  
   - Probabilidade: 30%  
   - Descrição: Baixo comprometimento de membros pode prejudicar as entregas.  
   - Responsável: Scrum Master  
   - Plano de Ação: Acompanhar de perto o progresso e e sempre alinhar as tarefas nos encontros do grupo.

5. **Conflitos entre a equipe**  
   - Impacto: Moderado  
   - Probabilidade: 30%  
   - Descrição: Falta de alinhamento pode gerar conflitos e afetar as entregas.  
   - Responsável: Scrum Master  
   - Plano de Ação: Durante os encontros ajudar a mediar as discussões.

6. **Falta da presença do grupo completo em momentos importantes**  
   - **Impacto:** Moderado  
   - **Probabilidade:** 50%  
   - **Descrição:** A ausência de membros durante os encontros prejudica o grupo no alinhamento e no planejamento das tarefas.  
   - **Responsável:** Scrum Master  
   - **Plano de Ação:** Garantir o comprometimento do grupo com os encontros diários e marcar a presença dos membros.


#### Oportunidades

1. **Aprendizagem com relação a novas tecnologias (Streamlit)**  
   - Impacto: Muito Alto  
   - Probabilidade: 70%  
   - Descrição: Oportunidade de adotar e aprender novas tecnologias úteis para o projeto.  
   - Responsável: Time de Desenvolvimento  
   - Plano de Ação: Buscar entender e aprender durante a realização de tarefas de novas tecnologias.

2. **Aprendizagem com relação à visualização dos dados**  
   - Impacto: Moderado  
   - Probabilidade: 90%  
   - Descrição: Oportunidade de entender melhor sobre as técnicas de visualização para análise e apresentação dos dados, utilizando tecnologias novas como streamlit.  
   - Responsável: Time de Desenvolvimento  
   - Plano de Ação: Estudar ferramentas de visualização.

3. **Possibilidade de otimização de processos**  
   - Impacto: Alto  
   - Probabilidade: 50%  
   - Descrição: Melhorias no fluxo de trabalho identificando falhas e diminuindo retrabalhos.  
   - Responsável: Líder Técnico  
   - Plano de Ação: Entender as ultimas sprints e as tecnologias, para que os fluxos possam ser otimizados.

4. **Melhoria na convivência e trabalho em equipe do grupo**  
   - Impacto: Alto  
   - Probabilidade: 50%  
   - Descrição: Possibilidade de alinhar a equipe e fortalecer a colaboração entendendo melhor os erros e acertos das sprints anteriores.  
   - Responsável: Scrum Master  
   - Plano de Ação: Fazer sessões de feedback e dinâmicas de grupo para melhorar a comunicação.

5. **Capacitação técnica interna**  
   - Impacto: Moderado  
   - Probabilidade: 50%  
   - Descrição: Aumento do conhecimento técnico do grupo.  
   - Responsável: Time de Desenvolvimento  
   - Plano de Ação: Estudar além das aulas e autoestudos as tecnologias que serão necessárias.


### Sprint V

<div align="center">
<p><b>Quadro 5</b> - Matriz de Risco 5</p>
<img src="https://res.cloudinary.com/dyioydhrw/image/upload/v1734371563/Sprint_5_kfzziq.png" width="100%"></a>

<sup><b>Fonte:</b> Material produzido pelo Grupo Pérola Negra (2024)</sup>
</div>

#### Ameaças

1. **Tempo insuficiente para a entrega final**  
   - Impacto: Muito Alto  
   - Probabilidade: 90%  
   - Descrição: Apenas uma semana de trabalho pode comprometer a qualidade e o prazo das entregas.  
   - Responsável: Scrum Master  
   - Plano de Ação: Priorizar as tarefas mais críticas e realizar revisões diárias para mitigar atrasos.  

2. **Sobrecarga de Trabalho**  
   - Impacto: Alto  
   - Probabilidade: 70%  
   - Descrição: A pressão para cumprir o prazo pode sobrecarregar os membros da equipe, afetando a produtividade.  
   - Responsável: PO  
   - Plano de Ação: Dividir as tarefas de forma equilibrada e estabelecer períodos curtos de descanso.  

3. **Falta de alinhamento interno**  
   - Impacto: Moderado  
   - Probabilidade: 50%  
   - Descrição: Divergências entre os membros sobre prioridades podem atrasar o progresso das entregas.  
   - Responsável: Scrum Master  
   - Plano de Ação: Promover reuniões rápidas de alinhamento e priorizar a comunicação clara.  

#### Oportunidades 

1. **Melhoria no DataAPP com base em feedback**  
   - Impacto: Muito Alto  
   - Probabilidade: 90%  
   - Descrição: Incorporar melhorias com base nos feedbacks pode aumentar significativamente a qualidade do produto.  
   - Responsável: Time de Desenvolvimento  
   - Plano de Ação: Priorizar o feedback crítico e implementá-lo rapidamente.  

2. **Entrega do Pipeline**  
   - Impacto: Alto  
   - Probabilidade: 70%  
   - Descrição: Demonstrar a arquitetura completa do pipeline pode reforçar a competência técnica do grupo.  
   - Responsável: Time de Desenvolvimento  
   - Plano de Ação: Garantir que todas as etapas do pipeline sejam devidamente integradas e testadas.  

4. **DataAPP interativo**  
   - Impacto: Muito Alto  
   - Probabilidade: 70%  
   - Descrição: Entregar um aplicativo com alto nível de interatividade pode agregar valor ao projeto e garantir alta usabilidade.  
   - Responsável: Time de Desenvolvimento
   - Plano de Ação: Realizar testes e ajustar funcionalidades com base nos resultados.  

### Conclusão

&emsp;&emsp;A matriz de risco, acompanhada dos planos de ação, facilita o reconhecimento de oportunidades que podem preparar e fortalecer o grupo, ao mesmo tempo em que permite uma abordagem preventiva diante das ameaças identificadas. Com esse mapeamento claro, a equipe está mais bem equipada para evitar situações que possam prejudicar o andamento do projeto ou afetar stakeholders importantes. Assim, o grupo consegue atuar de forma mais estratégica, garantindo tanto a mitigação de riscos quanto o aproveitamento de oportunidades para o sucesso do MVP.

<br>

## 4.3. Total Addressable Market (TAM)
&emsp;&emsp;A Companhia Paulista de Trens Metropolitanos (CPTM) desempenha um papel fundamental no transporte público do Estado de São Paulo, servindo uma vasta população que depende desse sistema ferroviário para seus deslocamentos diários. Para entender o potencial econômico deste serviço, é essencial analisar três componentes-chave: o **Mercado Total Endereçável** (**TAM**), o **Mercado Disponível e Endereçável** (**SAM**) e o **Mercado Obtível** (**SOM**). Esses parâmetros permitem avaliar o alcance e a viabilidade financeira da CPTM dentro de uma das maiores regiões metropolitanas do Brasil.

&emsp;&emsp;Como a CPTM é uma empresa pública do Governo de São Paulo, seus clientes em potencial são todos os cidadãos do estado. No entanto, para calcular o **TAM**, é preciso considerar o alcance geográfico dos serviços oferecidos. Assim, o **TAM** da CPTM inclui a população dos municípios por onde suas linhas passam:

1. **Caieiras**: 95.032
2. **Campo Limpo Paulista**: 77.632
3. **Ferraz de Vasconcelo**s: 179.198
4. **Francisco Morato**: 165.139
5. **Franco da Rocha**: 144.849
6. **Guarulhos**: 1.291.771
7. **Itaquaquecetuba**: 369.275
8. **Jundiaí**: 443.221
9. **Mauá**: 418.261
10. **Mogi das Cruzes**: 451.505
11. **Poá**: 103.765
12. **Ribeirão Pires**: 115.559
13. **Rio Grande da Serra**: 44.170
14. **Santo André**: 748.919
15. **São Caetano do Sul**: 165.655
16. **São Paulo**: 11.451.999
17. **Suzano**: 307.429
18. **Várzea Paulista**: 115.771

&emsp;&emsp;Com uma população total de **16.689.150 pessoas** nos municípios atendidos, o **TAM** reflete o potencial máximo de mercado em termos de bilhetes diários. Considerando um valor de R\$5,00 por bilhete e a hipótese de que cada pessoa faça duas viagens por dia (ida e volta), o **TAM** diário seria:

&emsp;&emsp;**TAM = 16.689.150 pessoas x R$5,00 x 2 bilhetes = R$166.891.500,00** em bilhetes diários potenciais.

## 4.4. Service Addressable Market (SAM)

&emsp;&emsp;Para calcular o **SAM**, é necessário excluir a população que tem acesso a transporte particular, como carros ou motos. Segundo o IPEA, **54% dos domicílios no Sudeste possuem um veículo**, o que reduz a necessidade de transporte público para uma parcela significativa da população.

&emsp;&emsp;Portanto, **46%** da população das cidades atendidas pela CPTM ainda depende do transporte público. Logo, o **SAM** pode ser calculado como:

&emsp;&emsp;**SAM = 46% de 16.689.150 pessoas = 7.677.009 pessoas** (sem acesso regular a carro/moto).

<br>
O potencial de receita em bilhetes diários seria:

&emsp;&emsp;**SAM = 7.677.009 pessoas x R\$5,00 x 2 bilhetes = R\$76.770.090,00** em bilhetes diários potenciais.

## 4.5. Service Obtainable Market (SOM)

&emsp;&emsp;Para calcular o **SOM**, utilizamos dados reais sobre o número de passageiros diários da CPTM. Atualmente, cerca de **3,2 milhões de pessoas** utilizam o sistema de trens diariamente.

&emsp;&emsp;Logo, o **SOM** em termos de receita diária seria:

&emsp;&emsp;**SOM = 3.200.000 pessoas x R\$5,00 x 2 bilhetes = R\$32.000.000,00** em bilhetes diários potenciais.

&emsp;&emsp;A análise do **TAM**, **SAM** e **SOM** permite uma visão clara do potencial de mercado da CPTM. Com um **TAM** de R\$166,9 milhões em bilhetes diários, reduzido para um **SAM** de R\$76,7 milhões, e um **SOM** mais realista de R\$32 milhões, é possível ver o impacto direto dos fatores de mobilidade e posse de veículos na receita potencial. Essas métricas auxiliam no planejamento e na tomada de decisões para otimizar o serviço da CPTM e aumentar sua eficiência operacional e financeira.

<br>

# 5. Análise Financeira

&emsp;&emsp;A análise financeira é uma etapa essencial em qualquer processo de avaliação e tomada de decisão relacionado a novos investimentos. Essa prática abrange diferentes tipos de organizações, como empresas privadas, entidades sem fins lucrativos e instituições estatais, garantindo uma avaliação aprofundada da viabilidade e dos riscos envolvidos, além de fornecer bases sólidas para decisões estratégicas.

## 5.1. Custos de Implementação e Manutenção

&emsp;&emsp;Na análise financeira para a implementação e manutenção do projeto, são considerados aspectos fundamentais, como a utilização de premissas predefinidas e a necessidade de contratação de mão de obra especializada. Esses fatores são cruciais para assegurar a precisão das projeções e o sucesso na execução.

&emsp;&emsp;Abaixo, é apresentada uma tabela com a estrutura de custos esperada para a implementação e manutenção do projeto, considerando que ele será realizado *on premise* (executado em software local).

<div align="center">
<p><b>Tabela 1</b> - Estrutura de Custos</p>

| Categoria | Nome | Custo Fracionado | Custo Total | Fonte |
| --- | --- | --- | --- | --- |
| Infraestrutura | Servidor Local | R$0,00 (Estado) | R$0,00 | CPTM |
| Tecnologia | Docker | R$0,00 (Open Source) | R$0,00 | Próprio Site |
| Tecnologia | DBeaver | R$0,00 (Open Source) | R$0,00 | Próprio Site |
| Tecnologia | Python | R$0,00 (Open Source) | R$0,00 | Próprio Site |
| Tecnologia | Prefect | R$0,00 (Open Source) | R$0,00 | Próprio Site |
| Tecnologia | Streamlit | R$0,00 (Open Source) | R$0,00 | Próprio Site |
| Mão de Obra | 2 Cientistas de Dados | R$30,77/hora cada | R$8.100,20 (cada) | [Talent, 2024](https://br.talent.com/) |
| Mão de Obra | 2 Analistas de Dados | R$23,28/hora cada | R$6.458,40 (cada) | [Talent, 2024](https://br.talent.com/) |
| Mão de Obra | Engenheiro de Software | R$41,54/hora | R$10.460,99 | [Talent, 2024](https://br.talent.com/) |
| Mão de Obra | Product Owner | R$36,92/hora | R$9.448,28 | [Talent, 2024](https://br.talent.com/) |
| Mão de Obra | Product Manager | R$12,31/hora | R$4.053,77 | [Talent, 2024](https://br.talent.com/) |
| **TOTAL/MÊS** | - | - | **R$53.080,24/mês** | - |
| **TOTAL/ANO** | - | - | **R$636.962,93/ano** | - |

<sup><b>Fonte:</b> Material produzido pelo Grupo Pérola Negra (2024)</sup>
</div>

### Detalhamento dos Custos por Membro da Equipe

&emsp;&emsp;A tabela abaixo apresenta os custos detalhados de cada cargo, incluindo salário base, benefícios e encargos tributários, para fornecer uma visão completa dos valores investidos na equipe.

<div align="center">
<p><b>Tabela 2</b> - Estrutura de Custos Detalhados</p>

| Cargo | Escopo | Valor/Hora | Carga Horária | Salário Total | Benefícios ([VC S/A, 2024](https://vocesa.abril.com.br/)) | Renda Total | Impostos (37% do salário líquido) ([Catho, 2024](https://catho.com.br/)) | Custo Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 Cientistas de Dados | Otimização do ETL | R$30,77/hora | 160h/mês | R$4.923,20 | VR: R$1.135,42VT: R$220,00 | R$6.278,62 | R$1.821,58 | R$8.100,20 (cada) |
| 2 Analistas de Dados | Criação de Views e Dashboards | R$23,28/hora | 160h/mês | R$3.724,80 | VR: R$1.135,42VT: R$220,00 | R$5.080,22 | R$1.378,18 | R$6.458,40 (cada) |
| Engenheiro de Software | Front-end e Arquitetura | R$41,54/hora | 160h/mês | R$6.646,40 | VR: R$1.135,42VT: R$220,00 | R$8.001,82 | R$2.459,17 | R$10.460,99 |
| Product Owner | Gestão do projeto | R$36,92/hora | 160h/mês | R$5.907,20 | VR: R$1.135,42VT: R$220,00 | R$7.262,62 | R$2.185,66 | R$9.448,28 |
| Product Manager | Recolhimento de demandas e métricas | R$12,31/hora | 160h/mês | R$1.969,60 | VR: R$1.135,42VT: R$220,00 | R$3.325,02 | R$728,75 | R$4.053,77 |
| **TOTAL/MÊS** | - | - | - | **R$31.819,20/mês** | - | **R$41.307,14/mês** | **R$11.773,10/mês** | **R$53.080,24/mês** |
| **TOTAL/ANO** | - | - | - | - | - | - | **R$636.962,93/ano** |  |

<sup><b>Fonte:</b> Material produzido pelo Grupo Pérola Negra (2024)</sup>
</div>

### Explicações Importantes

&emsp;&emsp;Aqui, é relevante ressaltar a diferença entre **salário** e **renda**:

- **Salário**: Refere-se ao montante associado às horas trabalhadas.
- **Renda**: Inclui o total recebido, considerando benefícios e outras fontes de receita.

&emsp;&emsp;Os conceitos acima foram detalhados para demonstrar os custos totais de cada funcionário, desde o salário base até os impostos que a empresa deve arcar sobre cada cargo.

## 5.2. Custos de Desenvolvimento

&emsp;&emsp;Além dos custos de implementação e manutenção, também é apresentada a estrutura de custos relacionada à ideação e ao desenvolvimento do projeto. Isso garante transparência e detalhamento sobre os recursos utilizados, sejam tecnologias, infraestrutura ou mão de obra.

<div align="center">
<p><b>Tabela 3</b> - Estrutura de Custos de Desenvolvimento</p>

| Categoria | Nome | Custo Fracionado | Custo Total |
| --- | --- | --- | --- |
| Infraestrutura | Amazon S3 | R$0,00 (Patrocínio) | R$0,00 |
| Tecnologia | Docker | R$0,00 (Open Source) | R$0,00 |
| Tecnologia | DBeaver | R$0,00 (Open Source) | R$0,00 |
| Tecnologia | Python | R$0,00 (Open Source) | R$0,00 |
| Tecnologia | Prefect | R$0,00 (Open Source) | R$0,00 |
| Tecnologia | Streamlit | R$0,00 (Open Source) | R$0,00 |
| Mão de Obra | Desenvolvedores (6 alunos) | R$0,00 (Alunos) | R$0,00 |
| **TOTAL** | - | - | **R$0,00** |

<sup><b>Fonte:</b> Material produzido pelo Grupo Pérola Negra (2024)</sup>
</div>

### Observação

&emsp;&emsp;Embora seja possível calcular um valor representativo para os custos de desenvolvimento, ele não reflete a realidade, pois, na prática, não houve aporte financeiro da cliente (CPTM). Assim, optou-se por descrever os recursos utilizados para manter a transparência, sem atribuir custos monetários fictícios.

## 5.3. ROI (Return On Investment)

&emsp;&emsp;Com base nos custos detalhados, é possível estimar as receitas potenciais que o projeto pode gerar para a CPTM. De acordo com a análise TAM-SAM-SOM, cerca de 3,2 milhões de pessoas utilizam transporte público diariamente, enquanto o público endereçável da CPTM é estimado em aproximadamente 7,7 milhões de indivíduos. Melhorias no sistema ferroviário têm demonstrado resultados significativos em outros países. Na Europa, por exemplo, houve aumentos expressivos no uso de trens após reformas: na Espanha, o incremento foi de 26%, e na Itália, de 18,7% ([Railway, 2023](https://www.railway.supply/en/significant-growth-in-rail-passenger-transport-across-europe-in-2023/)).

&emsp;&emsp;Esses dados sugerem que melhorias no sistema ferroviário têm o potencial de aumentar significativamente a utilização dos serviços e, consequentemente, as receitas geradas. Aplicando uma estimativa conservadora de aumento de 10% no uso diário dos trens da CPTM, isso representaria uma receita adicional de R$3,2 milhões por dia. Em um mês, considerando apenas dias úteis, o incremento seria de R$70,4 milhões, totalizando R$844,8 milhões em um ano.

&emsp;&emsp;Com base nesses números, o ROI (Retorno sobre Investimento) do projeto pode ser calculado. O ROI é uma métrica essencial para avaliar a viabilidade de um investimento, sendo obtido pela fórmula: subtraímos o custo total do investimento da receita adicional gerada, dividimos o resultado pelo custo total e multiplicamos por 100. No caso deste projeto, com um custo total estimado de R$636.962,928, o ROI é calculado como:

**ROI = [(70.400.000 - 636.962,928) / 636.962,928] x 100 = 109,52 x 100 = 10.952,44%**

&emsp;&emsp;Este resultado reflete um retorno excepcionalmente elevado, evidenciando o enorme potencial do projeto para gerar impacto financeiro positivo para a CPTM, além de reforçar a viabilidade e a atratividade do investimento.

## 5.4. Conclusão

&emsp;&emsp;A análise financeira realizada evidencia a importância de um planejamento detalhado e transparente para o sucesso do projeto. Com a identificação clara dos custos de implementação, manutenção e desenvolvimento, foi possível estabelecer uma base sólida para avaliar a viabilidade do investimento e suas implicações estratégicas.

&emsp;&emsp;Além disso, a projeção de possíveis retornos com base em estudos e casos internacionais demonstra que melhorias no sistema ferroviário têm o potencial de gerar impactos positivos, tanto no aumento da utilização do transporte quanto nas receitas da CPTM. Esses indicadores reforçam a relevância do projeto e o papel essencial da gestão eficiente de recursos para alcançar resultados sustentáveis.

&emsp;&emsp;Portanto, a decisão de avançar com o projeto deve considerar tanto os benefícios tangíveis quanto os intangíveis, garantindo que as melhorias propostas atendam às expectativas de usuários e stakeholders, contribuindo para o desenvolvimento da infraestrutura de transporte público e para a qualidade de vida na região.

<br>

# 6. Plano de Comunicação

&emsp;&emsp;Esta seção detalha o plano de comunicação estabelecido para o projeto com a CPTM, incluindo objetivos, stakeholders, mensagens-chave, canais de comunicação, plano de implementação, medidas de sucesso, feedback e ajustes. O objetivo é garantir uma comunicação eficaz entre todos os envolvidos, promovendo alinhamento, transparência e eficiência.

## 6.1. Objetivo

&emsp;&emsp;O plano de comunicação tem como objetivo assegurar que todos os stakeholders estejam alinhados em relação ao progresso, desafios e entregas do projeto. Ele promove transparência, colaboração e uma tomada de decisão eficiente, facilitando o fluxo de informações entre os diferentes níveis do projeto. Isso minimiza ruídos e maximiza a eficiência da equipe.

## 6.2. Stakeholders

&emsp;&emsp;Esta seção apresenta os stakeholders do projeto, descrevendo seus papéis e como se comunicam entre si. Também explicita a hierarquia e responsabilidades.

**Principais Stakeholders e seus Papéis**

- **Time de Desenvolvimento:**
  - **Grupo Pérola Negra:** Responsável pelo desenvolvimento técnico da solução.

- **Product Owner (PO):**
  - **Membros Rotativos do Grupo Pérola Negra:** Coordenam as necessidades do cliente com a equipe de desenvolvimento.
    - **Quadro de PO:**

      <div align="center">
      <p><b>Quadro 6</b> - Quadro de PO</p>

            | Sprint | Product Owner |
            |--------|---------------|
            | Sprint 1 | Nicolas       |
            | Sprint 2 | Lucas         |
            | Sprint 3 | Eduardo       |
            | Sprint 4 | Ana           |
            | Sprint 5 | Nicollas      |

      <sup><b>Fonte:</b> Material produzido pelo Grupo Pérola Negra (2024)</sup>
      </div>

- **Scrum Master:**
  - **Membros Rotativos do Grupo Pérola Negra:** Facilitam a metodologia ágil e garantem a remoção de impedimentos.
    - **Quadro de Scrum Master:**

<div align="center">
<p><b>Quadro 7</b> - Quadro de Scrum Master</p>

            | Sprint | Scrum Master |
            |--------|--------------|
            | Sprint 1 | Sophia      |
            | Sprint 2 | Keylla      |
            | Sprint 3 | Sophia      |
            | Sprint 4 | Eduardo     |
            | Sprint 5 | Lucas       |

<sup><b>Fonte:</b> Material produzido pelo Grupo Pérola Negra (2024)</sup>
</div>  

- **Orientador:**
  - **Renato Penha:** Orientador da Turma 10 de Sistemas de Informação, fornece direcionamento técnico e metodológico.

- **Coordenador do Curso:**
  - **Egon Daxbacher:** Coordena o curso e oferece suporte acadêmico ao projeto.

- **Líder do Projeto:**
  - **Roberto Morina:** Gerencia a equipe e assegura que as metas e entregas sejam alcançadas.

- **Ponto Focal Backup:**
  - **Sarah de Sá Fernandes:** Serve como ponto de contato secundário, garantindo continuidade em casos de ausência do líder.

- **Líder Técnico:**
  - **Roberto Morina:** Fornece liderança técnica e orienta o desenvolvimento da solução.

- **Líder de Negócio:**
  - **Sarah de Sá Fernandes:** Garante que a solução atenda aos objetivos de negócio e à estratégia da CPTM.

- **Líder Executivo:**
  - **Maicon Satiro de Oliveira:** Representa a alta gestão da CPTM e toma decisões estratégicas para o projeto.

**Comunicação entre Stakeholders:**

- O **Time de Desenvolvimento** reporta diretamente ao **Scrum Master** e ao **Product Owner**, que organizam e priorizam as entregas.
- O **Scrum Master** facilita a comunicação com o orientador e a alta gestão.
- O **Product Owner** é o responsável por comunicar os requisitos recebidos da CPTM para o time de desenvolvimento.
- A **Sarah de Sá Fernandes**, como ponto focal backup e líder de negócio, intermedia possíveis pedidos do time de desenvolvimento ao time técnico da CPTM.
- O **Orientador** revisa entregas e garante a aderência às diretrizes do curso.

&emsp;&emsp; Para facilitar o acesso às informações sobre os stakeholders, veja a tabela abaixo, que traz o stakeholder, se ele é interno ou externo, suas expectativas e sua influência:

<div align="center">
<p><b>Tabela 4</b> - Expectativa e Influência</p>

| **Stakeholder**             | **Tipo**    | **Expectativa**                                                                                                                                                                      | **Influência**                                                                                                       |
|------------------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| **Time de Desenvolvimento** | Interno     | Concluir o desenvolvimento técnico da solução de forma eficiente, atendendo aos requisitos e prazos estabelecidos.                                                                  | Alta - Responsável pela entrega técnica e resolução de desafios.                                                   |
| **Product Owner (PO)**       | Interno     | Garantir que os requisitos da CPTM sejam entendidos e priorizados corretamente, comunicando as necessidades do cliente ao time de desenvolvimento.                                   | Alta - Define prioridades e reflete as expectativas do cliente no produto.                                         |
| **Scrum Master**             | Interno     | Facilitar a execução da metodologia ágil, removendo impedimentos e garantindo o progresso contínuo do projeto.                                                                      | Média - Influencia o andamento das sprints, mas não define requisitos diretamente.                                  |
| **Orientador (Renato Penha)**| Interno     | Fornecer direcionamento técnico e metodológico, ajudando a manter o projeto dentro dos padrões acadêmicos e profissionais exigidos.                                                  | Alta - Atua como guia técnico e garante alinhamento com a metodologia acadêmica.                                   |
| **Coordenador do Curso**     | Interno     | Assegurar que o projeto esteja alinhado aos objetivos do curso e às expectativas da instituição de ensino.                                                                           | Média - Garante alinhamento acadêmico, mas não interfere diretamente no desenvolvimento diário.                    |
| **Líder do Projeto**         | Externo     | Gerenciar o time, alinhar entregas e coordenar as interações entre stakeholders internos e externos.                                                                                 | Alta - Centraliza a organização e garante a entrega dos objetivos do projeto.                                      |
| **Ponto Focal Backup**       | Externo     | Assegurar continuidade em casos de ausência do líder, respondendo por questões críticas e mantendo alinhamento com os stakeholders principais.                                       | Média - Atua como suporte, mas sua influência é limitada à ausência do líder.                                      |
| **Líder Técnico**            | Externo     | Fornecer suporte técnico ao time de desenvolvimento e assegurar a qualidade técnica das entregas.                                                                                    | Alta - Central na supervisão técnica e qualidade das soluções implementadas.                                       |
| **Líder de Negócio**         | Externo     | Garantir que a solução atenda às metas estratégicas da CPTM e aos objetivos do cliente, validando requisitos de negócio.                                                             | Alta - Influencia diretamente na adequação do projeto às expectativas estratégicas da CPTM.                        |
| **Líder Executivo (Maicon)** | Externo     | Representar a alta gestão da CPTM, assegurando que o projeto esteja alinhado aos objetivos estratégicos e aprovando decisões críticas.                                               | Alta - Principal tomador de decisões estratégicas e aprovador final das entregas do projeto.                       |
| **CPTM (Gestão e Operação)** | Externo     | Receber atualizações claras sobre o progresso do projeto e entender como ele impactará a operação, esperando uma solução prática e viável.                                           | Alta - Define os requisitos gerais e valida a usabilidade da solução proposta.                                     |
| **Time Técnico da CPTM**     | Externo     | Garantir que os requisitos técnicos estejam claros e sejam cumpridos, fornecendo suporte técnico quando necessário.                                                                 | Média - Influencia tecnicamente o escopo, mas depende de alinhamentos internos para mudanças estruturais.          |
| **Faculdade Inteli**         | Interno     | Observar o desempenho do grupo no projeto, avaliando como ele reflete o aprendizado e os objetivos do curso, além de manter a parceria com a CPTM.                                   | Média - Não interfere diretamente no projeto, mas influencia o alinhamento geral com os objetivos educacionais.    |

<sup><b>Fonte:</b> Material produzido pelo Grupo Pérola Negra (2024)</sup>
</div>
      

&emsp;&emsp;E para Para tornar o fluxo de comunicação entre os stakeholders mais intuitivo, veja a figura abaixo, que apresenta um diagrama de comunicação entre eles, ilustrando tudo que foi falado anteriormente. Outras informações são aplicados nas demais subseções da seção 6. 

<div align="center">
<p><b>Figura 6</b> - Diagrama de Stakeholders</p>
<img src="https://res.cloudinary.com/dmornatkl/image/upload/v1732732406/Inserir_um_t%C3%ADtulo_8_jv82wl.png" width="100%"></a>

<sup><b>Fonte:</b> Material produzido pelo Grupo Pérola Negra (2024)</sup>
</div>


## 6.3. Mensagens-Chave

&emsp;&emsp;Esta seção define as principais mensagens que serão transmitidas aos stakeholders, adaptadas às suas necessidades e expectativas.

**Principais Mensagens:**

- **Para a CPTM (Gestão e Operação):**
  - Atualizações sobre o progresso do projeto.
  - Alinhamento sobre requisitos e impactos operacionais.

- **Para o Time Acadêmico:**
  - Orientações sobre as entregas técnicas.
  - Suporte metodológico e acadêmico.

- **Para a Equipe de Desenvolvimento:**
  - Priorização de tarefas.
  - Refinamento de funcionalidades.
  - Resolução de impedimentos.

## 6.4. Canais de Comunicação

&emsp;&emsp;Nesta seção, descrevemos os canais de comunicação escolhidos, considerando a natureza de cada mensagem e a frequência ideal de uso.

- **Reuniões:**
  - **Daily Meetings (Grupo Pérola Negra):** Realizadas ao longo da semana para refinamento de tarefas e alinhamento interno.
  - **Reuniões de Entrega de Sprint:** Realizadas quinzenalmente com Sarah de Sá Fernandes para discutir entregas e alinhar dúvidas.

- **Ferramentas Digitais:**
  - **Google Meet:** Para comunicação entre stakeholders e reuniões virtuais.
  - **E-mail:** Para formalizações e envio de relatórios e comunicação emergencial.
  - **Slack:** Para comunicação rápida entre os membros do Grupo Pérola Negra.

## 6.5. Plano de Implementação

&emsp;&emsp;Esta seção descreve como o plano de comunicação será implementado, detalhando etapas e responsabilidades.

**Etapas do Plano:**

1. **Definição da Frequência:**
   - Dailies semanais para alinhamento técnico.
   - Reuniões quinzenais com os principais stakeholders (Sarah e Roberto Morina).

2. **Responsáveis pela Comunicação:**
   - O Scrum Master e o Product Owner garantem que o plano seja seguido e que todos sejam atualizados, sendo eles que apresentam as atividades feitas ao longo de cada sprint.

3. **Controle de Qualidade:**
   - Revisão das mensagens e feedback constante dos stakeholders para garantir clareza e eficiência.

## 6.6. Medidas de Sucesso

&emsp;&emsp;Os indicadores de sucesso avaliados para o plano de comunicação incluem:

- Taxa mínima de participação nas reuniões: **90%**.
- Tempo médio para resolução de dúvidas pendentes: **inferior a 72 horas**.
- Feedback positivo dos stakeholders em relação à clareza e eficiência da comunicação: **70% ou mais**.
- Completude de mais de **70% das tarefas** da sprint, apresentadas no status report na entrega da sprint.

## 6.7. Feedback e Ajustes

&emsp;&emsp;Esta seção explica como o feedback será coletado e os ajustes realizados.

**Plano para Ajustes:**

1. **Coleta de Feedback:**
   - Questionários quinzenais para avaliar a efetividade dos canais, mensagens e entregas da sprint.
   - Sessões de revisão com o orientador (Renato Penha) para alinhamento com o TAPI (Termo de Abertura do Projeto do Inteli) e Lean Inception da seção 3.

2. **Ajustes Necessários:**
   - Redefinição da frequência das reuniões, se necessário.
   - Adaptação dos canais de comunicação para atender às demandas do projeto.

<br>

# 7. Conclusões

&emsp;&emsp;Mais do que um simples resumo do que já foi dito, as conclusões do projeto mostram a evolução de toda a equipe e a construção de um alicerce sólido para que a CPTM passe a tomar decisões guiadas por dados. Não foi só alinhar objetivos, delimitar escopo ou fazer análises estatísticas, mas também avanços para uma visão integrada, que combina a mudança cultural na forma de lidar com informação e a criação de uma base tecnológica robusta, segura e escalável.

&emsp;&emsp;Partimos de um diagnóstico realista, olhando para as brechas na operação e para o potencial inexplorado do volume de dados gerados diariamente. Assim, desenhamos um pipeline de Big Data não para ter mais números, mas sim para transformá-los em insights práticos e úteis. Além das ferramentas técnicas usadas (como Data Lake, ETL e dashboards), buscamos criar um projeto para, futuramente, aplicar previsões mais precisas, análises em tempo real e um aperfeiçoamento constante das rotinas de manutenção e planejamento.

&emsp;&emsp;Porém, não ficamos só na parte técnica. Ao esclarecer quem são os stakeholders, como se dá a comunicação entre eles e como manter um fluxo de feedback constante, ampliamos o impacto da solução. Isso garante que o conhecimento gerado não se perca na complexidade da empresa. Ao integrar áreas internas da CPTM e conectar o time técnico ao gerencial e acadêmico, a iniciativa deixa de ser um produto fechado para se tornar um processo contínuo de melhoria. Cada sprint, ajuste ou análise alimenta um ciclo que faz a empresa crescer em maturidade.

&emsp;&emsp;A análise financeira reforça a importância estratégica de apostar em dados. Não é só economizar ou aumentar a eficiência: é colocar a CPTM em outro patamar competitivo, algo especialmente relevante num serviço público que influencia a mobilidade e a qualidade de vida da população.

&emsp;&emsp;Chegar até aqui não significou apenas colocar um projeto no papel, mas criar as bases para um ecossistema de dados mais esperto. O próximo passo não é simplesmente "codificar o que falta", mas consolidar essas diretrizes como um padrão de qualidade. O objetivo é que, a partir desse ponto, cada novo insight ajude a CPTM a antecipar demandas, melhorar o serviço, economizar recursos e, principalmente, aprender continuamente.

<br>

# 8. Referências


**ALESP.** Lei nº 7.861, de 28 de maio de 1992. 28 maio 1996. Disponível em: https://www.al.sp.gov.br/repositorio/legislacao/lei/1992/lei-7861-28.05.1992.html. Acesso em: 19 out. 2024.

**CAROLI, Paulo.** 3 Differences Between Design Sprint and Lean Inception You Need To Know. Disponível em: https://caroli.org/3-differences-between-design-sprint-and-lean-inception-you-need-to-know/. Acesso em: 20 ago. 2024.

**CAROLI, Paulo.** Lean Inception: How to Align People and Build the Right Product. Disponível em: https://caroli.org/lean-inception-3/. Acesso em: 20 ago. 2024.

**CAROLI, Paulo.** Learn Lean Inception at Caroli.org. Disponível em: https://caroli.org/lean-inception-how-to-align-people-and-build-the-right-product/. Acesso em: 20 ago. 2024.

**CAROLI, Paulo.** Why did the Lean Inception creator get involved with Data Mesh?. Disponível em: https://caroli.org/why-did-the-lean-inception-creator-get-involved-with-data-mesh/. Acesso em: 20 ago. 2024.

**CARVALHO, Leandro S.** Data Product Canvas. Disponível em: https://medium.com/@leandroscarvalho/data-product-canvas-cd91f24776b1. Acesso em: 10 set. 2024.

**GUSHIKEN, A.** (2023, 23 de outubro). Value Proposition Canvas: o que é e como funciona essa metodologia? G4 Educação. https://g4educacao.com/portal/value-proposition-canvas. Acesso em: 17 out. 2024.

**HILLSON, D.; SIMON, P.** Practical project risk management : the ATOM methodology. Tysons Corner, Va.: Management Concepts, 2012.

**STICKDORN, M.; SCHNEIDER, J.** This is service design thinking basics, tools, cases. [s.l.] Amsterdam Bis Publ, 2015.

**TALENT.COM.** (2024). Salário médio de Cientista de Dados em Brasil 2024. Talent.com. https://br.talent.com/salary?job=cientista+de+dados#:~:text=Sal%C3%A1rio%20M%C3%A9dio%20de%20Cientista%20De%20Dados%20em%20Brasil%202024&text=O%20sal%C3%A1rio%20m%C3%A9dio%20de%20cientista,a%20ganhar%20R%24105.003%20anuais. Acesso em: 3 dez. 2024.  

**TALENT.COM.** (2024). Salário médio de Analista de Dados em Brasil 2024. Talent.com. https://br.talent.com/salary?job=analista+de+dados#:~:text=Sal%C3%A1rio%20M%C3%A9dio%20de%20Analista%20De%20Dados%20em%20Brasil%202024&text=O%20sal%C3%A1rio%20m%C3%A9dio%20de%20analista,a%20ganhar%20R%2474.755%20anuais. Acesso em: 3 dez. 2024.  

**TALENT.COM.** (2024). Salário médio de Engenheiro de Software. Talent.com. https://br.talent.com/salary?job=engenheiro+de+software. Acesso em: 3 dez. 2024.  

**TALENT.COM.** (2024). Salário médio de Product Owner. Talent.com. https://br.talent.com/salary?job=product+owner. Acesso em: 3 dez. 2024.  

**TALENT.COM.** (2024). Salário médio de Product Manager. Talent.com. https://br.talent.com/salary?job=product+manager. Acesso em: 3 dez. 2024.  

**RAILWAY SUPPLY.** (2023). Significant growth in rail passenger transport across Europe in 2023. Railway Supply. https://www.railway.supply/en/significant-growth-in-rail-passenger-transport-across-europe-in-2023/. Acesso em: 3 dez. 2024.  

**EUROSTAT.** (2023). Railway passenger transport statistics - quarterly and annual data. Eurostat. https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Railway_passenger_transport_statistics_-_quarterly_and_annual_data. Acesso em: 3 dez. 2024.  

**VOCÊ S/A.** Vale-refeição dura 10 dias por mês no Brasil, mostra pesquisa. Disponível em: https://vocesa.abril.com.br/economia/vale-refeicao-dura-10-dias-por-mes-no-brasil-mostra-pesquisa. Acesso em: 8 dez. 2024.

**CATHO PARA EMPRESAS.** Quanto custa um funcionário para a empresa? Disponível em: https://paraempresas.catho.com.br/quanto-custa-um-funcionario-para-empresa/#:~:text=Somados%2C%20os%20encargos%20equivalem%20a,da%20empresa%20vai%20precisar%20desembolsar. Acesso em: 8 dez. 2024.

</div>