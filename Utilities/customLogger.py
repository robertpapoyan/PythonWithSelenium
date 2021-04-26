import logging

class LogGenerator():
    @staticmethod
    def logGenerator():
        logging.basicConfig(filename=".\\logs\\auto.log",
                        format='%(asctime)s: %(message)s:', datefmt='%d/%m/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

