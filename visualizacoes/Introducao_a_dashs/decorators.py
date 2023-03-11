# definir variaveis como funcoes
def soma_um(numero):
    return numero+1
f1 = soma_um
f1(1)

# definindo funcoes dentro de funcoes
def soma_um(num):
    def ad_um(num2):
        return num2 + 1
    return ad_um(num)
soma_um(4)

def soma_um(numero):
    return numero+1

#funcoes como arg
def function_call(function):
    numero_to_add = 5
    return function(numero_to_add)
function_call(soma_um)

def funcao_ola():
    def diga_oi():
        return "hi"
    return diga_oi
hello = funcao_ola()
hello()

def decorador_maiusculo(function):
    def wrapper():
        func = function()
        cria_maiusculo = func.upper() #modificador de funcoes
        return cria_maiusculo
    return wrapper

def diga_oi():
    return 'hello there'

funcao_decorada = decorador_maiusculo(diga_oi)
funcao_decorada()

@decorador_maiusculo
def diga_oi_decorado():
    return 'hello there'
diga_oi_decorado()

