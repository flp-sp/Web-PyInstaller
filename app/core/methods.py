import os
import shutil

def limpar_src():
    diretorio = '../app/src'

    for item in os.listdir(diretorio):
        caminho_completo = os.path.join(diretorio, item)
        if os.path.isfile(caminho_completo) or os.path.islink(caminho_completo):
            os.remove(caminho_completo)
        elif os.path.isdir(caminho_completo):
            shutil.rmtree(caminho_completo)