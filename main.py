from random import sample
import random
ale = 0
i=0
respostas_certas = 0
perguntas = [['Qual é o estado mais populoso do Brasil? (a)São Paulo   (b)Rio de Janeiro   (c)Minas Gerais   (d)Pernambuco', 'a'],
    ['Qual é o ponto mais alto da Terra? (a)Broad Peak   (b)Everest  (c)Manaslu  (d)Cho Oyu ', 'b'],
    ['O que é a Via Láctea? (a)uma marca de leite     (b)o nome de um cantor    (c)uma banda de rock     (d)uma galáxia ', 'd'],
    [' Quais desses não é considerado um planeta? (a)Plutão   (b)Saturno  (c)Júpiter   (d)Vênus ','a'],
    ['Quais destas estrelas faz parte da constelação de escorpião? (a)Alpha Piscium   (b)Ross 157  (c)Antares  (d)Sol ','c'],
    ['Qual destes países é localizado no continente norte americano? (a)França   (b)EUA   (c)Espanha   (d)Argentina ', 'b'],
    ['Quantos estados existem no Brasil? (a)27 estados mais o Distrio Federal    (b)29 estados mais o Distrito Federal   (c)26 estados mais o Distrito Federal  (d)25 estados mais o Distrito Federal ','c'],
    ['Em qual ano o homem pisou na Lua? (a)1967   (b)1975   (c)1965   (d)1969 ','d'],
    ['Qual dos animais abaixo NÃO é um mamífero?: (a)Aranha   (b)Gato   (c)Cachorro   (d)Urso ','a'],
    ['Qual das seguintes empresas tem origem coreana : (a)Sony    (b)   Microsoft   (c)Apple (d)Samsung ', 'd']
    ]
result = []


while (i < 5):
    ale = random.randint(0,9)
    if ale not in result:
        i=i+1
        result.append(ale)
        print (perguntas[ale][0])
        resposta_usuario = input('Sua resposta é a alternativa: ')
        if (perguntas[ale][1] == resposta_usuario):
            print("acertou!!!")
            respostas_certas = respostas_certas + 100
        else:
            print("errou :(")
            break
print ("Acabou o jogo, você fez essa pontuaçao:", respostas_certas)

