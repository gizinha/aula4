"""
def retornar_meu_nome():
    nome = input('Digite seu nome: ')
    print('Seu nome é: ',nome)
    return nome

retornar_meu_nome()
"""
#OU
"""
def retornar_nome(nome,sobrenome):
    resposta= 'Seu nome é: ' + nome + ' ' + sobrenome
    return resposta

resultado = retornar_nome('Giovanna','Melloni')
print(resultado)
"""

def somar(a,b):
    som = a + b
    if som >= 40:
        return som
    else:
        frase = 'Ops, só retorno valores acima de 40!'
        return frase

a=int(input('Insira o primeiro valor: '))
b=int(input('Insira o segundo valor: '))
result = somar(a,b)
print(result)