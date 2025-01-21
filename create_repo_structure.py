import os

# Define a estrutura do repositório
repo_structure = [
    "scripts",
    "infra",
    "data",
    "docs",
]

# Conteúdo básico para o README.md
readme_content = """# AWS Glue ETL Pipeline

Este repositório apresenta um pipeline ETL de ponta a ponta utilizando AWS Glue. Abrange desde a configuração de infraestrutura como código (IaC) até scripts PySpark para processamento de dados, oferecendo uma solução robusta e escalável para cenários reais de engenharia de dados.
"""

# Conteúdo básico para o requirements.txt
requirements_content = """boto3
pyspark
awswrangler
pandas
pyarrow
fastparquet
sqlalchemy
pyyaml
"""

# Função para criar a estrutura do repositório
def create_repo_structure():
    for directory in repo_structure:
        os.makedirs(directory, exist_ok=True)
    
    # Cria o README.md
    if not os.path.exists("README.md"):
        with open("README.md", "w") as readme_file:
            readme_file.write(readme_content)
    
    # Cria o requirements.txt
    if not os.path.exists("requirements.txt"):
        with open("requirements.txt", "w") as requirements_file:
            requirements_file.write(requirements_content)

    print("Estrutura do repositório criada com sucesso!")

# Executa a função
create_repo_structure()
