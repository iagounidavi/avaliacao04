from typing import List

# Interface da estratégia de ordenação
class OrdenacaoEstrategia:
    def ordenar(self, dados: List[str]) -> List[str]:
        raise NotImplementedError("Esta função deve ser implementada pela subclasse.")

# Implementação da estratégia BubbleSort
class BubbleSort(OrdenacaoEstrategia):
    def ordenar(self, dados: List[str]) -> List[str]:
        """BubbleSort: Ideal para listas pequenas, pois tem alto custo em listas maiores."""
        n = len(dados)
        for i in range(n):
            for j in range(0, n-i-1):
                if dados[j] > dados[j+1]:
                    dados[j], dados[j+1] = dados[j+1], dados[j]
        return dados

# Implementação da estratégia QuickSort
class QuickSort(OrdenacaoEstrategia):
    def ordenar(self, dados: List[str]) -> List[str]:
        """QuickSort: Ótimo para listas grandes, mas menos eficiente em listas quase ordenadas."""
        if len(dados) <= 1:
            return dados
        pivot = dados[len(dados) // 2]
        menores = [x for x in dados if x < pivot]
        iguais = [x for x in dados if x == pivot]
        maiores = [x for x in dados if x > pivot]
        return self.ordenar(menores) + iguais + self.ordenar(maiores)

# Implementação da estratégia MergeSort
class MergeSort(OrdenacaoEstrategia):
    def ordenar(self, dados: List[str]) -> List[str]:
        """MergeSort: Muito eficiente e estável, ideal para listas de tamanhos variados."""
        if len(dados) <= 1:
            return dados
        meio = len(dados) // 2
        esquerda = self.ordenar(dados[:meio])
        direita = self.ordenar(dados[meio:])
        return self._merge(esquerda, direita)

    def _merge(self, esquerda: List[str], direita: List[str]) -> List[str]:
        resultado = []
        while esquerda and direita:
            if esquerda[0] <= direita[0]:
                resultado.append(esquerda.pop(0))
            else:
                resultado.append(direita.pop(0))
        resultado.extend(esquerda or direita)
        return resultado

# Contexto que utiliza diferentes estratégias
class Ordenador:
    def __init__(self, estrategia: OrdenacaoEstrategia):
        self._estrategia = estrategia

    def definir_estrategia(self, estrategia: OrdenacaoEstrategia):
        self._estrategia = estrategia

    def ordenar(self, dados: List[str]) -> List[str]:
        return self._estrategia.ordenar(dados)

def main():
    print("Bem-vindo ao InformaList de ordenação!")
    lista_usuarios = []

    while True:
        print("\nOpções:")
        print("1. Adicionar usuário à lista")
        print("2. Ordenar usando BubbleSort")
        print("3. Ordenar usando QuickSort")
        print("4. Ordenar usando MergeSort")
        print("5. Exibir lista atual de usuários")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            novo_usuario = input("Informe o nome do usuário: ").strip()
            if novo_usuario:
                lista_usuarios.append(novo_usuario)
                print(f"Usuário '{novo_usuario}' adicionado com sucesso.")
            else:
                print("O nome do usuário não pode estar vazio.")
        elif escolha == "2":
            ordenador = Ordenador(BubbleSort())
            lista_usuarios = ordenador.ordenar(lista_usuarios)
            print("\n--- BubbleSort ---")
            print("Ideal para listas pequenas, mas ineficiente para listas grandes.")
            print("Lista ordenada:", lista_usuarios)
        elif escolha == "3":
            ordenador = Ordenador(QuickSort())
            lista_usuarios = ordenador.ordenar(lista_usuarios)
            print("\n--- QuickSort ---")
            print("Eficiente para listas grandes, mas não ideal para listas quase ordenadas.")
            print("Lista ordenada:", lista_usuarios)
        elif escolha == "4":
            ordenador = Ordenador(MergeSort())
            lista_usuarios = ordenador.ordenar(lista_usuarios)
            print("\n--- MergeSort ---")
            print("Estável e eficiente, ideal para listas de tamanhos variados.")
            print("Lista ordenada:", lista_usuarios)
        elif escolha == "5":
            print("Lista atual de usuários:", lista_usuarios if lista_usuarios else "Nenhum usuário na lista.")
        elif escolha == "6":
            print("\nObrigado por usar o InformaList!")
            print("Desenvolvido por Iago Artner.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()