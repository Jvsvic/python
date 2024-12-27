def calcula_pontos():
    gols_marcados = [2, 1, 3, 1, 0]
    gols_sofridos = [1, 2, 2, 1, 3]
    total_marcados = sum(gols_marcados)
    total_sofridos = sum(gols_sofridos)
    return total_marcados, total_sofridos
    
marcados, sofridos = calcula_pontos()
print(f"Total de gols marcados: {marcados}")
print(f"Total de gols sofridos: {sofridos}")    