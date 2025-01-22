from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import functions as F
from awsglue.dynamicframe import DynamicFrame

# Inicializa o contexto do Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# 1. Extração dos dados do Glue Data Catalog
datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database="example_database",  # Substitua pelo nome do seu banco de dados no Glue Catalog
    table_name="reviews_csv",  # Substitua pelo nome da tabela criada pelo Crawler
    transformation_ctx="datasource0"
)

# 2. Converter DynamicFrame para DataFrame para facilitar a transformação
df = datasource0.toDF()

# 3. Limpeza dos dados: Remover linhas com a coluna 'Text' nula ou vazia
df_cleaned = df.filter(df["Text"].isNotNull())

# 4. Agregação: Calcular a média das avaliações por 'ProductId'
df_aggregated = df_cleaned.groupBy("ProductId").agg(
    F.avg("Score").alias("average_rating"),  # Cálculo da média das avaliações
    F.count("Text").alias("review_count")  # Contagem de reviews
)

# 5. Converter o DataFrame de volta para DynamicFrame
dynamic_frame_aggregated = DynamicFrame.fromDF(df_aggregated, glueContext, "dynamic_frame_aggregated")

# 6. Carga dos dados: Armazenar os dados no S3 em formato Parquet
s3_path = "s3://camc-glue-etl-bucket/processed/"  
glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame_aggregated,
    connection_type="s3",
    connection_options={"path": s3_path},
    format="parquet"
)
