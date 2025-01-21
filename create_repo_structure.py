import os

# Define a estrutura combinada do repositório
repo_structure = {
    "scripts": {
        "": ["setup-aws-cli.sh"],
        "glue-scripts": ["job1.py", "job2.py"]
    },
    "infra": [],
    "data": [],
    "docs": [],
    "terraform": ["main.tf", "variables.tf", "outputs.tf", "backend.tf"]
}

# Arquivos diretamente na raiz do repositório
root_files = ["aws-cli-commands.md", "README.md", ".gitignore"]

# Conteúdo básico para o README.md
readme_content = """# AWS Glue ETL Pipeline

Este repositório apresenta um pipeline ETL de ponta a ponta utilizando AWS Glue. Abrange desde a configuração de infraestrutura como código (IaC) até scripts PySpark para processamento de dados, oferecendo uma solução robusta e escalável para cenários reais de engenharia de dados.
"""

# Conteúdo básico para o .gitignore
gitignore_content = """*.pyc
__pycache__/
.env
.terraform/
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

# Função para criar arquivos com conteúdo opcional
def create_file(file_path, content=None):
    with open(file_path, "w") as file:
        if content:
            file.write(content)

# Função para criar a estrutura do repositório
def create_repo_structure(structure, root=""):
    for key, value in structure.items():
        current_path = os.path.join(root, key)
        
        if isinstance(value, dict):  # Diretório com subdiretórios ou arquivos
            os.makedirs(current_path, exist_ok=True)
            create_repo_structure(value, current_path)
        elif isinstance(value, list):  # Diretório com arquivos
            os.makedirs(current_path, exist_ok=True)
            for file in value:
                file_path = os.path.join(current_path, file)
                create_file(file_path)

# Cria arquivos na raiz do repositório
def create_root_files(files):
    for file in files:
        content = None
        if file == "README.md":
            content = readme_content
        elif file == ".gitignore":
            content = gitignore_content
        create_file(file, content)

# Executa as funções
create_repo_structure(repo_structure)
create_root_files(root_files)

print("Estrutura do repositório combinada criada com sucesso!")
