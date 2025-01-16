import pymysql
connection = pymysql.connect(host="localhost",user="root",passwd="",database="db_pendidikan")
cursor = connection.cursor()

def add_text(nama_barang_jasa, deskripsi):
    try:
        cursor.execute("INSERT INTO content (id, nama_barang_jasa, deskripsi) VALUES (DEFAULT, %s, %s)",(nama_barang_jasa, deskripsi),)
        connection.commit()
        return 1
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()  
        return 0

def get_data():
    cursor.execute("SELECT * FROM content")
    rows = cursor.fetchall()
    return rows

def update_text(id, nama_barang_jasa, deskripsi):
    query = "UPDATE content SET nama_barang_jasa = %s, deskripsi = %s WHERE id = %s"
    values = (nama_barang_jasa, deskripsi, id)
    cursor.execute(query, values)
    connection.commit()
    return cursor.rowcount > 0

def delete_text(id):
    query = "DELETE FROM content WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()

    return cursor.rowcount > 0 

def get_data_by_id(id):
    query = "SELECT * FROM content WHERE id = %s"
    cursor.execute(query, (id,))
    rows = cursor.fetchall()
    return rows