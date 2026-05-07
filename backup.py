import sqlite3
import datetime

def realizar_backup(db_origem):

    data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_backup = f"backup_sistema_{data_atual}.db"

    try:
        conn_origem = sqlite3.connect(db_origem)
        conn_destino = sqlite3.connect(nome_backup)

        with conn_destino:
            conn_origem.backup(conn_destino)

        print(f"Backup criado: {nome_backup}")

    except sqlite3.Error as e:
        print(f"Erro: {e}")

    finally:
        conn_origem.close()
        conn_destino.close()

realizar_backup("banco.db")