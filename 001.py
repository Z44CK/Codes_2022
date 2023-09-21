# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.


def calc_salario():
    qtd_horas = float(input('Valor ganho por hora: '))
    horas_tb = int(input('Horas trabalhadas no mês: '))
    salario_bruto = qtd_horas * horas_tb
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    print('Salario Bruto: R$ %.2f' % salario_bruto)
    print('IR: R$ %.2f' % ir)
    print('INSS: R$ %.2f' % inss)
    print('Sindicato: R$ %.2f' % sindicato)
    print('Salario Liquido: R$ %.2f' % (salario_bruto - ir - inss - sindicato))


calc_salario()
