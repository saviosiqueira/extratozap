# extratoZap

    Projeto em Python de controle de acesso a grupos do Whatsapp

# Descrição das classes do projeto
## Cada Grupo possui:
- Arquivo
- Nome
- Numero
- Alunos

## Aluno possui:
- Numero
- Data de Entrada
- Data de Saída (?)
- Status => Presença (Saiu/Continua)

## Grupo precisa:
- Importar os grupos
- Exportas os contatos
- Extrair o nome e número
- Remover duplicatas

## aluno precisa:
- Extrair alunos
- Controlar data de entrada e saída
- Criar o Contato
- Exportar Contatos
- Remover Duplicatas
- Alterar o número

## Operações:
- Entrada e Saída do grupo
- Mudança de número

# Códigos Regex
## Regex de entrada e saída:
    ([\d/ :].*) - (\+55[\d\s-]*)( entrou| saiu| mudou para )(?:(\+55[\d\s-]*)$)?
    Resultado esperado do regex:
        Grupo 1: Horário da ação
        Grupo 2: Número do telefone
        Grupo 3: Ação realizada
        Grupo 4: (Opcional) Novo telefone

## Regex de nome dos grupos:
    Conversa do WhatsApp com (\[(\d{1,})\].*)
    Resultado esperado do regex:
        Grupo 1: Nome completo do grupo (incluindo número)
        Grupo 2: Número do grupo
