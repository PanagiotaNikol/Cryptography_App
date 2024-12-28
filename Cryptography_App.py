# Importing necessary modules for GUI creation
import tkinter as tk
from tkinter import *
import customtkinter

# Setting the appearance mode for the customtkinter framework
customtkinter.set_appearance_mode("dark")

# Initializing the main window for the application
Window = customtkinter.CTk()
Window.title("Cryptography App")  # Setting the title of the application
Window.geometry("400x300")       # Setting the dimensions of the application window

# Function to switch between different frames in the application
def show_frame(frame):
    frame.tkraise()

# Creating frames for each cryptography method to work on the main page
Main = customtkinter.CTkFrame(master=Window, width=400, height=300)
caesar = customtkinter.CTkFrame(master=Window, width=400, height=300)
affine = customtkinter.CTkFrame(master=Window, width=400, height=300)
vigenere = customtkinter.CTkFrame(master=Window, width=400, height=300)

# Placing frames in the window and ensuring they are aligned
for frame in (Main, caesar, affine, vigenere):
    frame.place(relx=0.5, rely=0.5, anchor="center")

# Function for Caesar Cipher GUI and logic
def Caesar():
    # GUI elements for input and output in Caesar cipher
    text1 = customtkinter.CTkLabel(master=caesar, text="Insert the Text you want to encrypt:")
    text1.place(relx=0.5, rely=0.1, anchor=CENTER)

    text2 = customtkinter.CTkLabel(master=caesar, text="Insert the key:")
    text2.place(relx=0.2, rely=0.3, anchor=CENTER)

    entry = customtkinter.CTkEntry(master=caesar, placeholder_text="Insert Text", width=220, height=25)
    entry.place(relx=0.5, rely=0.2, anchor=CENTER)

    entry2 = customtkinter.CTkEntry(master=caesar, placeholder_text="Insert Key", width=150, height=25)
    entry2.place(relx=0.5, rely=0.3, anchor=CENTER)

    text3 = customtkinter.CTkLabel(master=caesar, text="")
    text3.place(relx=0.5, rely=0.7, anchor=CENTER)

    # Function to perform Caesar encryption
    def Encryption(entry, entry2):
        Text_Input = entry.get()  # Retrieve the input text
        key = int(entry2.get())  # Convert the key input to integer
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        text_output = '' 

        Text_Input = Text_Input.upper()  # Convert text to uppercase

        # Encrypt each character
        for i in range(len(Text_Input)):
            char = Text_Input[i]  
            if char in alphabet:
                old_index = alphabet.index(char)
                new_index = (old_index + key) % 26  # Shift the character by the key
                text_output += alphabet[new_index]
            else:
                text_output += char  # Retain non-alphabetic characters
        
        text3.configure(text="Your message is: " + text_output)  # Display the encrypted message

    buttonEncr = customtkinter.CTkButton(master=caesar, text="Encrypt", command=lambda: Encryption(entry, entry2))
    buttonEncr.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Back button to return to the main menu
    back_button = customtkinter.CTkButton(master=caesar, text="Back", command=lambda: show_frame(Main))
    back_button.place(relx=0.5, rely=0.9, anchor="center")

