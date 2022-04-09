# /-------------------------------------------\
# | Crie um algoritmo que entre com um vetor, |
# | retornando "ORDENADO" se o vetor estiver  |
# | em ordem crescente e "DESORDENADO" caso   |
# | contrário.                                |
# \-------------------------------------------/

# Importações
import os

# Funções
def checkOrder(vector: list) -> None:
    print("ORDENADO" if vector == sorted(vector) else "DESORDENADO")

def main() -> None:  # sourcery skip: for-append-to-extend
    while True:
        # Limpar console
        os.system("cls" if os.name == "nt" else "clear")

        # Inicializar vetor vazio
        vector = []

        # Definir comprimento do vetor
        try:
            length = int(input("Select vector length\n>>> "))
        except Exception as e:
            print(f"ERROR: {e}")

        # Lê o valor a ser adicionado no vetor[i]
        for i in range(length):
            vector.append(int(input(f"POS#{i + 1} >>> ")))

        # Checar ordem do vetor
        checkOrder(vector)

        # Executar novamente?
        match input("\nExecute again? (y/n)\n>>> ").lower():
            case "y":
                continue
            case _:
                break

if __name__ == "__main__":
    main()
