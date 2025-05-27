import sqlite3

class Database_Manager:
    __instance = None
    def __new__(cls, database_file="Passwords.db"):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self, database_file="Passwords.db") -> None:
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()
        
        # this will only ever run one time after that the table will never have to be made again
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS Passwords 
                            (SubscriptionName TEXT NOT NULL, 
                            Username TEXT NOT NULL,
                            Password TEXT NOT NULL, 
                            LastUpdated DATETIME NOT NULL)""")
        
        
    def store_password(self, subscription_name:str, username:str, password:str):
        self.cursor.execute(f"""
                            INSERT INTO Passwords 
                            (SubscriptionName, Username, Password, LastUpdated)
                            VALUES
                            ({subscription_name}, {username}, {password}, datetime("now"))""")
        self.connection.commit()




