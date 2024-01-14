import matplotlib.pyplot as plt

def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read().replace('\n', '')
            return data.strip()
    except FileNotFoundError:
        return "File not found."

def convert_to_string(data):

    lines = data.split('\n')
    print(lines)
    binary_string = ''.join(lines)
    return binary_string

teste = read_txt_file("seq1.txt")

numeros = []
str_check = ""

for bit in teste:
    str_check += bit

    if len(str_check) == 6:
        numero_atual = 0
        for i in range(0,6):
            numero_atual += 2**i * int(str_check[-(i+1)])
        numeros.append(numero_atual)
        str_check = ""

plt.hist(numeros, 64, rwidth=0.9)
plt.show()
# Obrigado ChatGPT