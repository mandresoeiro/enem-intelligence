# Diretório de Dados

Este diretório é usado para armazenar os microdados do ENEM.

## Como usar

1. Baixe os microdados do ENEM 2024 do site do INEP
2. Coloque o arquivo CSV neste diretório com o nome: `MICRODADOS_ENEM_2024.csv`
3. O sistema buscará automaticamente as notas dos alunos ao cadastrá-los

## Funcionalidades

- **Busca Automática**: Ao cadastrar um aluno com CPF, o sistema busca automaticamente as notas nos microdados
- **Importação em Lote**: Use o comando `python manage.py importar_microdados_enem --csv=data/MICRODADOS_ENEM_2024.csv`
- **Endpoint API**: `POST /api/enem/alunos/buscar_notas_cpf/` com body `{"cpf": "12345678901"}`

## Estrutura esperada do CSV

O arquivo deve conter as seguintes colunas:
- `NU_CPF`: CPF do participante
- `SG_UF_PROVA`: UF da prova
- `NU_NOTA_MT`: Nota de Matemática
- `NU_NOTA_LC`: Nota de Linguagens e Códigos
- `NU_NOTA_CN`: Nota de Ciências da Natureza
- `NU_NOTA_CH`: Nota de Ciências Humanas