# Functions for Affine Cipher GUI and logic
def Affine():
    # GUI elements for Affine cipher main menu
    text = customtkinter.CTkLabel(master=affine, text="Choose the Cipher you want:")
    text.place(relx=0.5, rely=0.2, anchor=CENTER)

    buttonEn = customtkinter.CTkButton(master=affine, text="Encryption", command=lambda: Encryption())
    buttonEn.place(relx=0.5, rely=0.4, anchor=CENTER)
    buttonDec = customtkinter.CTkButton(master=affine, text="Decryption", command=lambda: Decryption())
    buttonDec.place(relx=0.5, rely=0.6, anchor=CENTER)

    back_button = customtkinter.CTkButton(master=affine, text="Back", command=lambda: show_frame(Main))
    back_button.place(relx=0.5, rely=0.9, anchor="center")

    # Function to perform Affine Encryption
    def Encryption():
        # Clear main menu buttons
        buttonEn.place_forget()
        buttonDec.place_forget()

        # GUI elements for Affine encryption inputs and outputs
        text1 = customtkinter.CTkLabel(master=affine, text="Insert the Text you want to encrypt:")
        text1.place(relx=0.5, rely=0.1, anchor=CENTER)

        entry = customtkinter.CTkEntry(master=affine, placeholder_text="Insert Text", width=220, height=25)
        entry.place(relx=0.5, rely=0.2, anchor=CENTER)

        text2 = customtkinter.CTkLabel(master=affine, text="Insert the a and b:")
        text2.place(relx=0.5, rely=0.3, anchor=CENTER)

        entry2 = customtkinter.CTkEntry(master=affine, placeholder_text="Insert a", width=90, height=25)
        entry2.place(relx=0.3, rely=0.4, anchor=CENTER)

        entry3 = customtkinter.CTkEntry(master=affine, placeholder_text="Insert b", width=90, height=25)
        entry3.place(relx=0.7, rely=0.4, anchor=CENTER)

        text3 = customtkinter.CTkLabel(master=affine, text="")
        text3.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Function to calculate Affine encryption
        def affine_encrypt(text, a, b):
            Text_Input = entry.get()
            a = int(entry2.get())
            b = int(entry3.get())
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            m = len(alphabet)  # Length of the alphabet
            text_output = ""

            Text_Input = Text_Input.upper()  # Convert text to uppercase

            # Encrypt each character
            for char in Text_Input:
                if char in alphabet:
                    x = alphabet.index(char)  # Current character index
                    new_char_index = (a * x + b) % m  # Affine encryption formula
                    text_output += alphabet[new_char_index]
                else:
                    text_output += char  # Retain non-alphabetic characters

            text3.configure(text="Your message is: " + text_output)  # Display the encrypted message

        # Button to trigger the encryption function
        buttonEncr = customtkinter.CTkButton(master=affine, text="Encrypt", command=lambda: affine_encrypt(entry, entry2, entry3))
        buttonEncr.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Back button to return to the main Affine menu
        back_button = customtkinter.CTkButton(master=affine, text="Back", command=lambda: show_frame(Main))
        back_button.place(relx=0.5, rely=0.9, anchor="center")

    # Function to perform Affine Decryption
    def Decryption():
        # Clear main menu buttons
        buttonEn.place_forget()
        buttonDec.place_forget()

        # GUI elements for Affine decryption inputs and outputs
        text1 = customtkinter.CTkLabel(master=affine, text="Insert the Text you want to decrypt:")
        text1.place(relx=0.5, rely=0.1, anchor=CENTER)

        entry = customtkinter.CTkEntry(master=affine, placeholder_text="Insert Text", width=220, height=25)
        entry.place(relx=0.5, rely=0.2, anchor=CENTER)

        text2 = customtkinter.CTkLabel(master=affine, text="Insert the a and b:")
        text2.place(relx=0.5, rely=0.3, anchor=CENTER)

        entry2 = customtkinter.CTkEntry(master=affine, placeholder_text="Insert a", width=90, height=25)
        entry2.place(relx=0.3, rely=0.4, anchor=CENTER)

        entry3 = customtkinter.CTkEntry(master=affine, placeholder_text="Insert b", width=90, height=25)
        entry3.place(relx=0.7, rely=0.4, anchor=CENTER)

        text3 = customtkinter.CTkLabel(master=affine, text="")
        text3.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Helper function to find the modular inverse of `a` under modulo `m`
        def mod_inverse(a, m):
            for x in range(1, m):
                if (a * x) % m == 1:
                    return x
            return None

        # Function to calculate Affine decryption
        def affine_decrypt(text, a, b):
            Text_Input = entry.get()
            a = int(entry2.get())
            b = int(entry3.get())
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            m = len(alphabet)  # Length of the alphabet
            text_output = ""

            Text_Input = Text_Input.upper()  # Convert text to uppercase

            a_inv = mod_inverse(a, m)  # Calculate modular inverse of `a`
            if a_inv is None:  # Check if the modular inverse exists
                text3.configure(text="Error: No modular inverse found for a.")
                return

            # Decrypt each character
            for char in Text_Input:
                if char in alphabet:
                    y = alphabet.index(char)  # Current character index
                    new_char_index = (a_inv * (y - b)) % m  # Affine decryption formula
                    text_output += alphabet[new_char_index]
                else:
                    text_output += char  # Retain non-alphabetic characters

            text3.configure(text="Your message is: " + text_output)  # Display the decrypted message

        # Button to trigger the decryption function
        buttonEncr = customtkinter.CTkButton(master=affine, text="Decrypt", command=lambda: affine_decrypt(entry, entry2, entry3))
        buttonEncr.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Back button to return to the main Affine menu
        back_button = customtkinter.CTkButton(master=affine, text="Back", command=lambda: show_frame(Main))
        back_button.place(relx=0.5, rely=0.9, anchor="center")

