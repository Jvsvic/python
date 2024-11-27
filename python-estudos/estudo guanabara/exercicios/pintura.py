larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print(f'Sua parede tem a dimensão de {larg}x{alt}, a área entre os dois é de {area}m')
tinta = area / 2
print(f'Para pintar a parede você precisará de {tinta}L de tinta')