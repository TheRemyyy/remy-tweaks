import os
import time

# Colors
PURPLE = "\033[38;2;147;112;219m"
RESET = "\033[0m"

APP_TITLE = '"Remy Tweaks | Made By: TheRemyyy | Plan: Free"'

BANNER = f"""{PURPLE}
    
    

                                      ___                   ______                __      
                                     / _ \___ __ _  __ __  /_  __/    _____ ___ _/ /__ ___
                                    / , _/ -_)  ' \/ // /   / / | |/|/ / -_) _ `/  '_/(_-<
                                   /_/|_|\__/_/_/_/\_, /   /_/  |__,__/\__/\_,_/_/\_\/___/
                                                  /___/                                   
                                                                                                                                                              
                                                {RESET}Made by {PURPLE}TheRemyyy {RESET}with {PURPLE}<3
                                                      {RESET}Plan: {PURPLE}Free{RESET}"""

MENU_BANNER = f"""{PURPLE}
          



                                      ___                   ______                __      
                                     / _ \___ __ _  __ __  /_  __/    _____ ___ _/ /__ ___
                                    / , _/ -_)  ' \/ // /   / / | |/|/ / -_) _ `/  '_/(_-<
                                   /_/|_|\__/_/_/_/\_, /   /_/  |__,__/\__/\_,_/_/\_\/___/
                                                  /___/                               
                                                                                                        
                                {RESET}Remy {PURPLE}Tweaks {PURPLE}| {RESET}Made By: {PURPLE}TheRemyyy | {RESET}Plan: {PURPLE}Free{RESET}"""

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def set_title():
    if os.name == "nt":
        os.system(f'title {APP_TITLE}')

def show_loading():
    clear_screen()
    print(BANNER)
    # The original script had an input here, preserving the flow but making it optional/enter to continue could be better
    # But adhering to original UX for now
    input(f"\n{PURPLE}       [PRESS ENTER TO START]{RESET}")
    time.sleep(0.2)

def print_done():
    print(f"\n       {PURPLE}[+] Done !!!{RESET}")
    time.sleep(2)

def print_invalid():
    print(f"\n       {PURPLE}[!] Invalid Selection !!!{RESET}")
    time.sleep(1)

def show_menu():
    clear_screen()
    print(MENU_BANNER)
    print(f"""
       {PURPLE}[1] {RESET}Memory Usage                    {PURPLE}[10] {RESET}Disable Background Programs   {PURPLE}[19] {RESET}Hardware DataQueueSize
       {PURPLE}[2] {RESET}Disable Wifi Sense              {PURPLE}[11] {RESET}Tweak Processor (CPU)         {PURPLE}[20] {RESET}BCD Tweaks
       {PURPLE}[3] {RESET}Disable WMPNetworkSvc           {PURPLE}[12] {RESET}Disable Aero Peek             {PURPLE}[21] {RESET}Memory Tweaks
       {PURPLE}[4] {RESET}Disable WalletService           {PURPLE}[13] {RESET}Disable PreLaunch             {PURPLE}[22] {RESET}Disable Telemetry
       {PURPLE}[5] {RESET}Disable Bing search             {PURPLE}[14] {RESET}Disable GameDVR               {PURPLE}[23] {RESET}Disabling unnecessary Services
       {PURPLE}[6] {RESET}Disable Xbox live network       {PURPLE}[15] {RESET}Make Windows More Secure      {PURPLE}[24] {RESET}System Tweaks
       {PURPLE}[7] {RESET}Disable Power Throttling        {PURPLE}[16] {RESET}Auto Defrag SSD               {PURPLE}[25] {RESET}Fast Start Up
       {PURPLE}[8] {RESET}Enable hardware GPU scheduling  {PURPLE}[17] {RESET}Disable Hibernation           {PURPLE}[26] {RESET}Disable TIPC
       {PURPLE}[9] {RESET}Tweak Graphic Card (GPU)        {PURPLE}[18] {RESET}High Performance 
       {PURPLE}[0] {RESET}Exit
    """)
    return input(f"       {PURPLE}[choice] {RESET}>> {PURPLE}")
