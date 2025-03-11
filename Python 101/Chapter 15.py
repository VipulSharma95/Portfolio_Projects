import logging

logging.basicConfig(filename="sample.log", level=logging.INFO)

logging.debug("this is a debug message")
logging.info("Informational Message")
logging.error("An Error has occured")

log = logging.getLogger("ex")

try:
    raise RuntimeError
except RuntimeError:
    log.exception("error")
