import random
from cryptography.fernet import Fernet

# tokens - will be stored in the database
# private keys will be kept by the user in order to obtain the password


class PasswordManager:
    __instance = None
    PASSWORD_MANDATORY_CHARACTERS: str = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    PASSWORD_SPECIAL_CHARACTERS: str = "~!@#$%^&*()-_=+[]{}\\|;:'\",<.>/?"
    # Overrided this function in order to create only one instance of this class, which is a singleton, this is called before object is initialized
    # This is a static method, this is used for creating an object, which __init__ is used for initializing it

    def __new__(cls, should_use_special_characters: bool = True, password_length: int = 15, private_key=None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, should_use_special_characters: bool = True, password_length: int = 15, private_key=None):
        self.should_use_special_characters = should_use_special_characters
        self.password_length = password_length
        self.private_key = Fernet.generate_key()

    # --------------------------------------------------------------------- PRIVATE METHODS ---------------------------------------------------------------------

    def __generate_password(self) -> str:
        generated_password: str = ""
        if self.should_use_special_characters:
            generated_password = "".join(random.sample(
                PasswordManager.PASSWORD_MANDATORY_CHARACTERS + PasswordManager.PASSWORD_SPECIAL_CHARACTERS, self.password_length))
        else:
            generated_password = "".join(random.sample(
                PasswordManager.PASSWORD_MANDATORY_CHARACTERS, self.password_length))
        return generated_password

    def __generate_salt(self) -> str:
        return "".join(random.sample(PasswordManager.PASSWORD_MANDATORY_CHARACTERS + PasswordManager.PASSWORD_SPECIAL_CHARACTERS, self.password_length))

    def __encrypt_password(self, salted_password: str):
        """This returns the the public key respectively\n
            Ensure the safety of your private key. The private key will be used later to get your password when needed."""
        encrypter: Fernet = Fernet(self.private_key)
        return encrypter.encrypt(salted_password.encode())

    # --------------------------------------------------------------------- PUBLIC METHODS ---------------------------------------------------------------------

    def create_password(self) -> tuple[str, str, str]:
        """Returns the generated password, the encrypted password/token, and the private key
            The private key is returned so that the user can store the private key and use it to get there passwords"""
        generated_password: str = self.__generate_password()
        salted_password: str = generated_password + self.__generate_salt()
        encrypted_password: bytes = self.__encrypt_password(salted_password)
        return generated_password, encrypted_password.decode(), self.private_key.decode()

    def decrypt_password(self, private_key: bytes, token: bytes):
        try:
            decrypter = Fernet(private_key)
            message = decrypter.decrypt(token).decode()
            return message[:self.password_length]
        except:
            return "Could not decrypt! this is not the correct private key or there is no password to decrypt"

    def set_private_key(self, private_key: bytes):
        self.private_key = private_key

    def get_private_key(self):
        return self.private_key