# alvo: C:\Users\Roberto\Desktop\teste.txt

from time import sleep

ListaIntens = list()
ListaQuant = list()

# Documento com as informacoes:
caminho = str(input('Caminho do arquivo: '))


def ListaProvisoria(item):
    for itens in ListaIntens:
        if itens == item:
            return True
    return False


def ListaQuantidade(list):
    quantTemp, quantFinal = '', int()

    ind = ''
    list = sorted(list)
    doc = open(caminho, 'r')
    linhasDoc = doc.readlines()

    for item in list:
        for linha in linhasDoc:
            for index in range(len(linha)):
                if linha[index] == '\n':
                    quantFinal = int(quantTemp)
                    ListaQuant.append(int(quantTemp))
                    ind = ''
                else:
                    ind = ind + str(linha[index])
                    # sleep(1)
                    if item in ind:
                        if linha[index].isnumeric():
                            quantTemp = quantTemp + linha[index]
                            print(quantTemp)
    print(ListaQuant)


def FiltraLinha():
    ind = ''

    # Documento novo com Lista Final
    # ListaFinal = open('C:\\Users\\Roberto\\Desktop\\ListaFiltrada.txt', 'w')
    doc = open(caminho, 'r')
    linhasDoc = doc.readlines()
    for linha in linhasDoc:
        for index in range(len(linha)):
            if linha[index] != '\x09':
                ind = ind + str(linha[index])
            else:
                break
        if not ListaProvisoria(ind):
            ListaIntens.append(ind)

        ind = ''
    doc.close()
    ListaQuantidade(ListaIntens)


if __name__ == '__main__':
    FiltraLinha()
