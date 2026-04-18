# 1. Básico

for num in range(0,101):
    print(num)

# 2. Múltiples de 2

for num_par in range(2,501,2):
    print(num_par)

# 3. Contando Vanilla Ice

for v_ice in range(0,101):
    resultante= v_ice
    if v_ice % 5 == 0:
        resultante= "ice ice"
    if v_ice % 10 == 0:
        resultante= "baby"
    print(resultante)

# 4. Wow. Número gigante a la vista

suma = []
for par in range(0,500001,2):
    suma.append(par)

print(f" el numero es: {sum(suma)}")

# 5. Regrésame al 3

for rever in range(2024,0,-3):
    print(rever)

# 6. Contador dinámico

numInicial= 0
numFinal = 30
multiplo = 3

for cont_dina in range(numInicial,numFinal+1,multiplo):
    print(cont_dina)