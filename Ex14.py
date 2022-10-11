a = float(input("Digite sua altura:"))
p = float(input("Digite seu peso:"))

imc = p/(a*a)

if imc<20:
    print(f"Abaixo do peso! Seu imc é {imc:.2f}:")
elif imc>=25:
    print(f"Acima do peso! Seu imc é {imc:.2f}")
else:
    print(f"Você está no peso ideal! Seu imc é {imc:.2f}")
