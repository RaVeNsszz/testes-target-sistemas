def fibonacci(n):
    seq = [0, 1] #Valores iniciais
    
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    
    return seq[:n]

n = int(input("Digite o número de termos da sequência de Fibonacci: "))
print(fibonacci(n))