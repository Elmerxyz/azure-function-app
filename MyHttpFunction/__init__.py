import logging
import azure.functions as func
import pymysql

def main(mytimer: func.TimerRequest) -> None:
    logging.info('Python timer trigger function ejecutada correctamente')
    
    # Datos de conexión a la base de datos
    db_host = '20.106.206.184'  # Dirección del servidor de base de datos
    db_user = 'adminuser'       # Usuario de la base de datos
    db_password = 'TuPasswordSegura'  # Contraseña (actualizar con la correcta)
    db_name = 'productos_db'    # Nombre de la base de datos
    
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
        
        # Cerrar la conexión de forma segura
        conn.close()
        logging.info("Conexión cerrada correctamente")
        
    except Exception as e:
        # Capturar y mostrar cualquier error en detalle
        error_detallado = f"ERROR DE CONEXIÓN: {str(e)} - Tipo: {type(e).__name__}"
        logging.error(error_detallado)