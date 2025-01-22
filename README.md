# AWS Glue ETL Project

Este repositório apresenta um projeto ETL de ponta a ponta utilizando AWS Glue, com foco em boas práticas e uma infraestrutura robusta para engenharia de dados. O projeto utiliza o dataset "Amazon Product Reviews" do Kaggle.

## Objetivo do Projeto

O objetivo é demonstrar o processo de construção de um pipeline ETL com as melhores práticas, abordando:

- Integração com AWS Glue e outras ferramentas AWS.
- Construção de scripts de transformação em PySpark.
- Configuração de infraestrutura via AWS CLI e AWS Toolkit.
- Visualização e exploração de dados transformados.

## Estrutura do Projeto

### 1. Dataset

- **Fonte:** Amazon Product Reviews (disponível no Kaggle).
- **Descrição:** Avaliações de produtos da Amazon contendo metadados, notas e textos de revisão.

### 2. Ferramentas Utilizadas

- **Linguagens:** Python, PySpark.
- **Infraestrutura AWS:**
  - AWS Glue (Crawlers, Jobs, Data Catalog).
  - S3 (armazenamento de dados bruto e processado).
  - IAM (gerenciamento de permissões).
  - CloudWatch (monitoramento).
  - AWS CLI e AWS Toolkit para VSCode.

### 3. Etapas do Pipeline

#### a. Extração
- Upload dos dados brutos para um bucket no S3.
- Configuração de Glue Crawlers para catalogar os dados.

#### b. Transformação
- Desenvolvimento de scripts PySpark para:
  - Limpeza de dados (remoção de duplicatas, tratamento de valores nulos).
  - Enriquecimento de dados com colunas derivadas.
  - Agregações para sumarização de informações.

#### c. Carregamento
- Salvamento dos dados processados em diferentes camadas (bronze, silver, gold) no S3.
- Atualização do Glue Data Catalog com as tabelas transformadas.

### 4. Infraestrutura como Código

- Utilização de **Terraform** para provisionamento da infraestrutura AWS.
- Configuração de recursos como buckets S3, Glue Jobs e Crawlers automatizada.

### 5. Visualização e Análise

- Integração com ferramentas de BI (opcional, como QuickSight ou Tableau).
- Exportação de relatórios de análise com métricas das avaliações de produtos.

### 6. Documentação

#### Fluxo do Pipeline ETL

1. Upload dos dados brutos no S3.
2. Catalogação dos dados com Glue Crawlers.
3. Processamento e transformação em Glue Jobs.
4. Armazenamento dos dados transformados no S3.
5. Atualização do Glue Data Catalog para consulta via Athena.


## Requisitos

- Conta AWS configurada.
- AWS CLI e AWS Toolkit instalados.
- Ambiente Python configurado com dependências (veja o arquivo `requirements.txt`).

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/aws-glue-etl.git
   cd aws-glue-etl
   ```

2. Configure suas credenciais AWS:
   ```bash
   aws configure
   ```

3. Provisione a infraestrutura com Terraform:
   ```bash
   terraform init
   terraform apply
   ```

4. Execute o pipeline ETL via AWS Glue.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

---

### Autor

Este projeto foi desenvolvido por Cézar Augusto Meira Carmo ```dataengineercezar@gmail.com```, como parte do portfólio de engenharia de dados.
