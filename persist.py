class PersistData:
    def __init__(self, dbType):
        print("within persist data constructor")
        self.db_type = dbType
    def store_data(self):
        print('Storing data to ' + self.db_type + " file")