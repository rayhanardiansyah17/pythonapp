from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# Konfigurasi database MySQL
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'nyoba'
app.config['MYSQL_PORT'] = 3306

# Inisialisasi MySQL
mysql = MySQL(app)

@app.route('/')
def index():
   

    cur = mysql.connection.cursor()
    # Query untuk mengambil data dari tabel
    cur.execute("SELECT kode, nama, harga, jumlah FROM cobalagi")
    data = cur.fetchall()  # Ambil semua data
    cur.close()
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

