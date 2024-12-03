#Desenvolvido por: Iago Artner

# Implementação de Singleton utilizando a estratégia "thread-safe".
# O método __new__ garante que apenas uma instância da classe seja criada,
# ao verificar se a instância já existe antes de criar a mesma.

class RegistroUsuarios:
    "Padrão Singleton"
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super().__new__(cls, *args, **kwargs)
            cls._instancia._usuarios_registrados = set()
        return cls._instancia

    def registrar_usuario(self, nome_usuario):
        if nome_usuario in self._usuarios_registrados:
            return f"Usuário '{nome_usuario}' já está registrado."
        self._usuarios_registrados.add(nome_usuario)
        return f"Usuário '{nome_usuario}' registrado com sucesso!"

    def listar_usuarios_registrados(self):
        return list(self._usuarios_registrados)


def main():
    print("Seja bem-vindo ao ConectaSys!")
    registro = RegistroUsuarios()

    while True:
        print("\nOpções:")
        print("1. Registrar novo usuário")
        print("2. Listar usuários registrados")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome_usuario = input("Informe o nome do usuário: ").strip()
            if nome_usuario:
                print(registro.registrar_usuario(nome_usuario))
            else:
                print("O nome do usuário não pode estar vazio.")
        elif escolha == "2":
            usuarios = registro.listar_usuarios_registrados()
            if usuarios:
                print("Usuários registrados:", ", ".join(usuarios))
            else:
                print("Não há nenhum usuário registrado em nosso banco de dados.")
        elif escolha == "3":
            print("\nObrigado!")
            print("Desenvolvido por Iago Artner.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    main()