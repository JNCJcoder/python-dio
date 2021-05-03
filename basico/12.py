import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    dados_cep = response.json()
    
    return dados_cep

if __name__ == '__main__':
    retorna_dados_cep('22041001')
