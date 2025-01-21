from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import functions as F

# Iniciar o contexto do Glue e Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# 1. Extração: Carregar dados do Glue Data Catalog
datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database="example_database",  # Substitua pelo nome do seu banco de dados
    table_name="reviews_csv",     # Substitua pelo nome da tabela criada pelo Crawler
    transformation_ctx="datasource0"
)

# 2. Transformação: Limpeza e agregação dos dados
df = datasource0.toDF()

# Limpeza: Remover linhas com reviewText nulo ou vazio
df_cleaned = df.filter(df["reviewText"].isNotNull())

# Agregação: Calcular a média das avaliações por produto
df_aggregated = df_cleaned.groupBy("productTitle").agg(
    F.avg("rating").alias("average_rating"),
    F.count("reviewText").alias("review_count")
)

# 3. Carga: Armazenar os dados no S3 em formato Parquet
dynamic_frame_aggregated = glueContext.create_dynamic_frame.from_dataframe(df_aggregated, glueContext)

# Caminho do S3 para armazenar os dados processados
s3_path = "s3://camc-glue-etl-bucket/processed/"
glueContext.write_dynamic_frame.from_options(
    dynamic_frame_aggregated,
    connection_type="s3",
    connection_options={"path": s3_path},
    format="parquet"
)
