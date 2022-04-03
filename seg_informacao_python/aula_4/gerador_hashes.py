import hashlib

string = input('Digite o texto a ser gerado o hash: ')

while True:
    menu = int(input(''' --- MENU - ESCOLHA DO TIPO DE HASH ---
1 - MD5
2 - SHA1
3 - SHA256
4 - SHA512
Digite o número do hash a ser gerado: '''))

    if menu == 1:
        resultado = hashlib.md5(string.encode('utf-8'))
        hash = 'MD5'

    elif menu == 2:
        resultado = hashlib.sha1(string.encode('utf-8'))
        hash = 'SHA1'

    elif menu == 3:
        resultado = hashlib.sha256(string.encode('utf-8'))
        hash = 'SHA256'

    elif menu == 4:
        resultado = hashlib.sha512(string.encode('utf-8'))
        hash = 'SHA512'

    else:
        print('Opção incorreta. Tente novamente.')
        continue

    print(f'O hash {hash} da string é {resultado.hexdigest()}')
    break