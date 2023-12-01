# Calculadora com interface no console
from calc import soma
# Apresentação
print('\n\t\t\t -- Calculadora --\n')

# Entrada
n1 = int(input('Informe n1: '))
n2 = int(input('Informe n2: '))

# Processamento
total = soma(2, 2)

# Saída
print(f'{n1} + {n2} = {total}')

