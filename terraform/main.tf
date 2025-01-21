provider "aws" {
  region = "us-east-1"
}

# Bucket S3
resource "aws_s3_bucket" "glue_bucket" {
  bucket = "camc-glue-etl-bucket"
}

# resource "aws_s3_bucket_acl" "glue_bucket_acl" {
#   bucket = aws_s3_bucket.glue_bucket.id
#   acl    = "private"
# }

# Glue Database
resource "aws_glue_catalog_database" "example_database" {
  name = "example_database"
}

# Glue Crawler
resource "aws_glue_crawler" "example_crawler" {
  name          = "example-crawler"
  database_name = aws_glue_catalog_database.example_database.name
  role          = "arn:aws:iam::038462755196:role/GlueServiceRole"

  s3_target {
    path = "s3://${aws_s3_bucket.glue_bucket.bucket}/"
  }
}

resource "aws_glue_crawler" "product_reviews_crawler" {
  name            = "product-reviews-crawler"
  role            = "arn:aws:iam::038462755196:role/GlueServiceRole"
  database_name   = aws_glue_catalog_database.example_database.name

  s3_target {
    path = "s3://${aws_s3_bucket.glue_bucket.bucket}/raw"
  }

  configuration = jsonencode({
    "Version" = 1  # Especificando a versão da configuração
  })
}


# Glue Job
resource "aws_glue_job" "example_job" {
  name     = "example-job"
  role_arn = "arn:aws:iam::038462755196:role/GlueServiceRole"

  command {
    name            = "glueetl"
    script_location = "s3://${aws_s3_bucket.glue_bucket.bucket}/scripts/etl-script.py"
    python_version  = "3"
  }

  default_arguments = {
    "--TempDir" = "s3://${aws_s3_bucket.glue_bucket.bucket}/temp/"
  }
}

# Glue Workflow
resource "aws_glue_workflow" "example_workflow" {
  name = "example-workflow"
}