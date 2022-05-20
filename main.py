import ingest
import persist
import logging


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
    eg = Test("csv")  #Creating an instance of the objects
    eg.my_function()
    # reader = ingest.FileReader()
    # writer = persist.PersistData()
    # reader.read_file()
    # writer.store_data()