# Functions for Vigenere Cipher GUI and logic
def Vigenere():
    # GUI elements for Vigenere cipher main menu
    text = customtkinter.CTkLabel(master=vigenere, text="Choose the Cipher you want:")
    text.place(relx=0.5, rely=0.2, anchor=CENTER)

    buttonEn = customtkinter.CTkButton(master=vigenere, text="Encryption", command=lambda: Encryption())
    buttonEn.place(relx=0.5, rely=0.4, anchor=CENTER)
    buttonDec = customtkinter.CTkButton(master=vigenere, text="Decryption", command=lambda: Decryption())
    buttonDec.place(relx=0.5, rely=0.6, anchor=CENTER)

    back_button = customtkinter.CTkButton(master=vigenere, text="Back", command=lambda: show_frame(Main))
    back_button.place(relx=0.5, rely=0.9, anchor="center")

    # Function to perform Vigenere Encryption
    def Encryption():
        # Clear main menu buttons
        buttonEn.place_forget()
        buttonDec.place_forget()

        # GUI elements for Vigenere encryption inputs and outputs
        text1 = customtkinter.CTkLabel(master=vigenere, text="Insert the Text you want to encrypt:")
        text1.place(relx=0.5, rely=0.1, anchor=CENTER)

        entry = customtkinter.CTkEntry(master=vigenere, placeholder_text="Insert Text", width=220, height=25)
        entry.place(relx=0.5, rely=0.2, anchor=CENTER)

        text2 = customtkinter.CTkLabel(master=vigenere, text="Insert the key:")
        text2.place(relx=0.2, rely=0.3, anchor=CENTER)

        entry2 = customtkinter.CTkEntry(master=vigenere, placeholder_text="Insert Key", width=150, height=25)
        entry2.place(relx=0.5, rely=0.3, anchor=CENTER)

        text3 = customtkinter.CTkLabel(master=vigenere, text="")
        text3.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Function to calculate Vigenere encryption
        def vigenere_encrypt(entry, entry2):
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            text_output = ""
            key = entry2.get()
            key = key.upper()
            text = entry.get()
            text = text.upper()
            key_index = 0

            for char in text:
                if char in alphabet:
                    text_index = alphabet.index(char)
                    key_char = key[key_index % len(key)]
                    key_index_char = alphabet.index(key_char)
                    new_char_index = (text_index + key_index_char) % 26
                    text_output += alphabet[new_char_index]
                    key_index += 1
                else:
                    text_output += char

            text3.configure(text="Your message is: " + text_output)

        buttonEncr = customtkinter.CTkButton(master=vigenere, text="Encrypt", command=lambda: vigenere_encrypt(entry, entry2))
        buttonEncr.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Back button to return to the main Vigenere menu
        back_button = customtkinter.CTkButton(master=vigenere, text="Back", command=lambda: show_frame(Main))
        back_button.place(relx=0.5, rely=0.9, anchor="center")

    # Function to perform Vigenere Decryption
    def Decryption():
        # Clear main menu buttons
        buttonEn.place_forget()
        buttonDec.place_forget()

        # GUI elements for Vigenere decryption inputs and outputs
        text1 = customtkinter.CTkLabel(master=vigenere, text="Insert the Text you want to decrypt:")
        text1.place(relx=0.5, rely=0.1, anchor=CENTER)

        entry = customtkinter.CTkEntry(master=vigenere, placeholder_text="Insert Text", width=220, height=25)
        entry.place(relx=0.5, rely=0.2, anchor=CENTER)

        text2 = customtkinter.CTkLabel(master=vigenere, text="Insert the key:")
        text2.place(relx=0.2, rely=0.3, anchor=CENTER)

        entry2 = customtkinter.CTkEntry(master=vigenere, placeholder_text="Insert Key", width=150, height=25)
        entry2.place(relx=0.5, rely=0.3, anchor=CENTER)

        text3 = customtkinter.CTkLabel(master=vigenere, text="")
        text3.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Function to calculate Vigenere decryption
        def vigenere_decrypt(entry2, entry):
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            text_output = ""
            key = entry2.get()
            key = key.upper()
            text = entry.get()
            text = text.upper()
            key_index = 0

            for char in text:
                if char in alphabet:
                    text_index = alphabet.index(char)
                    key_char = key[key_index % len(key)]
                    key_index_char = alphabet.index(key_char)
                    new_char_index = (text_index - key_index_char) % 26
                    text_output += alphabet[new_char_index]
                    key_index += 1
                else:
                    text_output += char

            text3.configure(text="Your message is: " + text_output)

        buttonEncr = customtkinter.CTkButton(master=vigenere, text="Decrypt", command=lambda: vigenere_decrypt(entry2, entry))
        buttonEncr.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Back button to return to the main Vigenere menu
        back_button = customtkinter.CTkButton(master=vigenere, text="Back", command=lambda: show_frame)

# Making the Main Page of the app
def main():

    text = customtkinter.CTkLabel(master=Main, text="Choose your Cipher:")
    text.place(relx = 0.5,rely= 0.2, anchor=CENTER)

    buttonC = customtkinter.CTkButton(master=Main , text= "Caesar Cipher", command= lambda : show_frame(caesar))
    buttonC.place(relx = 0.5, rely= 0.3, anchor  = CENTER)

    buttonA = customtkinter.CTkButton(master=Main, text= "Affine Cipher", command= lambda : show_frame(affine))
    buttonA.place(relx = 0.5,rely = 0.5, anchor = CENTER)

    buttonV = customtkinter.CTkButton(master=Main, text= "Vigenere Cipher", command= lambda : show_frame(vigenere))
    buttonV.place(relx = 0.5, rely = 0.7, anchor = CENTER)

    
# Write the variables of the frames to start working at the start of the app
main()
Caesar()
Affine()
Vigenere()

# Which Page i want to show on the start of the app
show_frame(Main)

Window.mainloop()
