from enum import Enum
from glob import glob
import os
from pprint import pprint
#"import re" para importar a library de regex
import re

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
        ...
    
    def importar_grupos():
        caminho_conversas = 'arquivos' + os.path.sep
        return glob(caminho_conversas + '*.txt')
    
    def remover_duplicados(grupos):
        ...

class Operacao(Enum):
    ENTRADA = 1
    SAIDA = 2
    MUDANCA = 3

class Aluno:
    def __init__(self, numero):
        self.numero = numero
        self.presente = True

    def extrair_alunos(arquivo):
        padrao_aluno = r"([\d/ :]*) - (\+55[\d\s-]*)( entrou| saiu| mudou para )(\+55[\d\s-]*$)?"
        lista_alunos = []

        with open(arquivo, encoding='UTF-8') as arq:
            conversa = arq.readlines()
        
        for linha in conversa:
            resultado = re.search(padrao_aluno, linha, re.MULTILINE)

            if resultado != None:
                horario = resultado.group(1)
                numero = resultado.group(2)
                operacao = resultado.group(3)
                novo_numero = resultado.group(4)

                #Print de teste para ver se os dados foram pegos corretamente
                print("||", horario, '-', numero, operacao, (novo_numero if novo_numero is not None else ' '))

                if novo_numero is not None:
                    for aluno in lista_alunos:
                        if aluno.numero == numero:
                            aluno.alterar_numero(novo_numero)                
                elif 'entrou' in operacao:
                    aluno = Aluno.criar_aluno(numero)
                    aluno.entrada_saida(Operacao.ENTRADA, horario)
                    lista_alunos.append(aluno)
                else:
                    for aluno in lista_alunos:
                        if aluno.numero == numero:
                            aluno.entrada_saida(Operacao.SAIDA, horario)





    def alterar_numero(self, novo_numero):
        self.numero = novo_numero
    
    def criar_aluno(numero):
        return Aluno(numero)

    def entrada_saida(self, operacao, horario):
        if operacao == Operacao.ENTRADA:
            self.data_entrada = horario
        else:
            self.data_saida = horario

    def remover_duplicados(lista_alunos):
        ...
    def exportar_contatos(arquivo, lista_alunos):
        ...
        


if __name__ == '__main__':
    arquivos_grupos = Grupo.importar_grupos()

    arquivos_grupo = arquivos_grupos[0]
    #pprint(arquivos_grupo)

    #grupo = Grupo(arquivos_grupo)
    #print(f'Grupo: {grupo.nome} \n-Número: {grupo.numero}')

    for grupo in arquivos_grupos:
        grupo = Grupo(grupo)
        pprint(f'Grupo: {grupo.nome} - Número: {grupo.numero}')
    
