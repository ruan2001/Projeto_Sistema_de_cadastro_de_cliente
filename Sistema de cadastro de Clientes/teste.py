import barcode
from barcode.writer import ImageWriter

# Função para adicionar o dígito verificador a um número de 12 dígitos para EAN-13
def gerar_codigo_ean13(numero):
    # Obtém a classe EAN-13 e adiciona o dígito verificador
    codigo_classe = barcode.get_barcode_class("ean13")
    codigo = codigo_classe(numero, writer=ImageWriter())
    return codigo

# Aplicativo de console para geração de códigos de barras
def main():
    # Solicita um número de 12 dígitos ao usuário
    numero = input("Digite um número de 12 dígitos para criar um código de barras EAN-13: ")

    # Garante que o número tem 12 dígitos
    if len(numero) != 12 or not numero.isdigit():
        print("Erro: O número deve ter 12 dígitos numéricos.")
        return

    # Gera o código de barras e salva como imagem
    codigo_barras = gerar_codigo_ean13(numero)
    arquivo = "codigo_barras_ean13.png"
    codigo_barras.save(arquivo)

    print(f"Código de barras salvo como '{arquivo}'.")

# Executa o aplicativo
if __name__ == "__main__":
    main()
