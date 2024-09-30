import requests
import random
import os
import time
from datetime import datetime
from colorama import Fore

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def write_timestamped_username(username):
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%Y-%m-%d") 
    with open("available-usernames.txt", "a") as file:
        file.write(f"{current_date} {current_time} - [GitHub-Username] Username Available: {username}\n") 

def get_username_length():
    clear_screen()
    print(Fore.GREEN + "[GitHub-Username]: " + Fore.LIGHTYELLOW_EX + "How long should the usernames be? (minimum 3)")
    answer = input(Fore.MAGENTA + "root@you:~$ " + Fore.WHITE).strip()
    while not answer.isdigit() or int(answer) < 3:
        print(Fore.RED + "[GitHub-Username]: " + Fore.LIGHTYELLOW_EX + "Please enter a valid number greater than or equal to 3.")
        answer = input(Fore.MAGENTA + "root@you:~$ " + Fore.WHITE).strip()
    return int(answer)

def check_username(username_length):
    clear_screen()
    print(Fore.GREEN + "[GitHub-Username]: " + Fore.LIGHTYELLOW_EX + "Press" + Fore.YELLOW + " Enter" + Fore.LIGHTYELLOW_EX + " to stop the process." + Fore.RESET)
    print(Fore.GREEN + "[GitHub-Username]: " + Fore.LIGHTYELLOW_EX + "Available usernames are being saved to" + Fore.YELLOW + " available-usernames.txt" + Fore.RESET)
    print()

    total_attempts = 0 
    available_count = 0  
    taken_count = 0     

    while True:
        if os.name == 'nt':
            import msvcrt
            if msvcrt.kbhit() and msvcrt.getch() == b'\r':
                return
        else:
            import select
            i, o, e = select.select([sys.stdin], [], [], 0)
            if i:
                input()
                return

        user = "".join(random.choices("abcdefghijklmnopqrstuvwxyz123456789", k=username_length))
        total_attempts += 1  

        try:
            response = requests.get(f"https://github.com/{user}")
            if response.status_code == 404:  
                print(Fore.YELLOW + "[GitHub-Username] " + Fore.GREEN + "Username Available: " + Fore.LIGHTYELLOW_EX + f"{user}" + Fore.RESET)
                write_timestamped_username(user)
                available_count += 1  
            elif response.status_code == 200:  
                taken_count += 1  
                continue
            else:
                print("")
                print(Fore.YELLOW + "[GitHub-Username] " + Fore.LIGHTYELLOW_EX + f"Total attempts: {total_attempts - 1}")
                print(Fore.YELLOW + "[GitHub-Username] " + Fore.LIGHTYELLOW_EX + f"Available: {available_count}")
                print(Fore.YELLOW + "[GitHub-Username] " + Fore.LIGHTYELLOW_EX + f"Taken: {taken_count}")
                print()
                
                print(Fore.GREEN + "[GitHub-Username]: " + Fore.RED + f"BLOCKED FROM GITHUB with status {response.status_code}. Possible restricted username." + Fore.RESET)
                
                total_attempts = 0 
                available_count = 0  
                taken_count = 0  

                print(Fore.GREEN + "[GitHub-Username]: " + Fore.LIGHTRED_EX + f"Waiting for 15 seconds before retrying..." + Fore.RESET)
                print()
                time.sleep(15) 

        except requests.exceptions.RequestException as e:
            print()
            print(Fore.RED + "[GitHub-Username]: " + Fore.LIGHTYELLOW_EX + f"An error occurred: {str(e)}" + Fore.RESET)
            print()
            time.sleep(1.337)

while True:
    username_length = get_username_length()
    check_username(username_length)
