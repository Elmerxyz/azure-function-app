# import logging
# import azure.functions as func
# import pymysql

# def main(mytimer: func.TimerRequest) -> None:
#     logging.info('Python timer trigger function ejecutada correctamente')
    
#     # Datos de conexión a la base de datos
#     db_host = '20.106.206.184'  # Dirección del servidor de base de datos
#     db_user = 'adminuser'       # Usuario de la base de datos
#     db_password = 'TuPasswordSegura'  # Contraseña (actualizar con la correcta)
#     db_name = 'productos_db'    # Nombre de la base de datos
    
#     try:
#         # Intentar la conexión
#         logging.info(f"Intentando conectar a MySQL en {db_host}...")
#         conn = pymysql.connect(
#             host=db_host,
#             user=db_user,
#             password=db_password,
#             db=db_name,
#             connect_timeout=10,
#             cursorclass=pymysql.cursors.DictCursor
#         )
#         logging.info("¡CONEXIÓN EXITOSA a la base de datos!")
#         print("¡CONEXIÓN EXITOSA a la base de datos!")
#         # Cerrar la conexión de forma segura
#         conn.close()
#         logging.info("Conexión cerrada correctamente")
#         print("Conexión cerrada correctamente")
#     except Exception as e:
#         # Capturar y mostrar cualquier error en detalle
#         error_detallado = f"ERROR DE CONEXIÓN: {str(e)} - Tipo: {type(e).__name__}"
#         logging.error(error_detallado)
#         print(error_detallado)

import logging
import pymysql

# Configurar logging básico
logging.basicConfig(level=logging.INFO)

# Datos de conexión a la base de datos
db_host = '20.106.206.184'  # Dirección del servidor de base de datos
db_user = 'adminuser'       # Usuario de la base de datos
db_password = 'TuPasswordSegura'  # Contraseña (actualizar con la correcta)
db_name = 'clientes_db'    # Nombre de la base de datos

print("Iniciando prueba de conexión y actualización en MySQL...")

try:
    # Intentar la conexión
    print(f"Intentando conectar a MySQL en {db_host}...")
    conn = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        db=db_name,
        connect_timeout=10,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("¡CONEXIÓN EXITOSA a la base de datos!")
    
    # Buscar clientes con bienvenida no enviada
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, correo FROM clientes WHERE bienvenida_enviada = FALSE")
    clientes = cursor.fetchall()
    print(f"Se encontraron {len(clientes)} clientes para actualizar")
    
    # Actualizar cada cliente
    for cliente in clientes:
        id_cliente = cliente['id']
        nombre = cliente['nombre']
        correo = cliente['correo']
        print(f"Actualizando a {nombre} ({correo})")
        cursor.execute("UPDATE clientes SET bienvenida_enviada = TRUE WHERE id = %s", (id_cliente,))
        
    # Confirmar los cambios
    conn.commit()
    print(f"Se actualizaron {len(clientes)} registros exitosamente")
    
    # Cerrar la conexión de forma segura
    cursor.close()
    conn.close()
    print("Conexión cerrada correctamente")
    
except Exception as e:
    # Capturar y mostrar cualquier error en detalle
    error_detallado = f"ERROR DE CONEXIÓN: {str(e)} - Tipo: {type(e).__name__}"
    print(error_detallado)
    
    # Si hay una conexión activa, hacer rollback
    if 'conn' in locals() and conn:
        conn.rollback()
        print("Se ha realizado rollback de transacciones")