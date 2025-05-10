import logging
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    logging.info('Python timer trigger function ejecutada correctamente')