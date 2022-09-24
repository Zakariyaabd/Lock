from cryptography.fernet import Fernet

class smart_lock: 

    def __init__(self): 
        self.password_file = None 
        self.password_dict = {}

    def create_key(self, path): 
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f: 
            f.write(self.key)

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def create_file(self, path, initia_values=None): 
        self.password_file = path 

        if initia_values is not None: 
            for key, value in initia_values.items():
                self.add_password(key, value)

    def load_file(self, path): 
        self.password_file = path 

        with open(path, 'r') as f: 
            for line in f: 
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode())

    def add_password(self, site, password): 
        self.password_dict[site] = password

        if self.password_file is not None: 
            with open(self.password_file, 'a') as f: 
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site): 
        return self.password_dict[site]







        