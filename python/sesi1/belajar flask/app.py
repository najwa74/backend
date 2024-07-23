from flask import Flask, render_template, redirect, request, jsonify
from service import db
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'abcen'
)


    

app = Flask(__name__)



@app.route('/', methods=['GET'],)
def index():
    def fetch_data():
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tbl_siswa")
        return cursor.fetchall()
    items = fetch_data()
    for data in items:
        no = data[0]
        nama_siswa = data[1]
        nis = data[2]
        no_hp = data[3]
  
    return render_template('index1.html', no=no , nama=nama_siswa, nis=nis, no_hp=no_hp)

@app.route('/tambah', methods=['POST'])
def tambah():
    def insert_data( nama_siswa, nis, no_hp):
        cursor = db.cursor()
        insert = cursor.execute("INSERT INTO tbl_siswa ( nama_siswa, nis, no_hp) VALUES ( %s, %s, %s)", ( nama_siswa, nis, no_hp))
        db.commit()
    redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    
    