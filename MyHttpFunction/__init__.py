import logging
import pymysql
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    logging.info('Python timer trigger function ejecutada correctamente')
    
    # Configuración de la conexión a la base de datos
    db_host = '20.106.206.184'
    db_user = 'adminuser'
    db_password = 'TuPasswordSegura'
    db_name = 'clientes_db'

    try:
        # Intentar la conexión
        logging.info(f"Intentando conectar a MySQL en {db_host}...")
        conn = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            db=db_name,
            connect_timeout=10,
            cursorclass=pymysql.cursors.DictCursor
        )
        logging.info("¡CONEXIÓN EXITOSA a la base de datos!")
        
        # Buscar clientes con bienvenida no enviada
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, correo FROM clientes WHERE bienvenida_enviada = FALSE")
        clientes = cursor.fetchall()
        logging.info(f"Se encontraron {len(clientes)} clientes para actualizar")
        
        # Actualizar cada cliente
        for cliente in clientes:
            logging.info(f"Actualizando a {cliente['nombre']} ({cliente['correo']})")
            cursor.execute("UPDATE clientes SET bienvenida_enviada = TRUE WHERE id = %s", (cliente['id'],))
        
        # Confirmar los cambios
        conn.commit()
        logging.info(f"Se actualizaron {len(clientes)} registros exitosamente")
        
    except Exception as e:
        logging.error(f"ERROR DE CONEXIÓN: {str(e)} - Tipo: {type(e).__name__}")
        if 'conn' in locals() and conn:
            conn.rollback()
            logging.info("Se ha realizado rollback de transacciones")
    finally:
        if 'conn' in locals() and conn:
            cursor.close()
            conn.close()
            logging.info("Conexión cerrada correctamente")