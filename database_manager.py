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
                                Email TEXT NOT NULL, 
                                Username TEXT NOT NULL,
                                Password TEXT NOT NULL, 
                                LastUpdated DATETIME NOT NULL,
                                CONSTRAINT CK_Passwords
                                PRIMARY KEY(SubscriptionName, Email))""")
        
        
    def store_password(self, subscription_name:str, email:str, username:str, password:str) -> bool:
        """Returns True if successfully added to the database, returns false if there was a value already in the table with the SubsciptionName and email """
        result = None
        try:
            self.cursor.execute("""
                            INSERT INTO Passwords 
                                (SubscriptionName, Email, Username, Password, LastUpdated)
                            VALUES
                                (?, ?, ?, ?, datetime("now"))""", (subscription_name, email, username, password))
            self.connection.commit()
            result = True
        except sqlite3.IntegrityError:
            print("Subscription already has a values assoicated with that email address...")
            result = False
        return result

    def retrieve_password(self, subscription_name:str, email: str) -> tuple[str, str]:
        """Will retrieve username and password from the email and subscription name
            if there is no record found an empty tuple will be returned as ("", "").
            If there is a record the result will be returned as a tuple (username, password)"""
        query_result = self.cursor.execute("""
                            SELECT
                                Username, Password
                            FROM
                                Passwords
                            WHERE
                                SubscriptionName = ? AND Email = ?
                            """, (subscription_name, email))
        
        result = query_result.fetchone()
        if result == None:
            return "", ""
        else:
            return result


