import logging

class PersistData:
    logging.basicConfig(level="DEBUG")
    def __init__(self, dbType):
        logging.debug("within persist data constructor")
        self.db_type = dbType
    def store_data(self):
        logging.debug('Storing data to ' + self.db_type + " file")