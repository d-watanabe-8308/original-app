import mysql.connector

# MySQLデータベースの接続情報を設定します
config = {
    'user': 'root',
    'password': '09025638348dw',
    'host': '43.207.111.176',
    'database': 'users',
    'raise_on_warnings': True
}

try:
    # MySQLデータベースに接続します
    cnx = mysql.connector.connect(**config)
    print("MySQLサーバーへの接続に成功しました！")

    # データベースの接続をクローズします
    cnx.close()
except mysql.connector.Error as err:
    print("MySQLサーバーへの接続に失敗しました。エラー:", err)
