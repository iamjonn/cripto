def vigenere(data, key, mode):
    result = ''
    key_length = len(key)
    key_index = 0
    
    for c in data:
        if c.isalpha():  # Processando apenas as letras
            char = c.lower()
            key_char = key[key_index % key_length].lower()
            shift = ord(key_char) - ord('a')
            
            if mode == MODE_ENCRYPT:
                # Cifrar: deslocar para a direita
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif mode == MODE_DECRYPT:
                # Decifrar: deslocar para a esquerda
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            
            result += new_char
            key_index += 1
        else:
            # Não alterar caracteres que não são letras
            result += c
    
    return result

# Testando com a cifra de Vigenère
key = 'ch4ve'
original = 'a ligeira raposa marrom saltou sobre o cachorro cansado'
ciphered = vigenere(original, key, MODE_ENCRYPT)
print('Encriptada:', ciphered)
plain = vigenere(ciphered, key, MODE_DECRYPT)
print('Decriptada:', plain)