from flask import Flask, request, jsonify
import mysql.connector
import requests
# test rubah
app = Flask(__name__)

# Koneksi ke database MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sekolah"
)

# mengirim pesan menggunakan Walazy Gateway
def kirim_pesan(no_telp, pesan):
    url = 'http://192.168.18.32:5570/api/send-message'
    headers = {
        'Authorization': 'apikeybaruya123',
        'Content-Type': 'application/json'
    }
    data = {
        "api_key": "apikeybaruya123",
        "receiver": "6281331365904",
        "data": {
            "message": pesan,
        }
    }

    # Print data for debugging
    print("Mengirim permintaan ke API dengan data berikut:")
    print(data)
    try:
        response = requests.post(url, headers=headers, json=data)
    except Exception as e:
        print(f"{data} tidak valid {e}")

    
    # Print response for debugging
    print("Status Kode:", response.status_code)
    print("Respons:", response.content)
    
    if response.status_code == 200:
        print(f"Pesan dikirim ke {no_telp}")
    else:
        print(f"Error mengirim pesan: {response.content}")

# Endpoint untuk menerima NIS
@app.route('/absensi', methods=['POST'])
def receive_nis():
    try:
        # Mendapatkan data JSON dari request
        data = request.get_json()
        if 'nis' not in data:
            return jsonify({'error': 'Data tidak lengkap, NIS tidak ditemukan'}), 400

        nis = data['nis']
        
        # Cari data siswa di database
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM siswa WHERE nis = %s", (nis,))
        siswa = cursor.fetchone()
        
        if siswa:
            # Kirim pesan ke nomor telepon orang tua
            pesan = f"Anak Anda dengan NIS {nis} telah hadir di sekolah."
            kirim_pesan(siswa['no_telp_ortu'], pesan)

            # Respon sukses
            return jsonify({'message': 'Pesan telah dikirim ke orang tua siswa'}), 200
        else:
            return jsonify({'error': 'Siswa dengan NIS tersebut tidak ditemukan di database'}), 404
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)