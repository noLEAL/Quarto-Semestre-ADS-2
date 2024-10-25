import sqlite3

class UserRegister:
    """Classe que gerencia os usuarios do sistema"""

    def __init__(self):
        """Conecta ao banco de dados (ou cria um novo se ele não existir)"""
        try:
            self.cone = sqlite3.connect('mercado.db')
            self.cu = self.cone.cursor()
            self.create_table()
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco: {e}")

    def create_table(self):
        """Cria tabela de usuarios"""
        self.cu.execute('''CREATE TABLE IF NOT EXISTS usuario (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            usuario TEXT NOT NULL,
                            senha TEXT NOT NULL,
                            priv TEXT NOT NULL)''')

    def baseuser(self):
        """Lista de produtos para inserir no banco de dados (dados padrão)"""
        try:
            usuarios = [
                ("Nome do Administrador Geral", "adm", "1234", "admin"),
                ("Nome do Funcionario", "fulado", "1234", "funci"),
                ("Nome do Filho do Dono", "adm", "1111", "funci")
            ]

            # Executa a inserção de todos os produtos
            self.cu.executemany("INSERT INTO usuario(nome, usuario, senha, priv) VALUES (?,?,?,?)", usuarios)
            self.cone.commit()

            # Mensagem de sucesso
            print("Usuriaos cadastrados com sucesso")
            #messagebox.showinfo('Sucesso', 'Produtos padrão cadastrados com sucesso')
        except sqlite3.Error as e:
            print(f"Erro ao inserir usuraio padrão: {e}")

    def search_username(self,username):
        """Busca um usuario pelo nome de usuario"""
        try:
            self.cu.execute("SELECT * FROM usuario WHERE usuario=?",(username,))
            resposta = self.cu.fetchall()
            #print(f'ID:{dados[0]} | nome:{dados[1]} | tipo:{dados[2]} | valor:{dados[3]} | estoque:{dados[4]}')
            # for i in dados:
            #     print(f'id:{i[0]} |nome:{i[1]} |usuario:{i[2]} |senha:{i[3]} |privilegio:{i[4]}')
            # print("Busca do realizada")
            return resposta

        except sqlite3.Error as e:
            print(f"Erro ao procurar produto pelo nome: {e}")

    def validar_user(self):
        """Valida se o usuario é valido ou não"""
        back_user = input(str("Digite usuario:"))
        back_pass = input(str("Digite senha:"))
        temp = self.search_username(back_user)
        for i in temp:
            print(f'usuario:{i[2]}, senha:{i[3]}, privilegio:{i[4]}\n')
            if i[2] == back_user and i[3] == back_pass and i[4] == 'adm':
                return True
            print('validando proximo')

        print("Credencial incorreta, tente novamente.")
        return False
