def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def inicio(escolha):
    return escolha
while True:
    try:
      print(f'Escolha o seu tipo de calculadora')
      print(f'Soma [1]')
      print(f'Subtração [2]')
      print(f'Multiplicação [3]')
      escolha = int(input('Digite a sua escolha ou (digite -1 para sair):'))
      if escolha == -1:
          break
      num1 = float(input('Digite o seu primeiro número:'))
      num2 = float(input('Digite o seu segundo numero:'))
      if escolha == 1:
        print(soma(num1, num2))
      elif escolha == 2:
        print(subtracao(num1, num2))
      elif escolha == 3:
        print(multiplicacao(num1, num2))
      else :
        print(f'Erro de dados, digite apenas números e use "." ao invés de ","')
    except:
        print(f'Erro de dados, digite apenas números e use "." ao invés de ","')    