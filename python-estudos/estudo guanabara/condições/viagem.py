v = float(input('Qual será a distância em KM? '))
r = (v * 0.50)
if v <= 200:
    print(f'O valor será: {r}')
else:
    des = (v * 0.45)
    print(f'O valor com desconto será: {des}')