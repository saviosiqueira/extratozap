from glob import glob
import os
from pprint import pprint
#"import re" para importar a library de regex
import re

class Grupo:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.nome, self.numero = self.Extrair_nome_numero()
        self.alunos = '' # Aluno.Extrair_alunos()

    #Extrai o nome e número de cada grupo
    def Extrair_nome_numero(self):
        #Digitando padrão do regex para pesquisa em uma string:
        padrao_grupo = r"Conversa do WhatsApp com (\[(\d{1,})\].*)"
        #Pesquisa no resultado os dados baseados no regex, e retorna na variavel resultado
        resultado = re.search(padrao_grupo, self.arquivo, re.MULTILINE)
        
        #Atribui os dados nome e numero de acordo com os resultados pra cada variavel
        nome = resultado.group(1)
        numero = resultado.group(2)

        return nome, numero

    def Exportar_Contatos(self):
        ...
    
    def Importar_Grupos():
        caminho_conversas = 'arquivos' + os.path.sep
        return glob(caminho_conversas + '*.txt')

    def Remover_duplicados():
        ...

class aluno:
    def __init__(self, numero):
        self.numero = numero
        self.presente = True



if __name__ == '__main__':
    arquivos_grupos = Grupo.Importar_Grupos()

    arquivos_grupo = arquivos_grupos[0]
    #pprint(arquivos_grupo)

    #grupo = Grupo(arquivos_grupo)
    #print(f'Grupo: {grupo.nome} \n-Número: {grupo.numero}')

    for grupo in arquivos_grupos:
        grupo = Grupo(grupo)
        pprint(f'Grupo: {grupo.nome} - Número: {grupo.numero}')
    


