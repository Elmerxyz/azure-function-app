import logging
import pymysql
import azure.functions as func
import os

def main(mytimer: func.TimerRequest) -> None:
    db_host = os.getenv('20.106.206.184')
    db_user = os.getenv('adminuser')
    db_password = os.getenv('TuPasswordSegura')
    db_name = os.getenv('productos_db')

    try:
        conn = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            db=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = conn.cursor()

        cursor.execute("SELECT id, nombre, correo FROM clientes WHERE bienvenida_enviada = FALSE")
        clientes = cursor.fetchall()

        for cliente in clientes:
            id_cliente = cliente['id']
            nombre = cliente['nombre']
            correo = cliente['correo']
            logging.info(f"Bienvenida enviada a {nombre} ({correo})")
            cursor.execute("UPDATE clientes SET bienvenida_enviada = TRUE WHERE id = %s", (id_cliente,))

        conn.commit()
        cursor.close()
        conn.close()
        logging.info("Proceso finalizado correctamente.")

    except Exception as e:
        logging.error(f"Error al procesar clientes: {str(e)}")
