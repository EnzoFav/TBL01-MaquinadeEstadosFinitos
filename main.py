"""Enzo Favareto da Costa
Para obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a
linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  determinar  se  uma  string de
entrada  faz  parte  da  linguagem  𝐿    definida  por  𝐿 = {𝑥 | 𝑥 ∈
 {𝑎,𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏} segundo o alfabeto  Σ={𝑎,𝑏,𝑐}.
O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt)
contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de
entrada. As linhas subsequentes contém uma string por linha.  A seguir está um exemplo das linhas que
podem existir em um arquivo de testes para o programa que você irá desenvolver:
3
abbaba
abababb
bbabbaaab
Neste  exemplo  temos  3  strings  de  entrada.  O  número  de  strings em  cada  arquivo  será
representado  por  um  número  inteiro  positivo.  A  resposta  do  seu  programa  deverá  conter  uma, e
somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado
da validação conforme o formato indicado a seguir:
abbaba: não pertence.
A  saída  poderá  ser  enviada  para  um  arquivo  de  textos,  ou  para  o  terminal  padrão  e  será
composta de uma linha de saída por string de entrada. No caso do exemplo, teremos 3 linhas de saída.
Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
contendo um número diferente de strings diferentes. Os arquivos de entrada criados para os seus testes
devem estar disponíveis tanto no ambiente repl.it quanto no ambiente Github. Observe que o professor
irá  testar  seu  programa  com  os  arquivos  de  testes  que  você  criar  e  com,  no  mínimo  um  arquivo  de
testes criado pelo próprio professor."""

def Inicio():
    filename = input("Digite o nome do arquivo com extensão desejado (Ex: Teste1.txt):")
    with open(filename, 'r') as file:
        line = file.readlines()
    poss = 1
    lista = []
    NumString = int(line[0])
    pos = NumString
    while poss < NumString:
        String = line[poss].replace('\n', '')
        lista.append(String)
        poss = poss + 1

    while NumString > NumString - pos:
        posl = 0
        palavra = lista[NumString - pos - 1]
        Valido(palavra, posl)
        pos = pos - 1



def Valido(palavra, posl):
    if posl >= len(palavra):
        print("%s: Pertence" %(palavra))
    elif palavra[posl] == 'a':
        posl = posl + 1
        PrimeiroA(palavra, posl)
    elif palavra[posl] == 'b':
        posl = posl + 1
        Valido(palavra, posl)
    elif palavra[posl] == 'c':
        posl = posl + 1
        Valido(palavra, posl)
    else:
        print("%s: String possui um caracter não válido!" %(palavra))

def PrimeiroA(palavra, posl):
    if posl >= len(palavra):
        print("%s: Não pertence" %(palavra))
    elif palavra[posl] == 'a':
        posl = posl + 1
        Invalido(palavra, posl)
    elif palavra[posl] == 'b':
        posl = posl + 1
        PrimeiroB(palavra, posl)
    elif palavra[posl] == 'c':
        posl = posl + 1
        Invalido(palavra, posl)
    else:
        print("%s: String possui um caracter não válido!" %(palavra))

def PrimeiroB(palavra, posl):
    if posl >= len(palavra):
        print("%s: Não pertence" %(palavra))
    elif palavra[posl] == 'a':
        posl = posl + 1
        Invalido(palavra, posl)
    elif palavra[posl] == 'b':
        posl = posl + 1
        Valido(palavra, posl)
    elif palavra[posl] == 'c':
        posl = posl + 1
        Invalido(palavra, posl)
    else:
        print("%s: String possui um caracter não válido!" %(palavra))

def Invalido(palavra, posl):
    if posl >= len(palavra):
        print("%s: Não pertence" %(palavra))
    elif palavra[posl] == 'a':
        posl = posl + 1
        Invalido(palavra, posl)
    elif palavra[posl] == 'b':
        posl = posl + 1
        Invalido(palavra, posl)
    elif palavra[posl] == 'c':
        posl = posl + 1
        Invalido(palavra, posl)
    else:
        print("%s: String possui um caracter não válido!" %(palavra))

Inicio()