#Leer un archivo lÃ­nea por lÃ­nea
with open('Tale.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())

#Leer todas las lÃ­neas en una lista
with open('Tale.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

with open('Tale.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")

#Sobreescribir el texto
with open('Tale.txt', 'w') as file:
    file.write("\n\nBy:ChatGPT")