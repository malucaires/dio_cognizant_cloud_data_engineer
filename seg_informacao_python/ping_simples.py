#os integra os programas e recursos do Sistema Operacional
import os

print('#' * 60)
ip_ou_host = input('Digite o ip ou host a ser verificado: ')
print('-' * 60)
os.system(f'ping -n 6 {ip_ou_host}')
print('-' * 60)
