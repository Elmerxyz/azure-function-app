import logging
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    logging.info('¡Hola Mundo! Esta es una función de Azure ejecutada correctamente.')