glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
dados = [
    (x, 
     'Hipoglicemia' if x < 70 
     else 'Normal' if 70 <= x < 100 
     else 'Alterada' if 100 <= x < 125 
     else 'Diabetes') 
    for x in glicemia
]



print(dados)