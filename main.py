import password_manager
import database_manager

pw_handle = password_manager.PasswordManager(True, 14)
db_handle = database_manager.Database_Manager()

# TODO: REMOVE THIS IS JUST FOR TESTING PURPOSES ------------------------------------------------------------

password, encrypted_password, private_key = pw_handle.create_password()
db_handle.store_password("SubscriptionName","Email@gmail.com", "Username", encrypted_password)
print("\n", private_key, password)

password, encrypted_password, private_key = pw_handle.create_password()
db_handle.store_password("SubscriptionName","Email@gmail.com", "Username", encrypted_password)
print("\n", private_key, password)

password, encrypted_password, private_key = pw_handle.create_password()
db_handle.store_password("SubscriptionName2","Email2@gmail.com", "Username2", encrypted_password)
print("\n", private_key, password)

password, encrypted_password, private_key = pw_handle.create_password()
db_handle.store_password("Amazon","Email2@gmail.com", "Username2", encrypted_password)
print("\nAmazon", private_key, password)


username, password  = db_handle.retrieve_password("Amazon", "Email2@gmail.com")
pw_handle.set_private_key(b"RnM5x5wv_e-CFVjJirgKhFoDfflEa6RRUvrhKN6lNeA=")
password = pw_handle.decrypt_password(pw_handle.get_private_key(), password.encode())
print(username, password )
# ------------------------------------------------------------------------------------------------------------