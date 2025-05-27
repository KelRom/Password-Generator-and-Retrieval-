import password_manager
import database_manager

pw_handle = password_manager.PasswordManager(True, 14)
db_handle = database_manager.Database_Manager()

# TODO: REMOVE THIS IS JUST FOR TESTING PURPOSES
db_handle.store_password("SubscriptionName", "Username", "password")