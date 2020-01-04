import logging


FORMAT = "%(asctime)-8s %(message)s"
logging.basicConfig(level = logging.ERROR, format=FORMAT,
                    filename="errors_logs.log", filemode="w", datefmt="%m/%d/%Y %I:%M:%S %p")