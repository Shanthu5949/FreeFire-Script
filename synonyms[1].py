import requests
import time
import os
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Typing animation for banner
def typing_banner(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

# Display the banner
typing_banner(Fore.RED + r"""
  ______               _______         
   / ____/_______  ___  / ____(_)_______ 
  / /_  / ___/ _ \/ _ \/ /_  / / ___/ _ \
 / __/ / /  /  __/  __/ __/ / / /  /  __/
/_/   /_/   \___/\___/_/   /_/_/   \___/ 
""")

# Kali-like prompt
def kali_prompt(text):
    return Fore.GREEN + "$ " + Fore.CYAN + text + Style.RESET_ALL

# Get user inputs
def get_user_inputs():
    uid = input(kali_prompt("Enter your UID: "))
    region = input(kali_prompt("Enter your region (e.g., 'ind'): "))
    try:
        views = int(input(kali_prompt("Enter the number of views you need: ")))
        if views <= 0:
            raise ValueError
    except ValueError:
        print(Fore.RED + "Invalid input for views. Please enter a positive integer.")
        sys.exit(1)
    
    return uid, region, views

# Send view requests
def send_view_requests(uid, region, views):
    api_url = f"https://garena420ffapi.vercel.app/spam_visit?uid={uid}&region={region}&key=Cookieee"
    call_count = max(1, views // 100)
    
    print(Fore.YELLOW + "\nProcessing requests...\n" + Style.RESET_ALL)
    
    for i in range(call_count):
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            print(Fore.GREEN + f"{(i + 1) * 100} views sent successfully.")
        except requests.RequestException as e:
            print(Fore.RED + f"An error occurred: {e}")
        
        time.sleep(0.1)  # Small delay to avoid overloading the server

# Launch FreeFire Max game
def launch_game():
    print(Fore.YELLOW + "\nAll requests completed.\n" + Style.RESET_ALL)
    print(Fore.GREEN + "Launching FreeFire Max..." + Style.RESET_ALL)

    # Simulate game launch (replace with actual path if necessary)
    if sys.platform == "win32":
        os.system("start FreeFireMax")  # For Windows
    elif sys.platform == "linux":
        os.system("xdg-open FreeFireMax")  # For Linux (adjust if needed)
    elif sys.platform == "darwin":  # macOS check
        os.system("open FreeFireMax")
    else:
        print(Fore.RED + "Game auto-launch not supported on this OS.")

# Main function
def main():
    uid, region, views = get_user_inputs()
    send_view_requests(uid, region, views)
    launch_game()

# Entry point
if __name__ == "__main__":
    main()