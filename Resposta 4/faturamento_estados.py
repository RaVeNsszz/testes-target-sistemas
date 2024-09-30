# Valores de faturamento por Estado
revenue = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_revenue = sum(revenue.values())

# Calcula a porcentagem de cada estado
percentages = {state: (value / total_revenue) * 100 for state, value in revenue.items()}

# Retorno dos resultados
print("Percentage representation of monthly revenue by state:")
for state, percentage in percentages.items():
    print(f"{state}: {percentage:.2f}%")
