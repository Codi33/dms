import getpass
import json
import os.path


class Settings:
    def __init__(self):
        self.host = ''
        self.port = 0
        self.hours = 0
        self.passphrase = ''

    def save(self):
        with open('settings.json', 'w') as configfile:
            obj = json.dumps({
                'host': self.host,
                'port': self.port,
                'hours': self.hours,
                'passphrase': self.passphrase
            })

            configfile.write(obj)

    def load(self):
        with open('settings.json', 'r') as configfile:
            data = configfile.read()
        obj = json.loads(data)

        self.host = obj['host']
        self.port = obj['port']
        self.hours = obj['hours']; self.hours = self.hours * 3600  # 1h = 3600s
        self.passphrase = obj['passphrase']

    def exists(self) -> bool:
        return os.path.exists('settings.json')

    def init(self):
        if self.exists():
            print("Load settings from file? y/n")
            if input() == 'y' or input == 'Y':
                self.load()
            else:
                os.remove('settings.json')
                quit()
        else:
            print("Create config file? y/n")
            if input() == 'y' or input() == 'Y':
                self.host = input("Enter host ip: ")
                self.port = int(input("Enter host port: "))
                self.hours = int(input("Enter period in hours: ")); self.hours = self.hours * 3600  # 1h = 3600s
                self.passphrase = getpass.getpass(prompt="Enter passphrase: ")
                self.save()
                print("Configuration saved")
            else:
                quit()


settings = Settings()  # Global variable
