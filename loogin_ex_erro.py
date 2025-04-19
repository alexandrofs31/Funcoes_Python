from loguru import logger

logger.debug("Iniciando o processamento de dados")
logger.info("Carregando o arquivo CSV")
logger.warning("O arquivo CSV não foi encontrado")
logger.error("Erro ao processar o arquivo CSV")
logger.critical("Falha crítica no sistema")