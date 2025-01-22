# AWS CLI Commands for AWS Glue ETL Project

Este arquivo documenta os principais comandos do AWS CLI utilizados no projeto de ETL com AWS Glue, organizados por etapa do processo.

---

## Configuração Inicial

Configure as credenciais AWS para acesso:
```bash
aws configure
```
- Insira o ID da chave de acesso, chave secreta, região e formato de saída.

Verifique as credenciais configuradas:
```bash
aws sts get-caller-identity
```

---

## Gerenciamento de Buckets S3

### Criar um bucket:
```bash
aws s3 mb s3://<nome-do-bucket>
```

### Fazer upload de arquivos:
```bash
aws s3 cp <caminho-local-do-arquivo> s3://<nome-do-bucket>/<caminho-destino>
```

### Listar arquivos em um bucket:
```bash
aws s3 ls s3://<nome-do-bucket>
```

### Excluir arquivos:
```bash
aws s3 rm s3://<nome-do-bucket>/<caminho-do-arquivo>
```

---

## Configuração de Glue Crawlers

### Criar um crawler:
```bash
aws glue create-crawler \
    --name <nome-do-crawler> \
    --role <arn-da-role> \
    --database-name <nome-do-banco-de-dados> \
    --targets S3Targets=[{"Path":"s3://<caminho-dos-dados>"}]
```

### Executar um crawler:
```bash
aws glue start-crawler --name <nome-do-crawler>
```

### Verificar status do crawler:
```bash
aws glue get-crawler --name <nome-do-crawler>
```

---

## Configuração de Glue Jobs

### Criar um job:
```bash
aws glue create-job \
    --name <nome-do-job> \
    --role <arn-da-role> \
    --command "Name=glueetl,ScriptLocation=s3://<caminho-do-script>,PythonVersion=3" \
    --default-arguments "--TempDir=s3://<caminho-temp>\,--enable-continuous-cloudwatch"
```

### Iniciar um job:
```bash
aws glue start-job-run --job-name <nome-do-job>
```

### Monitorar um job:
```bash
aws glue get-job-run --job-name <nome-do-job> --run-id <id-da-execução>
```

---

## Consulta via Athena

### Executar uma consulta:
```bash
aws athena start-query-execution \
    --query-string "<sua-consulta-SQL>" \
    --query-execution-context Database=<nome-do-banco-de-dados> \
    --result-configuration OutputLocation=s3://<caminho-dos-resultados>
```

### Verificar status da consulta:
```bash
aws athena get-query-execution --query-execution-id <id-da-consulta>
```

---

## Monitoramento com CloudWatch

### Listar logs:
```bash
aws logs describe-log-groups
```

### Visualizar logs de um grupo:
```bash
aws logs get-log-events \
    --log-group-name <nome-do-log-group> \
    --log-stream-name <nome-do-log-stream>
```

---

## Limpeza de Recursos

### Excluir um bucket S3 (incluindo conteúdo):
```bash
aws s3 rb s3://<nome-do-bucket> --force
```

### Excluir um crawler:
```bash
aws glue delete-crawler --name <nome-do-crawler>
```

### Excluir um job:
```bash
aws glue delete-job --job-name <nome-do-job>
```

---

### Observações
- Certifique-se de substituir os placeholders (`< >`) pelos valores adequados.
- Sempre valide as permissões IAM antes de executar os comandos.

Para mais informações sobre os comandos, consulte a [documentação oficial do AWS CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html).
