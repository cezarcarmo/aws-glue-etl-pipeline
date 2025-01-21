import os
import kaggle

def download_kaggle_dataset(dataset_name, output_path):
    """
    Função para baixar datasets do Kaggle.
    Args:
        dataset_name (str): Nome do dataset no Kaggle.
        output_path (str): Caminho onde o dataset será salvo.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    kaggle.api.dataset_download_files(dataset_name, path=output_path, unzip=True)
    print(f"Dataset baixado e armazenado em: {output_path}")

# Exemplo de uso
if __name__ == "__main__":
    dataset_name = "snap/amazon-fine-food-reviews"
    output_path = "./data/raw"
    download_kaggle_dataset(dataset_name, output_path)