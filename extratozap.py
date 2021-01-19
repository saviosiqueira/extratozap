from glob import glob
import os
from pprint import pprint
import re

class Grupo:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.nome, self.numero = self.Extrair_nome_numero()
        self.usuarios = '' # Usuarios.Extrair_usuarios()

    def Extrair_nome_numero(self):
        #Padrão do regex:
        padrao_grupo = r"Conversa do WhatsApp com (\[(\d{1,})\].*)"
        resultado = re.search(padrao_grupo, self.arquivo, re.MULTILINE)
        
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

if __name__ == '__main__':
    arquivos_grupos = Grupo.Importar_Grupos()

    arquivos_grupo = arquivos_grupos[0]
    #pprint(arquivos_grupo)

    #grupo = Grupo(arquivos_grupo)
    #print(f'Grupo: {grupo.nome} \n-Número: {grupo.numero}')

    for grupo in arquivos_grupos:
        grupo = Grupo(grupo)
        print(f'Grupo: {grupo.nome} \n-Número: {grupo.numero}')
    


