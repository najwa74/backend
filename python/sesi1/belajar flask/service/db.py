import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'abcen'
)

def insert_data(id, nama_siswa, nis, no_hp):
    cursor = db.cursor()
    insert = cursor.execute("INSERT INTO tbl_siswa (id, nama_siswa, nis, no_hp) VALUES (%s, %s, %s, %s)", (id, nama_siswa, nis, no_hp))
    db.commit()
    
    
def fetch_data():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tbl_siswa")
    return cursor.fetchall()


if __name__ == '__main__':
    insert_data()
    fetch_data()