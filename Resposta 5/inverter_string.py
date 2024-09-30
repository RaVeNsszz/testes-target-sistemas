def invert_string(string):
    reversed_string = ""
    
    # Loop em ordem reversa através dos caracteres da string original
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    
    return reversed_string 

string = input("Digite uma string para inverter: ")
print("String invertida:", invert_string(string))
