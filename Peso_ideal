## Calcula o peso ideal baseado em sua altura, e o código abaixo usa sua altura e peso.

def pbaseh():
    user = input('Informe o sexo: ')
    if user == 'm':
        ah = float(input('Informe sua altura: '))
        vh = (72.7 * ah) - 58
        print(f'O peso ideal baseado na altura de um homem de {ah:.2f} altura é, {vh:.2f} KG')
    elif user == 'f':
        af = float(input('Informe sua altura: '))
        vf = (62.1 * af) - 44.7
        print(f'O peso ideal baseado na altura de uma mulher de {af:.2f} altura é, {vf:.2f} KG')
    else:
        if not 'm' or 'f':
            print('Escolha entre apenas: (m)- masculino / (f)- feminino')


pbaseh()

# O código abaixo faz praticamente a mesma coisa que o código acima, porem está mais melhorado.

def peso_ideal():
    sexo = float(input('Escolha: 1- Sexo Masculino / 2- Sexo Feminino: '))
    h = float(input('Altura: '))
    peso = float(input('Peso: '))

    pe_ideal = (72.7*h) - 58 if sexo == 1 else (62.1*h) - 44.7

    if peso < pe_ideal:
        print('Abaixo do peso ideal!')
    elif peso == pe_ideal:
        print('Dentro do peso ideal!')
    else:
        print('Acima do peso ideal!')
    print('Peso: %.2f / Peso ideal: %.2f' % (peso, pe_ideal))


peso_ideal()

## Para melhor entendmento na linha 27 onde se usa list comprehension é a mesma coisa que
if sexo == 1:
  pe_ideal = (72.7*h) - 58
  
else:
  pe_ideal = (62.1*h) - 44.7
