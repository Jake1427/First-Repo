import os
import json

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display ASCII art
def display_ascii_art():
    ascii_art = '''
    █▀▀▀▀▀▀█ █▀▀▀▀▀▀█ █▀▀▀▀▀▀█ █▄░█ █▀▀▀▀▀▀█
    █░░░░░░░█ █░░░░░░█ █░░░░░░░█ █░▀█ █░░░░░░█
    █░░░░░░░█ █░░░░░░█ █░░░░░░░█ █░░█ █░░░░░░█
    █░░░░░░░█ █░░░░░░█ █░░░░░░░█ █░░░█ █░░░░░░█
    █▄▄▄▄▄▄▄█ █▄▄▄▄▄▄▄█ █▄▄▄▄▄▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█
    '''
    print(ascii_art)

# Function to load login data from Login.json
def load_login_data():
    if os.path.exists('C:\Users\Jake1427\AppData\Local\Login.json'):
        with open('C:\Users\Jake1427\AppData\Local\Login.json', 'r') as f:
            return json.load(f)
    return {}

# Function to save login data to Login.json
def save_login_data(data):
    os.makedirs(os.path.dirname('C:\Users\Jake1427\AppData\Local\Login.json'), exist_ok=True)
    with open('C:\Users\Jake1427\AppData\Local\Login.json', 'w') as f:
        json.dump(data, f, indent=4)

# Main function for the application
def main():
    clear_console()
    display_ascii_art()

    print("Welcome to the Hacker App!")
    login_data = load_login_data()
    choice = input("1. Login\n2. Signup\nChoose an option: ").strip()

    if choice == '1':  # Login
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        if username in login_data and login_data[username] == password:
            print("Login successful!")
            # Display hacker-themed main menu
            print("-- Hacker Menu --")
            print("1. Hack the planet\n2. Exit")
            # Additional menu functionality here...
        else:
            print("Login failed. Check your username and password.")

    elif choice == '2':  # Signup
        username = input("Choose a username: ").strip()
        password = input("Choose a password: ").strip()
        login_data[username] = password
        save_login_data(login_data)
        print("Signup successful! You can now login.")

if __name__ == '__main__':
    main()