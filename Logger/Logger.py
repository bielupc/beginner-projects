import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("Front logger")


logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("log.log")
handler.setLevel(logging.INFO)
logger.addHandler(handler)

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)


logger.debug("Debug message")
logger.info("info msg")
    
