import logging

class LogGenerator():
    @staticmethod
    def logGenerator():
        # logging.basicConfig(filename=".\\logs\\auto.log",
        #                 format='%(asctime)s: %(message)s:', datefmt='%d/%m/%Y %I:%M:%S %p')
        # logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        # return logger

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler = logging.FileHandler(filename='.\\logs\\auto.log')
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger

