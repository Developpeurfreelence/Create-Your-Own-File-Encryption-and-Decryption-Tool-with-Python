

import time
from cryptography.fernet import Fernet, InvalidToken
import os
from PIL import Image, ImageTk

from tkinter import *
from tkinter import ttk, messagebox, filedialog

def generate_key():
    key = Fernet.generate_key()
    with open("Secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("Secret.key", "rb").read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    
    save_path = filedialog.asksaveasfilename(defaultextension=".enc", filetypes=[("Encrypted Files", "*.enc")])
    if save_path:
        with open(save_path, "wb") as file:
            file.write(encrypted_data)
            messagebox.showinfo("Success", f"File Encrypted and saved as '{os.path.basename(save_path)}'")

def decrypt(filename, key):
    for _ in range(3):
        try:
            f = Fernet(key)
        except ValueError:
            print("Invalid decryption key format. Make sure the key is 32 bytes and base64-encoded.")
        else:
            with open(filename, "rb") as file:
                encrypted_data = file.read()
                try:
                    decrypted_data = f.decrypt(encrypted_data)
                except InvalidToken:
                    print("Invalid key")
                else:
                    save_path = filedialog.asksaveasfilename(defaultextension=".dec", filetypes=[("Decrypted Files", "*.dec")])
                    if save_path:
                        with open(save_path, "wb") as file:
                            file.write(decrypted_data)
                            print("File Decrypted Successfully!!!")
                            messagebox.showinfo("Success", f"File Decrypted and saved as '{os.path.basename(save_path)}'")
                        return
        time.sleep(1800)  # Wait for 30 minutes
        print("Please wait for 30 minutes and try again.")

    print("Exceeded maximum attempts. Please wait for 30 minutes and try again.")

def main():
    windows = Tk()
    windows.title("File Encryption and Decryption")

    windows.title("Background Image Example")

    # Load the background image using Pillow
    background_image = Image.open("asus.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a label with the background image
    background_label = Label(windows, image=background_photo)
    background_label.place(relwidth=1, relheight=1)  
    
    def enter_data():
        accepted = accept_var.get()

        if accepted == "Accepted":
            filename = file_entry.get()
            if os.path.exists(filename):
                key = load_key()
                if encrypt_var.get():
                    encrypt(filename, key)
                elif decrypt_var.get():
                    hash_before = calculate_hash(open(filename, "rb").read())
                    decrypt(filename, key)
                    hash_after = calculate_hash(open(filename, "rb").read())
                    if hash_before == hash_after:
                        print("File Decrypted and Integrity Verified Successfully!!!")
                    else:
                        print("File Decrypted, but integrity check failed.")
            else:
                messagebox.showerror("Error", f"File '{filename}' not found. Please check the file name and try again.")
        else:
            messagebox.showwarning("Error", "You have not accepted the terms")

    frame = Frame(windows)
    frame.pack()

    accept_var = StringVar(value="Not Accepted")
    terms_check = Checkbutton(frame, text="I accept the terms and conditions.", variable=accept_var,
                              onvalue="Accepted", offvalue="Not Accepted")
    terms_check.pack()

    file_entry = Entry(frame, width=40)
    file_entry.pack()

    encrypt_var = BooleanVar(value=True)
    encrypt_check = Checkbutton(frame, text="Encrypt", variable=encrypt_var)
    encrypt_check.pack()

    decrypt_var = BooleanVar(value=False)
    decrypt_check = Checkbutton(frame, text="Decrypt", variable=decrypt_var)
    decrypt_check.pack()

    enter_button = Button(frame, text="Enter", command=enter_data)
    enter_button.pack()

    def calculate_hash(data):
        # Calculate a hash of the data for integrity check
        return hash(data)

    windows.mainloop()

if __name__ == "__main__":
    main()
