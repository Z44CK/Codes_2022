# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00
        
def calculo_folha_pag():
    valor_hora = float(input('Informe o valor ganho por horas trabalhadas: '))
    qtd_hora = float(input('Informe o total de horas trabalhadas esse mês: '))

    salario_bruto = valor_hora * qtd_hora

    if salario_bruto <= 900:
        desconto_ir = 0.0
    elif salario_bruto <= 1500:
        desconto_ir = 5
    elif salario_bruto <= 2500:
        desconto_ir = 10
    else:
        desconto_ir = 20

    ir = salario_bruto * (desconto_ir / 100)
    inss = salario_bruto * (10 / 100)
    fgts = salario_bruto * (11 / 100)
    total_desconto = ir + inss
    salario_liquido = salario_bruto - total_desconto

    print(f'\nSalário Bruto: R$ {salario_bruto:.2f}',
          f'\nIR (5%): R$ {desconto_ir:.2f}',
          f'\nINSS (10%): R$ {inss:.2f}',
          f'\nFGTS (11%): R$ {fgts:.2f}',
          f'\nTotal descontos: R$ {total_desconto:.2f}',
          f'\nSalário liquido: R$ {salario_liquido:.2f}',
          )


calculo_folha_pag()
