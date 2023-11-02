import download_csv
import lancamento_dados

# Baixa arquivo CSV do site do desafio
download_csv.baixar_arquivo_csv()

# Realiza o preenchimento dos dados no site com base nos dados obtidos no arquivo CSV
lancamento_dados.preencher_formulario_web()
