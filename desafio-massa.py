import random
perguntas = {
        1 : {
        'pergunta' : 'Qual é o estado mais populoso do Brasil?' ,
        'respostas' : {  'a' : ' São Paulo ' , 'b' : ' Rio de Janeiro ' , 'c' : ' Minas Gerais ' , 'd' : ' Pernambuco ' , } ,
        'resposta_certa' : 'a' ,
        },
        2 : {
        'pergunta' : ' Qual é o ponto mais alto da Terra? ' ,
        'respostas' : { 'a' : ' Broad Peak ' , 'b' : ' Everest ' , 'c' : ' Manaslu ' , 'd' : ' Cho Oyu ' , } ,
        'resposta_certa' : 'b' ,
        },
        3 : {
        'pergunta' : ' O que é a Via Láctea? ' ,
        'respostas' : { 'a' : ' uma marca de leite ' , 'b' : ' o nome de um cantor' , 'c' : ' uma banda de rock ' , 'd' : ' uma galáxia ' , } ,
        'resposta_certa' : 'd' ,
        },
        4 : {
        'pergunta' : ' Quais desses não é considerado um planeta? ' ,
        'respostas' : { 'a' : ' Plutão ' , 'b' : ' Saturno ' , 'c' : ' Júpiter ' , 'd' : ' Vênus ' , } ,
        'resposta_certa' : 'a' ,
        },
        5 : {
        'pergunta' : ' Quais destas estrelas faz parte da constelação de escorpião? ' ,
        'respostas' : { 'a' : '  Alpha Piscium ' , 'b' : ' Ross 157 ' , 'c' : ' Antares ' , 'd' : ' Sol ' , } ,
        'resposta_certa' : 'c' ,
        },
        6 : {
        'pergunta' : ' Qual destes países é localizado no continente norte americano? ' ,
        'respostas' : { 'a' : ' França ' , 'b' : ' EUA ' , 'c' : ' Espanha ' , 'd' : ' Argentina ' , } ,
        'resposta_certa' : 'b' ,
        },
        7 : {
        'pergunta' : ' Quantos estados existem no Brasil? ' ,
        'respostas' : { 'a' : ' 27 estados mais o Distrio Federal ' , 'b' : ' 29 estados mais o Distrito Federal  ' , 'c' : ' 26 estados mais o Distrito Federal ' , 'd' : ' 25 estados mais o Distrito Federal ' , } ,
        'resposta_certa' : 'c' ,
        },
        8 : {
        'pergunta' : ' Em qual ano o homem pisou na Lua? ' ,
        'respostas' : { 'a' : ' 1967 ' , 'b' : ' 1975 ' , 'c' : ' 1965 ' , 'd' : ' 1969 ' , } ,
        'resposta_certa' : 'd' ,
        },
        9 : {
        'pergunta' : ' Qual dos animais abaixo NÃO é um mamífero : ' ,
        'respostas' : { 'a' : ' Aranha ' , 'b' : ' Gato ' , 'c' : ' Cachorro ' , 'd' : ' Urso ' , } ,
        'resposta_certa' : 'a' ,
        },
        10 : {
        'pergunta' : ' Qual das seguintes empresas tem origem coreana : ' ,
        'respostas' : { 'a' : ' Sony ' , 'b' : ' Microsoft ' , 'c' : ' Apple  ' , 'd' : ' Samsung ' , } ,
        'resposta_certa' : 'd' ,
        },
    }
print()
coisa = random.choice(list(perguntas.items()))

respostas_certas = 0
for pk, coisa in perguntas.items() :
    coisa = random.choice(list(perguntas.keys()))
    print (coisa)
    print()
    for rk, rv in coisa['respostas'].items() :
        print(f'[{rk}]: {rv}') 
    resposta_usuario = input('Sua resposta é a alternativa: ')
    if resposta_usuario == coisa['resposta_certa'] :
        print('Certa a resposta!')
        respostas_certas += 100
    else:
        print('Resposta errada!')
 
    print()
    
print(f'Você fez {respostas_certas} pontos.')
