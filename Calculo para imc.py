def calcular_imc(peso, altura):
    return peso / (altura ** 2)
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso Normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"
while True:
     try:
        peso = float(input("Digite seu peso em kg (ou -1 para sair): "))
        if peso == -1:
            break
        altura = float(input("Digite sua altura em metros: "))
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        print(f"Seu IMC é: {imc:.2f} - Classificação: {classificacao}")
     except ValueError:
        print("Por favor, digite valores válidos apenas números inteiros e ponto ao invés de vírgula.")
        
        
        
        
        
        