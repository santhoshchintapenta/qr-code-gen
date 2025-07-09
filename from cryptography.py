from cryptography.fernet import Fernet
from datetime import datetime
import os

KEY_FILE = 'secret.key'
NOTES_FILE = 'notes.enc'

# Function to generate key
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)

# Function to load key
def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

# Function to write encrypted note
def write_note():
    note = input("📝 Enter your note: ")
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_note = f"[{time_now}] {note}"
    encrypted_note = Fernet(load_key()).encrypt(full_note.encode())

    with open(NOTES_FILE, 'ab') as f:
        f.write(encrypted_note + b'\n')
    print("✅ Note saved and encrypted.\n")

# Function to read all notes
def read_notes():
    if not os.path.exists(NOTES_FILE):
        print("❌ No notes found.")
        return

    print("\n📂 Your Notes (decrypted):")
    with open(NOTES_FILE, 'rb') as f:
        for line in f:
            decrypted = Fernet(load_key()).decrypt(line.strip())
            print(decrypted.decode())

# Main menu
def menu():
    while True:
        print("\n🔐 Encrypted Notes CLI App")
        print("1. Write a new note")
        print("2. View all notes")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            write_note()
        elif choice == '2':
            read_notes()
        elif choice == '3':
            print("👋 Exiting. Stay safe!")
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
