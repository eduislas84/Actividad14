import logging
from django.http import HttpResponse

# Obtener el logger de la aplicación
logger = logging.getLogger('miapp')

def vista_logging(request):
    logger.debug("Esto es un mensaje DEBUG.")
    logger.info("Esto es un mensaje INFO.")
    logger.warning("Esto es un mensaje WARNING.")
    logger.error("Esto es un mensaje ERROR.")
    logger.critical("Esto es un mensaje CRITICAL.")
    
    return HttpResponse("Revisa la consola o el archivo de logs para ver los mensajes generados.")
