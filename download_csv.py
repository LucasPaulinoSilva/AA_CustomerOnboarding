import configs
import httpx
import os


def baixar_arquivo_csv():
    # Caminho da pasta onde será salvo o arquivo
    caminhoPastaCSV = configs.PASTA_ARQUIVOS

    # Link URL do arquivo que será baixado
    url = configs.LINK_ARQUIVO_CSV

    # Faz a requisição GET para URL e obtém a resposta
    with httpx.Client() as client:
        response = client.get(url)

    # Verifica se a resposta foi bem-sucedida
    if response.status_code == 200:
        # Caso o arquivo exista, ele é baixado para pasta local
        with open(caminhoPastaCSV + configs.NOME_ARQUIVO, 'wb') as f:
            f.write(response.content)
        print(
            f"Arquivo: [{caminhoPastaCSV}{configs.NOME_ARQUIVO}] baixado com sucesso!")
    else:
        print(f"Erro ao obter o arquivo {configs.NOME_ARQUIVO}")


if __name__ == '__main__':
    baixar_arquivo_csv()
