import logging

class FileReader:
    logging.basicConfig(level="DEBUG")
    def __init__(self, fileType):
        logging.debug("i'm within the FileReader constructor")
        self.file_type = fileType

    def read_file(self):
        logging.debug('Reading a ' + self.file_type + " file")