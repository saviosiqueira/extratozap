from enum import Enum
from glob import glob
import os
from pprint import pprint
#"import re" para importar a library de regex
import re
#toolz unique usado para retornar a lista de alunos sem nenhuma duplicata de forma simples
from toolz import unique
import csv

class Grupo:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.nome, self.numero = self.extrair_nome_numero()
        self.alunos = Aluno.extrair_alunos(self.arquivo)

    #Extrai o nome e número de cada grupo
    def extrair_nome_numero(self):
        #Digitando padrão do regex de pesquisa de grupos em uma string:
        padrao_grupo = r"Conversa do WhatsApp com (\[(\d{1,})\].*)"
        #Pesquisa no resultado os dados baseados no regex, e retorna na variavel resultado
        resultado = re.search(padrao_grupo, self.arquivo, re.MULTILINE)
        
        #Atribui os dados nome e numero de acordo com os resultados pra cada variavel
        nome = resultado.group(1)
        numero = resultado.group(2)

        return nome, numero

    def exportar_contatos(self):
        Aluno.exportar_contatos(f'Alunos do grupo {self.numero}', self.alunos)
    
    def importar_grupos():
        caminho_conversas = 'arquivos' + os.path.sep
        return glob(caminho_conversas + '*.txt')
    
    def remover_duplicados(self):
        self.alunos = Aluno.remover_duplicados(self.alunos)

class Operacao(Enum):
    ENTRADA = 1
    SAIDA = 2
    MUDANCA = 3

class Aluno:
    def __init__(self, numero):
        self.numero = numero
        self.presente = True

    def extrair_alunos(arquivo):
        padrao_aluno = r"([\d/ :].*) - (\+55[\d\s-]*)( entrou| saiu| mudou para )(?:(\+55[\d\s-]*)$)?"
        lista_alunos = []

        with open(arquivo, encoding='UTF-8') as arq:
            conversa = arq.readlines()
        
        for linha in conversa:
            resultado = re.search(padrao_aluno, linha)

            if resultado != None:
                horario = resultado.group(1)
                numero = resultado.group(2).replace("\xa0", ' ') #O replace \xa0 serve pra remover o Non-Breaking Space da string numero
                operacao = resultado.group(3)
                novo_numero = resultado.group(4)

                #Faz o replace do nbsp e retira caracteres no final do numero caso a string não seja vazia
                if novo_numero is not None: 
                    novo_numero = novo_numero.replace("\xa0", ' ').rstrip()

                #Print de teste para ver se os dados foram pegos corretamente
                #print("||", horario, '---', numero, '---', operacao, (novo_numero if novo_numero is not None else ' '))

                if novo_numero is not None:
                    for aluno in lista_alunos:
                        if aluno.numero == numero:
                            aluno.alterar_numero(novo_numero)                
                            break
                elif 'entrou' in operacao:
                    aluno = Aluno.criar_aluno(numero)
                    aluno.entrada_saida(Operacao.ENTRADA, horario)
                    lista_alunos.append(aluno)
                else:
                    for aluno in lista_alunos:
                        if aluno.numero == numero:
                            aluno.entrada_saida(Operacao.SAIDA, horario)
                            break
                
        return lista_alunos

    def alterar_numero(self, novo_numero):
        self.numero = novo_numero
    
    def criar_aluno(numero):
        return Aluno(numero)

    def entrada_saida(self, operacao, horario):
        if operacao == Operacao.ENTRADA:
            self.data_entrada = horario
        else:
            self.data_saida = horario
            self.presente = False

    def remover_duplicados(lista_alunos):
        return list(unique(lista_alunos, key=lambda aluno: aluno.numero))

    def exportar_contatos(nome_arquivo, lista_alunos):
        if not os.path.isdir('contatos'):
            os.mkdir('contatos')
        
        separador = os.path.sep
        caminho_arquivo = os.path.join('contatos' + separador, f'{nome_arquivo}.csv')

        with open(caminho_arquivo, 'w', newline='', encoding='UTF-8') as arq:
            writer = csv.writer(arq)
            writer.writerow(['Número do Aluno', 'Status', 'Data de Entrada', 'Data de Saída'])
            for aluno in lista_alunos:
                if aluno.presente:
                    writer.writerow([aluno.numero, 'Continua no grupo', aluno.data_entrada])
                else:
                    writer.writerow([aluno.numero, 'Saiu do grupo', aluno.data_entrada, aluno.data_saida])
        print(f'CSV \'{nome_arquivo}\' gerado na pasta \'{caminho_arquivo}\'')
        


if __name__ == '__main__':
    arquivos_grupos = Grupo.importar_grupos()
    todos_alunos = []
    for grupo in arquivos_grupos:
        grupo = Grupo(grupo)

        for aluno in grupo.alunos:
            todos_alunos.append(aluno)

        grupo.remover_duplicados()
        grupo.exportar_contatos()

        print(f'{len(grupo.alunos)} alunos foram exportados do grupo {grupo.numero}')

    todos_alunos = Aluno.remover_duplicados(todos_alunos)
    Aluno.exportar_contatos('Lista todos alunos', todos_alunos)

    print('Todos os grupos exportados')
    print(f'Total de Alunos exportados:', len(todos_alunos))
    