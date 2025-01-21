output "s3_bucket_name" {
  value = aws_s3_bucket.glue_bucket.bucket
}

output "glue_database_name" {
  value = aws_glue_catalog_database.example_database.name
}

output "glue_job_name" {
  value = aws_glue_job.example_job.name
}

output "glue_workflow_name" {
  value = aws_glue_workflow.example_workflow.name
}