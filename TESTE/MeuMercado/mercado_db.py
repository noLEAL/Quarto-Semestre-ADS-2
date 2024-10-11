import sqlite3
import messagebox


class Sistemaderegistro:
    """
        Essa classe gerencia o banco de dados do mercado, fornecendo métodos para criar,
        inserir, visualizar, atualizar, buscar e deletar produtos.
    """
    def __init__(self):
        """Conecta ao banco de dados (ou cria um novo se ele não existir)"""
        self.conn = sqlite3.connect('mercado.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS produtos (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            tipo TEXT NOT NULL,
                            valor REAL NOT NULL,
                            estoque INTEGER NOT NULL)''')

    def basedate(self):
        """Lista de produtos para inserir no banco de dados (dados padrão)"""
        produtos = [
            ("Itaipava", "Cerveja", 1.50, 200),
            ("Skol", "Cerveja", 1.70, 300),
            ("Del Vale", "Suco", 2.10, 100),
            ("Pepsi Cola 2L", "Refrigerante", 3.00, 800),
            ("Guaraná Charrua 2L", "Refrigerante", 2.50, 340),
            ("Bis branco", "Chocolate", 2.70, 50)
        ]

        # Executa a inserção de todos os produtos
        self.c.executemany("INSERT INTO produtos(nome, tipo, valor, estoque) VALUES (?,?,?,?)", produtos)
        self.conn.commit()

        # Mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Produtos padrão cadastrados com sucesso')

    def register_product(self, produto):
        """Insere um novo produto no banco de dados"""
        self.c.execute("INSERT INTO produtos(nome, tipo, valor, estoque) VALUES (?,?,?,?)",produto)
        self.conn.commit()
        messagebox.showinfo('deu certo porra', 'Produto cadastrado com sucesso')

    def view_products(self):
        """Seleciona todos os produtos da tabela"""
        self.c.execute("SELECT * FROM produtos")
        dado = self.c.fetchall()

        for i in dado:
            print(f'ID:{i[0]} |nome:{i[0]} |tipo:{i[0]} |valor:{i[0]} |estoque:{i[0]}')

    def search_product(self):
        """Busca um produto pelo ID"""
        self.c.execute("SELECT * FROM produtos WHERE id=?", (id,))
        dados = self.c.fetchall()
        print(f'ID:{dados[0]} |nome:{dados[0]} |tipo:{dados[0]} |valor:{dados[0]} |estoque:{dados[0]}')
        messagebox.showinfo('deu certo', 'Busca realizada')

    def update_product(self, produto):
        """Atualiza os dados de um produto pelo ID"""
        query = "UPDATE produtos SET nome = ?, tipo = ?, valor = ?, estoque = ? WHERE id = ?"
        self.c.execute(query, produto)
        self.conn.commit()
        messagebox.showinfo('deu certo', 'Update realizado')

    def delete_product(self,id_produto):
        """Deleta um produto pelo ID"""
        self.c.execute("DELETE FROM produtos WHERE id=?", (id_produto,))
        self.conn.commit()
        messagebox.showinfo('deu certo', 'delete realizado')

