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
        ...

    def Exportar_Contatos(self):
        ...
    
    def Importar_Grupos():
        caminho_conversas = 'arquivos' + os.path.sep
        return glob(caminho_conversas + '*.txt')

    def Remover_duplicados():
        ...

if __name__ == '__main__':
    arquivos_grupos = Grupo.Importar_Grupos()

    arquivos_grupos = arquivos_grupos[0]
    pprint(arquivos_grupos)

