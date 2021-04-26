import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig():
    @staticmethod   #THIS ALLOWS US TO USE THIS METHOD WITHOUT CREATING OBJECTSOF THE CLASS
    def getURL():
        myURL = config.get('common info', 'baseURL')
        return myURL

    @staticmethod
    def getUserEmail():
        myUserName = config.get('common info', 'useremail')
        return myUserName

    @staticmethod
    def getPassword():
        myPassword = config.get('common info', 'password')
        return myPassword