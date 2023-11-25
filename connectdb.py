import mysql.connector

# Azure MySQL Serverの接続情報（SSL証明書を含む）
config = {
    'user': "sysadmin",  # データベースのホスト名
    'password': "Azurestudy123",  # データベースのパスワード
    'host': 'your_server_name.mysql.database.azure.com',  # データベースのホスト名
    'database': "db-azurestudy-1",  # データベース名
    'ssl_ca': './AzureMySQLServer.crt.pem'  # ローカルに保存したSSL証明書のパス
}

# MySQLに接続
conn = mysql.connector.connect(**config)

# カーソルを作成
cursor = conn.cursor()

# テーブルの作成
create_table_query = """
CREATE TABLE IF NOT EXISTS example_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT
)
"""
cursor.execute(create_table_query)
conn.commit()

# テストデータの挿入
insert_data_query = """
INSERT INTO example_table (name, age) VALUES
('Abe', 24)
"""
cursor.execute(insert_data_query)
conn.commit()

# 接続を閉じる
cursor.close()
conn.close()
