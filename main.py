from tkinter import *
from tkinter import ttk
import password_manager
import database_manager


        
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500

# Main Window Set up
main_window = Tk()
main_window.title("Password Generator and Retriever")
main_window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
main_window.maxsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
main_window.columnconfigure(0, weight=1)
main_window.rowconfigure(0, weight=1)

# The main frame is where all of the other widgets will be placed on. 
main_frame = ttk.Frame(main_window)
main_frame.grid(column=0, row=0, sticky='NESW')
main_frame.columnconfigure((0, 1, 2), weight=1)
main_frame.rowconfigure(0, weight=2)
main_frame.rowconfigure((1, 2), weight=1)

# Labels
title_lable = ttk.Label(main_frame, text="Password Generator and Retriever", font=("Times", 25))
title_lable.grid(row=0, column=0, columnspan=3, sticky="")

username_label = ttk.Label(main_frame, text="Username: ", font=("Times", 15))
username_label.grid(row=1, column=0, sticky="NE")

password_label = ttk.Label(main_frame, text="Password: ", font=("Times", 15) )
password_label.grid(row=1, column=0, sticky="E")

private_key_label = ttk.Label(main_frame, text="Private Key: ", font=("Times", 10) )
private_key_label.grid(row=2, column=0, sticky="SE")

# Username, Password, Private Key Entry
username = StringVar()
username_entry = ttk.Entry(main_frame, width=30, textvariable=username)
username_entry.grid(row=1, column=1, sticky="NW")

password = StringVar()
password_entry = ttk.Entry(main_frame, width=30, textvariable=password)
password_entry.grid(row=1, column=1, sticky="W")

private_key = StringVar()
private_key_entry = ttk.Entry(main_frame, width=30, textvariable=password)
private_key_entry.grid(row=2, column=1, sticky="SW")

username_entry.focus()

# Password Handler and Database handler
pw_handle = password_manager.PasswordManager()
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

main_window.mainloop()