import ingest
import persist
import logging
import logging.config


class Test:
    logging.config.fileConfig("resources/configs/logging.conf")
    def __init__(self, fileType):
        logging.debug("i'm within the constructor")
        self.file_type = fileType
    def my_function(self):
         logging.debug('inside my function . Processing ' + self.file_type + " file")
         reader = ingest.FileReader(self.file_type)
         writer = persist.PersistData("postgres")
         reader.read_file()
         writer.store_data()


if __name__ == '__main__':
    print("Entering the main method")
    print("Hello World")
    eg = Test("csv")  #Creating an instance of the objects
    eg.my_function()