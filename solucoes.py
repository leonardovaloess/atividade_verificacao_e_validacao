def sao_anagramas(string1, string2):
    s1 = string1.replace(" ", "").lower()
    s2 = string2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)

def cifra_de_cesar(texto, deslocamento):
    
    resultado = ""
    
    for char in texto:
        if char.isalpha():
            # Determina se é maiúscula ou minúscula
            if char.isupper():
                # Para maiúsculas (A-Z)
                novo_char = chr((ord(char) - ord('A') + deslocamento) % 26 + ord('A'))
            else:
                # Para minúsculas (a-z)
                novo_char = chr((ord(char) - ord('a') + deslocamento) % 26 + ord('a'))
            resultado += novo_char
        else:
            # Mantém caracteres que não são letras
            resultado += char
    
    return resultado


def valida_cpf(cpf_string):
    # TODO: Implementar a lógica
    pass
