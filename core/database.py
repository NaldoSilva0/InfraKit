import sqlite3
import json

conexao = sqlite3.connect("infrakit.db")

conexao.execute("""
CREATE TABLE IF NOT EXISTS scans (
    id INTEGER PRIMARY KEY,
    scan_id INTEGER,
    alvo TEXT,
    plugin TEXT,
    status TEXT,
    resultado TEXT
)
""")

conexao.execute("""
CREATE TABLE IF NOT EXISTS scan_sessions(
    id INTEGER PRIMARY KEY,
    alvo TEXT)""")

def criar_scan(alvo):
    conexao.execute("""
    INSERT INTO scan_sessions (alvo)
    VALUES (?)
    """, (alvo,))

    conexao.commit()
    return conexao.execute("SELECT last_insert_rowid()").fetchone()[0]

def salvar_scan(scan_id, alvo, plugin, status, resultado):
    if isinstance(resultado, dict):
        resultado = json.dumps(resultado)
    conexao.execute("""
    INSERT INTO scans (scan_id ,alvo, plugin, status, resultado)
    VALUES (?, ?, ?, ?, ?)
    """, (scan_id, alvo, plugin, status, resultado))

    conexao.commit()

def listar_scans(scan_id):
    consulta = conexao.execute("""
  
    SELECT  scan_id, id, alvo, plugin, status, resultado
    FROM scans   
    WHERE scan_id = ?

""", (scan_id,))
    
    return consulta.fetchall()

def listar_sessoes():
    consulta = conexao.execute("""

    SELECT id, alvo
    FROM scan_sessions    
""")
    return consulta.fetchall()



