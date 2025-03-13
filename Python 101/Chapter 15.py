import logging
import otherMod
import otherMod2
"""
logging.basicConfig(filename="sample.log", level=logging.INFO)

logging.debug("this is a debug message")
logging.info("Informational Message")
logging.error("An Error has occured")

log = logging.getLogger("ex")

try:
    raise RuntimeError
except RuntimeError:
    log.exception("error")

def main():
    logging.basicConfig(filename='mySnake.log',level=logging.INFO)
    logging.info("Program started")
    result = otherMod.add(7,8)
    logging.info("Done!")
"""

def main():
    logger = logging.getLogger("exampleApp")
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler("new_snake.log")

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    fh.setFormatter(formatter)

    logger.addHandler(fh)

    logger.info("Program started")
    result = otherMod2.add(7,8)
    logger.info("Done!")

if __name__ == "__main__":
    main()

