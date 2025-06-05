from tkinter import *
from tkinter import ttk
import password_manager
import database_manager

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500

def login(event):
    global pw_handle, db_handle
    
    # If name is empty or password is empty then ask to enter password and username 
    # After name has been supplied check the database for a master password
    # Once database has been checked see if a private key was supplied if a private key was supplied use it to go ahead and there is a master password, decrypt the password
        # If password entered and password in the database match and the username entered and username in the database match then the login is successful
        # Else let the user know that the username or password did not match and to please try again, or private key is incorrect
    # If private key was not provided and there is a master ask them to input the private key
    # If private key was not provided and there is no master, create an entry in the database with the username and password entered as the master
    
    if private_Key.get():
        pw_handle = password_manager.PasswordManager(private_key=private_Key.get().encode())
        stored_username, stored_password = db_handle.retrieve_password("DB_MASTER", "N/A")
        
        if password.get() == "" or username.get() == "":
            if (len(password.get()) < 10) or username.get() == "":
                print("please enter a password that is at least 10 characters long and please enter your username")
        else: 
            print("CREATED")
        stored_password = pw_handle.decrypt_password(pw_handle.get_private_key(), stored_password.encode())
        if stored_username == username.get() and stored_password == password.get():
            print("SUCCESS")
            title_label.grid_remove()
            username_label.grid_remove()
            username_entry.grid_remove()
            password_entry.grid_remove()
            password_label.grid_remove()
            private_key_label.grid_remove()
            private_Key_entry.grid_remove()
            temp_label = ttk.Label(main_frame, text="LOGGED IN SUCCESSFULLY", font=("Times", 25))
            temp_label.grid(row=0, column=0, rowspan=2, columnspan=2)
            temp_label.after(3000, temp_label.grid_remove)
            
            main_window.bind("<Return>", "") # Basically override the current binding to be nothing
            
    else:
        pw_handle = password_manager.PasswordManager()
    
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
title_label = ttk.Label(main_frame, text="Password Generator and Retriever", font=("Times", 25))
title_label.grid(row=0, column=0, columnspan=3, sticky="")

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

private_Key = StringVar()
private_Key_entry = ttk.Entry(main_frame, width=30, textvariable=private_Key, show="*")
private_Key_entry.grid(row=2, column=1, sticky="SW")

username_entry.focus()

# Password Handler and Database handler
pw_handle = password_manager.PasswordManager()
db_handle = database_manager.Database_Manager()

main_window.bind("<Return>", login)
# TODO: REMOVE THIS IS JUST FOR TESTING PURPOSES ------------------------------------------------------------

# password, encrypted_password, private_key = pw_handle.create_password()
# db_handle.store_password("DB_MASTER","N/A", "KelvinRoman", encrypted_password)
# print(f"\nPrivate Key:{private_key}\nPassword:{password}")

# password, encrypted_password, private_key = pw_handle.create_password()
# db_handle.store_password("SubscriptionName","Email@gmail.com", "Username", encrypted_password)
# print("\n", private_key, password)

# password, encrypted_password, private_key = pw_handle.create_password()
# db_handle.store_password("SubscriptionName2","Email2@gmail.com", "Username2", encrypted_password)
# print("\n", private_key, password)

# password, encrypted_password, private_key = pw_handle.create_password()
# db_handle.store_password("Amazon","Email2@gmail.com", "Username2", encrypted_password)
# print("\nAmazon", private_key, password)


# username, password  = db_handle.retrieve_password("Amazon", "Email2@gmail.com")
# password = pw_handle.decrypt_password(pw_handle.get_private_key(), password.encode())
# print(username, password )
# ------------------------------------------------------------------------------------------------------------

main_window.mainloop()