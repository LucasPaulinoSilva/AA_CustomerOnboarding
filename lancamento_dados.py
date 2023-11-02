from playwright.sync_api import sync_playwright
import configs
import pandas as pd


def preencher_formulario_web():
    # Concatena caminho do arquivo de CSV
    arquivoCSV = configs.PASTA_ARQUIVOS + configs.NOME_ARQUIVO

    with sync_playwright() as p:
        # Abre navegador no site do desafio
        navegador = p.chromium.launch(headless=False)
        pagina = navegador.new_page()
        pagina.goto(configs.LINK_DESAFIO)

        # Lê arquivo CSV
        tabela = pd.read_csv(arquivoCSV, sep=",")

        # Realiza o loop pelas linhas e colunas do CSV
        for coluna, linha in tabela.iterrows():

            # Preenche campos do site com as informações provenientes do CSV
            pagina.fill('[id="customerName"]', linha["Company Name"])
            pagina.fill('[id="customerID"]', linha["Customer ID"])
            pagina.fill('[id="primaryContact"]', linha["Primary Contact"])
            pagina.fill('[id="street"]', linha["Street Address"])
            pagina.fill('[id="city"]', linha["City"])
            pagina.select_option('[id="state"]', linha["State"])
            pagina.fill('[id="zip"]', str(linha["Zip"]))
            pagina.fill('[id="email"]', linha["Email Address"])
            if linha["Offers Discounts"] == "YES":
                pagina.locator('[id="activeDiscountYes"]').click()
            else:
                pagina.locator('[id="activeDiscountNo"]').click()
            if linha["Non-Disclosure On File"] == "YES":
                pagina.locator('[id="NDA"]').click()

            # Realiza o clique no botão de "Submit"
            pagina.locator('[id="submit_button"]').click()

        input("STOP para poder ver o resultado. Pressione qualquer tecla para finalizar.")


if __name__ == '__main__':
    preencher_formulario_web()
