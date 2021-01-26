import json


def empilhaObjeto(logs):
    lista = []
    for x in range(0, 100000):
        linha = (logs.readline())
        lista.append(linha)

    return lista


arquivoTXT = open('../Dados/logs.txt', 'r')
objetosEmpilhados = empilhaObjeto(arquivoTXT)


def transformandoEmDict(objEmpilhado, posicaoObj=0):
    transfEmDict = json.loads(objEmpilhado[posicaoObj])
    return transfEmDict
