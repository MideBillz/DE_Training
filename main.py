import ingest
import persist
import logging

print("This is a program")

class Test:
    def __init__(self, fileType):
        print("i'm within the constructor")
        self.file_type = fileType
    def my_function(self):
         print('inside my function . Processing ' + self.file_type + " file")
         reader = ingest.FileReader(self.file_type)
         writer = persist.PersistData("postgres")
         reader.read_file()
         writer.store_data()


if __name__ == '__main__':
    print("Entering the main method")
    logging.basicConfig(level = "DEBUG")
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    print("Hello World")
    eg = Test("csv")  #Creating an instance of the objects
    eg.my_function()