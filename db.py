import sqlite3

def conectar_banco():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    return conn, cursor

def criar_tabelas():
    conn, cursor = conectar_banco()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            meta TEXT NOT NULL,
            concluida INTEGER DEFAULT 0
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS desabafos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT NOT NULL,
            data TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cartas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            carta TEXT NOT NULL,
            data TEXT
        )
    """)
    conn.commit()
    conn.close()

def adicionar(tabela, dados):
    conn, cursor = conectar_banco()
    placeholders = ",".join("?" for _ in dados)
    cursor.execute(f"INSERT INTO {tabela} VALUES (NULL, {placeholders})", dados)
    conn.commit()
    conn.close()

def deletar(tabela, id):
    conn, cursor = conectar_banco()
    cursor.execute(f"DELETE FROM {tabela} WHERE id=?", (id,))
    conn.commit()
    conn.close()

def atualizar(tabela, coluna, valor, id):
    conn, cursor = conectar_banco()
    cursor.execute(f"UPDATE {tabela} SET {coluna}=? WHERE id=?", (valor, id))
    conn.commit()
    conn.close()

def buscar_por_id(tabela, id):
    conn, cursor = conectar_banco()
    cursor.execute(f"SELECT * FROM {tabela} WHERE id=?", (id,))
    item = cursor.fetchone()
    conn.close()
    return item