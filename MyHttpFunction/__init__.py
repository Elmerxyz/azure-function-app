import logging
import azure.functions as func
import datetime

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    
    logging.info(f'Python timer trigger function ejecutada en: {utc_timestamp}')
    logging.info(f'¡PRUEBA EXITOSA! La función timer está funcionando')
    
    if mytimer.past_due:
        logging.info('The timer is past due!')
    
    # Simular la lógica sin conexión a base de datos
    logging.info("Simulando proceso de envío de correos...")
    
    # Datos de ejemplo (simulando resultados de la base de datos)
    clientes_ejemplo = [
        {"id": 1, "nombre": "Juan Pérez", "correo": "juan@ejemplo.com"},
        {"id": 2, "nombre": "María López", "correo": "maria@ejemplo.com"}
    ]
    
    # Simulación de procesamiento
    for cliente in clientes_ejemplo:
        logging.info(f"Simulando envío de bienvenida a: {cliente['nombre']} ({cliente['correo']})")
    
    logging.info(f"Bienvenidas simuladas enviadas a {len(clientes_ejemplo)} clientes")
    logging.info("Proceso finalizado correctamente.")