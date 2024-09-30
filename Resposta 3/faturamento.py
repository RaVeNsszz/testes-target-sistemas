import json

def readDataFile(filename): # Lê o arquivo JSON
    with open(filename, 'r') as file:
        return json.load(file)


def filterData(data): # Remove valores indesejados dos registros.
    # Itera sobre a lista de forma reversa para evitar problemas ao remover elementos
    for i in range(len(data) - 1, -1, -1):
        value = data[i].get("valor")  # Usa get() para evitar KeyError se "valor" não existir
        
        # Remove a chave se o valor não for numérico ou for igual a 0
        if not isinstance(value, (int, float)) or value == 0:
            del data[i]

    return data


def min_revenue(data): # Retorna o menor valor de faturamento ocorrido
    revenues = [entry["valor"] for entry in data]
    return min(revenues) if revenues else None


def max_revenue(data): # Retorna o maior valor de faturamento ocorrido
    revenues = [entry["valor"] for entry in data]
    return max(revenues) if revenues else None


def avg_revenue(data): # Retorna o valor médio de faturamento ocorrido
    revenues = [entry["valor"] for entry in data]
    if revenues:
        total_revenue = sum(revenues)
        count = len(revenues)
        return total_revenue / count
    return 0


def days_above_average(data): # Número de dias no em que o valor de faturamento foi superior à média
    count = 0
    average = avg_revenue(data)
    for entry in data:
        if entry["valor"] > average:  # Verifica se o valor está acima da média
            count += 1
    return count


# Carregamento e Filtragem dos Dados
data = readDataFile('dados.json')
filterData(data)

#Execução dos Cálculos de Faturamento
print(f"Menor valor de faturamento: {min_revenue(data)}")
print(f"Maior valor de faturamento: {max_revenue(data)}")
# print(f"Média de valor de faturamento: {avg_revenue(data)}")
print(f"Número de dias em que o valor de faturamento foi superior à média: {days_above_average(data)}")
