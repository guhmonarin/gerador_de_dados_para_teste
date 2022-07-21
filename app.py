
from random import choice


def gerarArquivo():    
    arquivo = open('dados.txt', 'a')
    for i in resultado:
        arquivo.write(f'{i}')
        arquivo.write('\n')
    arquivo.close()
    
def gerarNome():
    nome_aleatorio = choice(nome)
    resultado.append(nome_aleatorio)

def gerarEmail():
    email_aleatorio = choice(email)
    resultado.append(email_aleatorio)

def gerarTelefone():
    telefone_aleatorio = choice(telefone)
    resultado.append(telefone_aleatorio)

def gerarCidade():
    cidade_aleatorio = choice(cidade)
    resultado.append(cidade_aleatorio)

def gerarEstado():
    estado_aleatorio = choice(estado)
    resultado.append(estado_aleatorio)

def limparArquivos():
    resultado.clear()

nome = ['Gustavo', 'Marilisa', 'Lucas', 'Melissa', 'Elaine']
email = ['gustao@gmail.com','melissa@gmail.com', 'marilisa@gmail.com', 'lucas@gmail.com']
telefone = ['99874-7845', '99685-7489', '99687-4852', '99682-1234', '99678-8901']
cidade = ['Osvaldo Cruz','São Paulo', 'Presidente-prudente', 'Adamantina', 'Lucelia']
estado = ['SP', 'RJ', 'PR', 'SC', 'GO']

escolha = []
resultado = []

while True:
    try:
        print('Bem-vindo ao gerador de dados (TESTE) - Para sair do programa, digite "parar"')
        print('-'*120)
        print('Escolha uma opção ou mais para ser gerado dados aleatório!')
        print('[1] - Nome')
        print('[2] - E-mail')
        print('[3] - Tefone')
        print('[4] - Cidade')
        print('[5] - Estado')

        escolha = input('Escolha uma(as) das opções: ').lower()
        print('-'*120)

        if 'parar' in escolha:
            break

        if '1' in escolha:
            gerarNome()

        if '2' in escolha:
            gerarEmail()

        if '3' in escolha:
            gerarTelefone()

        if '4' in escolha:
            gerarCidade()

        if '5' in escolha:
            gerarEstado()

        
        gerar = input('Deseja gerar os dados em um arquivo de texto?(s/n): ').lower()

        for i in resultado:
            print(f'{i}')
        
        print('-'*120)

        if gerar == 's':
            gerarArquivo()
    


    except:
        print('Escolha uma opção válida!')



    limparArquivos()




