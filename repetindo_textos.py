#Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

info = input("Digite o texto:")
numero = int( input("Digite os número de repetições"))
separador = " "
texto_repetido_com_separador = ""

for i in range(numero):
    if i > 0:
        texto_repetido_com_separador += separador
    
    texto_repetido_com_separador += info

print(texto_repetido_com_separador)