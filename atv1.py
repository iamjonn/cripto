# Fonte: https://medium.com/vacatronics/cifra-de-c%C3%A9sar-em-python-8d02d3bc7d42
MODE_ENCRYPT = 1
MODE_DECRYPT = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def caesar(data, key, mode):

    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data


def hackingCaesar(message):
    for key in range(26):  # Tentando chaves de 1 a 25
        decrypted_msg = caesar(message, key, MODE_DECRYPT)  # Tentando decifrar
        print(f"Chave {key}: {decrypted_msg}")
    return "Fim da tentativa de força bruta"

# Testando com a mensagem cifrada
hackingCaesar('macarronada é muito bom')
