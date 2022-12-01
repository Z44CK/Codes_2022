# Toda vez que traz um peso de peixe maior que o estabelecido pelo regulamento de pesca do estado de São Paulo. 
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. O programa lê a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que deverá ser pago ao exceder 50 quilos.


def peixe():
    while True:
        try:
            print('ATENÇÃO, VALOR EXCEDENTE A 50 QUILOS, SUJEITO A MULTA DE 4,00 R$ POR QUILO')
            peso = float(input('Insirá o peso do peixe:'))
            limite = 50
            if peso > limite:
                excesso = peso - limite
                multa = excesso * 4
                print(f'O peso do peixe é de: {peso:.2f}KG')
                print(f'O valor excedente do permitido foi {excesso:.2f}KG')
                print(f'O valor total da multa a pagar é de {multa:.2f}R$')

            elif peso <= limite:
                print(f'{peso:.2f}KG está dentro do limite extimado de {limite:.2f}KG,'
                      f' e está dentro do regulamento, nada a pagar!')

        except ValueError:
            print('Ops, caractere incorreto, informe apenas numeros!')

        else:
            break


peixe()
