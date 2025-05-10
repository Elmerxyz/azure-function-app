# import logging
# import pymysql
# import azure.functions as func
# import datetime

# def main(mytimer: func.TimerRequest) -> None:
#     utc_timestamp = datetime.datetime.utcnow().replace(
#         tzinfo=datetime.timezone.utc).isoformat()
    
#     logging.info(f'Python timer trigger function ejecutada en: {utc_timestamp}')
#     logging.info(f'¡PRUEBA EXITOSA! La función timer está funcionando')
    
#     if mytimer.past_due:
#         logging.info('The timer is past due!')
    
#     # Definir directamente los valores de conexión a la base de datos
#     db_host = '20.106.206.184'  # Dirección del servidor de base de datos
#     db_user = 'adminuser'  # Nombre de usuario de la base de datos
#     db_password = 'TuPasswordSegura'  # Contraseña de la base de datos
#     db_name = 'clientes_db'  # Nombre de la base de datos
    
#     logging.info("Iniciando el proceso de envío de correos...")
#     conn = None
    
#     try:
#         # Conexión a la base de datos MySQL
#         logging.info(f"Intentando conectar a MySQL en {db_host}...")
#         conn = pymysql.connect(
#             host=db_host,
#             user=db_user,
#             password=db_password,
#             db=db_name,
#             connect_timeout=10,
#             cursorclass=pymysql.cursors.DictCursor
#         )
#         logging.info("¡Conexión establecida con éxito!")
#         cursor = conn.cursor()

#         # Buscar clientes con bienvenida no enviada
#         cursor.execute("SELECT id, nombre, correo FROM clientes WHERE bienvenida_enviada = FALSE")
#         clientes = cursor.fetchall()
#         logging.info(f"Consulta ejecutada. Encontrados {len(clientes)} clientes para procesar")
        
#         # Verificar si hay clientes para procesar
#         if not clientes:
#             logging.info("No hay clientes nuevos para enviar bienvenida")
#             return

#         # Enviar bienvenida y actualizar la base de datos
#         for cliente in clientes:
#             id_cliente = cliente['id']
#             nombre = cliente['nombre']
#             correo = cliente['correo']
#             logging.info(f"Bienvenida enviada a {nombre} ({correo})")
#             cursor.execute("UPDATE clientes SET bienvenida_enviada = TRUE WHERE id = %s", (id_cliente,))

#         # Confirmar los cambios
#         conn.commit()
#         logging.info(f"Bienvenidas enviadas a {len(clientes)} clientes")

#     except Exception as e:
#         error_detallado = f"Error al procesar clientes: {str(e)}, Tipo de error: {type(e).__name__}"
#         logging.error(error_detallado)
#         # Si hubo un error en la actualización, hacer rollback
#         if conn:
#             conn.rollback()

#     finally:
#         # Cerrar la conexión de forma segura
#         if conn:
#             try:
#                 cursor.close()
#                 conn.close()
#                 logging.info("Conexión a la base de datos cerrada")
#             except:
#                 pass

#     logging.info("Proceso finalizado cfsdforrectamente.")
import logging
import azure.functions as func
import datetime

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    
    logging.info(f'Python timer trigger function ejecutada en: {utc_timestamp}')
    logging.info("Simulando procesamiento sin conexión a DB")