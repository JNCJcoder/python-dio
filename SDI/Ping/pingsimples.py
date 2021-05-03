import os

ip_ou_host = input("Digite o IP ou Host a ser verificado: \n")

print("-" * 60)
os.system('ping -n 6 {}'.format(ip_ou_host))
print("-" * 60)
