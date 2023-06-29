class Criptografia():

    def __init__(self):
        
        self.mensagem_criptografada = ""


    def criptografar(self, mensagem, chave):
        
        self.mensagem_criptografada = ""
        for caractere in mensagem:

            if caractere.isalpha():
                ascii_inicial = ord('a') if caractere.islower() else ord('A')
                indice = (ord(caractere) - ascii_inicial + chave) % 26
                caractere_criptografado = chr(ascii_inicial + indice)
                self.mensagem_criptografada += caractere_criptografado
            else:
                self.mensagem_criptografada += caractere
                
        



    def descriptografar(self, mensagem_criptografada, chave):
        self.criptografar(mensagem_criptografada, -chave)




def criptografar_codigo():
    with open('teste1.py', 'r') as f:
        texto_pegando = f.read()

    print(texto_pegando)

    res = c.criptografar(texto_pegando, k)
    res2 = c.mensagem_criptografada
    
    with open('teste2.py', 'w') as f:
        f.write(res2)
        
        
def descriptografar_codigo():
    with open('teste2.py', 'r') as f:
        texto_pegando2 = f.read()

    print(texto_pegando2)

    res = c.descriptografar(texto_pegando2, k)
    res2 = c.mensagem_criptografada
    
    with open('teste3.py', 'w') as f:
        f.write(res2)
      
      
        

c = Criptografia()
k = int(f"{ord('l')}{ord('u')}")
print(k)

criptografar_codigo()
descriptografar_codigo()

