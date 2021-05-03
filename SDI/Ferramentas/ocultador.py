import ctypes

pasta = input("Digite o caminho da pasta a ser ocultada: ")

ATRIBUTO_OCULTAR = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, ATRIBUTO_OCULTAR)

if retorno:
    print("Arquivo foi ocultado")
else:
    print("Arquivo não foi ocultado")
