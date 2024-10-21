import sqlite3

from django.utils.text import camel_case_to_spaces


#import messagebox


class Sistemaderegistro:
    """
        Essa classe gerencia o banco de dados do mercado, fornecendo métodos para criar,
        inserir, visualizar, atualizar, buscar e deletar produtos.
    """
    def __init__(self):
        """Conecta ao banco de dados (ou cria um novo se ele não existir)"""
        try:
            self.conn = sqlite3.connect('mercado.db')
            self.c = self.conn.cursor()
            self.create_table()
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco: {e}")

    def create_table(self):

        self.c.execute('''CREATE TABLE IF NOT EXISTS produtos (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            tipo TEXT NOT NULL,
                            valor REAL NOT NULL,
                            estoque INTEGER NOT NULL)''')

    def basedate(self):
        """Lista de produtos para inserir no banco de dados (dados padrão)"""
        try:
            produtos = [
                ("Itaipava", "Cerveja", 1.50, 200),
                ("Skol", "Cerveja", 1.70, 300),
                ("Del Vale", "Suco", 2.10, 100),
                ("Pepsi Cola 2L", "Refrigerante", 3.00, 800),
                ("Guaraná Charrua 2L", "Refrigerante", 2.50, 340),
                ("Bis branco", "Chocolate", 2.70, 50)
            ]

            # Executa a inserção de todos os produtos
            self.c.executemany("INSERT INTO produtos(nome, tipo, valor, estoque) VALUES (?,?,?,?)", (produtos,))
            self.conn.commit()

            # Mensagem de sucesso
            print("Produtos padrão cadastrados com sucesso")
            #messagebox.showinfo('Sucesso', 'Produtos padrão cadastrados com sucesso')
        except sqlite3.Error as e:
            print(f"Erro ao insser produtos padrão: {e}")

    def register_product(self, nome, tipo, valor, estoque):
        """Insere um novo produto no banco de dados"""
        try:
            self.c.execute("INSERT INTO produtos(nome, tipo, valor, estoque) VALUES (?,?,?,?)",(nome, tipo, valor, estoque,))
            self.conn.commit()
            #messagebox.showinfo('deu certo porra', 'Produto cadastrado com sucesso')
            print()
            print("Produto cadastrado com sucesso")
        except sqlite3.Error as e:
            print(f"Erro ao cadastrar produto: {e}")

    def view_products(self):
        """Seleciona todos os produtos da tabela"""
        try:
            self.c.execute("SELECT * FROM produtos")
            dado = self.c.fetchall()

            for i in dado:
                print(f'Codigo:{i[0]} | Nome:{i[1]} | Tipo:{i[2]} | Valor:R${i[3]} | Estoque:{i[4]}')
        except sqlite3.Error as e:
            print(f"Erro ao visualizar produtos: {e}")

    def search_product_name(self,name_produto):
        """Buscar produtos pelo nome"""
        try:
            self.c.execute("SELECT * FROM produtos WHERE nome=?",(name_produto,))
            dados = self.c.fetchall()
            #print(f'ID:{dados[0]} | nome:{dados[1]} | tipo:{dados[2]} | valor:{dados[3]} | estoque:{dados[4]}')
            for i in dados:
                print(f'C:{i[0]} |nome:{i[1]} |tipo:{i[2]} |valor:R${i[3]} |estoque:{i[4]}')
            print("Busca realizada")
        except sqlite3.Error as e:
            print(f"Erro ao procurar produto pelo nome: {e}")

    def update_product(self, id_produto, valor, operacao):
        """Atualiza os dados de um produto pelo ID"""
        try:
            print("entrou em upp")
            match operacao:
                case 'valor':
                    print("att valor ")
                    query = "UPDATE produtos SET valor = ? WHERE id = ?"
                    self.c.execute(query, (valor, id_produto))
                    self.conn.commit()
                    #messagebox.showinfo('deu certo', 'Update realizado')
                    print("Update do valor realizado")

                case 'estoque':
                    print("att valor ")
                    query = "UPDATE produtos SET estoque = ? WHERE id = ?"
                    self.c.execute(query, (valor, id_produto))
                    self.conn.commit()
                    # messagebox.showinfo('deu certo', 'Update realizado')
                    print("Update do estoque realizado")

        except sqlite3.Error as e:
            print(f"Erro ao fazer UPDATE no banco de dados: {e}")

    def delete_product(self,id_produto):
        """Deleta um produto pelo ID"""
        try:
            self.c.execute("DELETE FROM produtos WHERE id=?", (id_produto,))
            self.conn.commit()
            #messagebox.showinfo('deu certo', 'delete realizado')
            print("Delete realizado")
        except sqlite3.Error as e:
            print(f"Erro ao Apagar dado no banco de dados {e}")

    # def search_product(self,cod_server):
    #     """Busca um produto pelo ID"""
    #     try:
    #         self.c.execute("SELECT * FROM produtos WHERE id=?", (id,))
    #         dados = self.c.fetchall()
    #         print(f'ID:{dados[0]} |nome:{dados[1]} |tipo:{dados[2]} |valor:{dados[3]} |estoque:{dados[4]}')
    #         #messagebox.showinfo('deu certo', 'Busca realizada')
    #         print("Busca realizada")
    #     except sqlite3.Error as e:
    #         print(f"Erro ao procurar produto poelo codigo: {e}")