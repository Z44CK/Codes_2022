# """
# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# Não é necessário, más usando o .upper() antes do input
# Tanto faz digitar minusculas ou maiusculas, o codigo irá funcionar.
# """

def sex():
    sexo = str.upper((input('Escolha: M- Masculino / F- Feminino:')))
    if sexo == 'M':
        print('M-Masculino')
    elif sexo == 'F':
        print('F-Feminino')
    else:
        print('Sexo invalido')


sex()
