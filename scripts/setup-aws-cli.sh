#!/bin/bash

# Script para configurar AWS CLI e provisionar recursos iniciais para o projeto AWS Glue ETL

# Variáveis de entrada
AWS_REGION="us-east-1"          # Região da AWS
S3_BUCKET_NAME="aws-glue-etl-bucket" # Nome do bucket S3
IAM_ROLE_NAME="AWSGlueServiceRole"   # Nome da role IAM para o Glue

# Função para exibir mensagens de log
log() {
  echo "[INFO] $1"
}

# Validar se o AWS CLI está instalado
if ! command -v aws &> /dev/null
then
    echo "[ERRO] AWS CLI não está instalado. Por favor, instale antes de continuar."
    exit 1
fi

log "Iniciando configuração do AWS CLI para o projeto AWS Glue ETL."

# Configurar região no AWS CLI
log "Configurando região AWS para $AWS_REGION."
aws configure set region $AWS_REGION

# Criar bucket S3
log "Criando bucket S3: $S3_BUCKET_NAME."
aws s3 mb s3://$S3_BUCKET_NAME --region $AWS_REGION

# Criar role IAM para AWS Glue
log "Criando role IAM: $IAM_ROLE_NAME."
aws iam create-role \
    --role-name $IAM_ROLE_NAME \
    --assume-role-policy-document '{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "Service": "glue.amazonaws.com"
          },
          "Action": "sts:AssumeRole"
        }
      ]
    }'

# Anexar políticas à role IAM
log "Anexando políticas à role IAM $IAM_ROLE_NAME."
aws iam attach-role-policy \
    --role-name $IAM_ROLE_NAME \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole

log "Anexando política de acesso ao S3."
aws iam put-role-policy \
    --role-name $IAM_ROLE_NAME \
    --policy-name S3AccessPolicy \
    --policy-document '{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "s3:ListBucket",
            "s3:PutObject",
            "s3:GetObject"
          ],
          "Resource": [
            "arn:aws:s3:::'$S3_BUCKET_NAME'",
            "arn:aws:s3:::'$S3_BUCKET_NAME'/*"
          ]
        }
      ]
    }'

log "Configuração inicial do AWS CLI concluída com sucesso."

# Resumo das configurações
log "Resumo das configurações:"
log "- Bucket S3 criado: $S3_BUCKET_NAME"
log "- Role IAM criada: $IAM_ROLE_NAME com permissões para Glue e S3"

exit 0
