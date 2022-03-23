import random
import string

tamanho = 16 #Define o tamanho da senha

chars = string.ascii_letters + string.ascii_letters + '!@#$%¨&*()/*-+.' #Define letras em geral, números e caracteres especiais

rnd = random.SystemRandom() #os.urandom biblioteca os

print(''.join(rnd.choice(chars) for i in range(tamanho)))
