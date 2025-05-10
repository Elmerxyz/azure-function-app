import logging
import pymysql
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    # Definir directamente los valores de conexión a la base de datos
    db_host = '20.106.206.184'  # Dirección del servidor de base de datos
    db_user = 'adminuser'  # Nombre de usuario de la base de datos
    db_password = 'TuPasswordSegura'  # Contraseña de la base de datos
    db_name = 'productos_db'  # Nombre de la base de datos

    try:
        # Conexión a la base de datos MySQL
        conn = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            db=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = conn.cursor()

        # Buscar clientes con bienvenida no enviada
        cursor.execute("SELECT id, nombre, correo FROM clientes WHERE bienvenida_enviada = FALSE")
        clientes = cursor.fetchall()

        # Enviar bienvenida y actualizar la base de datos
        for cliente in clientes:
            id_cliente = cliente['id']
            nombre = cliente['nombre']
            correo = cliente['correo']
            logging.info(f"Bienvenida enviada a {nombre} ({correo})")
            cursor.execute("UPDATE clientes SET bienvenida_enviada = TRUE WHERE id = %s", (id_cliente,))

        # Confirmar los cambios
        conn.commit()

    except Exception as e:
        logging.error(f"Error al procesxascar clientes: {str(e)}")

    finally:
        # Cerrar la conexión de forma segura
        if conn:
            cursor.close()
            conn.close()

    logging.info("Proceso finalizado correctamente.")
