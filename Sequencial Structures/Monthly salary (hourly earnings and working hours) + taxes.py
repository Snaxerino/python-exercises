pagamento_hora = float(input('Indique quanto ganha por hora: '))
horas_trabalho = float(input('Indique quantas horas trabalha: '))
salario_bruto = pagamento_hora * horas_trabalho
inss = 0.08
ir = 0.11
sindicato = 0.05
salario_liquido = salario_bruto - inss - ir - sindicato

print(salario_bruto)
print(salario_liquido)