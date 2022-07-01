import configparser

configs = configparser.RawConfigParser()
configs.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getAppURL():
        baseURL = configs.get("common info", "baseURL")
        return baseURL

    @staticmethod
    def getUsername():
        username = configs.get("common info", "username")
        return username

    @staticmethod
    def getPassword():
        password = configs.get("common info", "password")
        return password
