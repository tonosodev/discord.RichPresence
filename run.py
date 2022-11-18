"""
Today is 6/26/2021
Session by: https://github.com/DevilDesigner
Create Time: 7:00 PM
This Class: RichPresence
"""

from pypresence import Presence

import random
import time
import sys
from colorama import init, Fore, Back

def _print(*args):
    print(*args, end=Fore.RESET+("\r\n" if sys.platform == "win32" else "\n"))

try:
    init()
    # Logo Initialize
    print(r"""   _     _
  (c).-.(c)
   / ._. \
 __\( Y )/__            𝔻𝕚𝕤𝕔𝕠𝕣𝕕 𝔸𝕔𝕥𝕚𝕧𝕚𝕥𝕪 𝕊𝕥𝕒𝕥𝕦𝕤 ℙ𝕣𝕠𝕛𝕖𝕔𝕥
(_.-/'-'\-._)                    v.2.0.0
    |DDP|                by  vk.com/DevilDesigner
 _.' `-' '._             github.com/DevilDesigner
(.-./`-'\.-.)
 `-'     `-'""")
    # Configuration file Initialize
    try:
        with open("config.py") as con:
            print(f"{Fore.GREEN}Configuration file found!")
    except:
        print(f"{Fore.GREEN}Configuration file not found!\nCreating new...")
        with open("config.py", "w+") as configuration_file:
            configuration_file.write("""# Сonfiguration
# Contact me (https://vk.com/devildesigner) if you have some troubles.

# Get in https://discord.com/developers/applications/
# Create and select your application, after copy APPLICATION ID in "General Information".
application_id = 0

# General Status settings.
# Edit if you need:

reloading_after_exception_time = 10
next_layer_time = 10

# You can use <["text1", "text2", "..."]> structure for randomize activity status or <["text"]> structure for single text!

# Buttons
first_button_layer_1_text = ["GitHub"]
first_button_layer_1_url = ["https://github.com/NeverMindDev"]
second_button_layer_1_text = ["VK.COM"]
second_button_layer_1_url = ["https://github.com/NeverMindDev"]
first_button_layer_2_text = ["Meta Peace Team®"]
first_button_layer_2_url = ["https://discord.gg/YkyN4ws8C9"]
# LayersQuotes
quotes_large_image_text = ["May The Force be with You!"]
quotes_small_image_text = ["RichPresence Project"]
window_error_large_text = ["#404: Problems Not Found."]
window_error_small_text = ["Coffee Time ☕️"]
# LayerImages
quotes_large_image = ["cat1_1024x1024"]
quotes_small_image = ["cat1_1024x1024"]
window_error_large_image = ["coffee_1_1024x1024"]
window_error_small_image = ["coffee_3_1024x1024"]""")
        _print(f"{Fore.GREEN}Configuration file created!")
finally:
    print("Starting. . .\n##########################################################")

from config import *

while True:
    client_id = application_id
    start_time = int(time.time())
    try:
        if not client_id:
            print(f"{Fore.RED}Please, check and correct your application_id in file settings.ini!")
            exit()
        else:
            try:
                RPC = Presence(client_id)  # Initialize the Presence class
                RPC.connect()
                print("Prescense connected successfully!")
            except TimeoutError:
                print("Token error!")

        # TODO: dynamic count of layers
        code_button_1_text = first_button_layer_1_text
        code_button_1_url = first_button_layer_1_url
        code_button_2_text = second_button_layer_1_text
        code_button_2_url = second_button_layer_1_url
        code_button_3_text = first_button_layer_2_text
        code_button_3_url = first_button_layer_2_url

        code_quotes_large_text = quotes_large_image_text
        code_quotes_small_text = quotes_small_image_text
        code_quotes_this_window_error_large_text = window_error_large_text
        code_quotes_this_window_error_small_text = window_error_small_text

        code_quotes_large_image = quotes_large_image
        code_quotes_small_image = quotes_small_image
        code_window_error_large_image = window_error_large_image
        code_window_error_small_image = window_error_small_image

        sl = lambda: time.sleep(next_layer_time)

        while True:
            try:
                buttons_list = [
                    {
                        "label": random.choice(code_button_2_text),
                        "url": random.choice(code_button_2_url)}
                ]
                RPC.update(
                    # start=start_time,
                    large_text=random.choice(code_quotes_large_text),
                    small_text=random.choice(code_quotes_small_text),
                    large_image=random.choice(code_quotes_large_image),
                    small_image=random.choice(code_quotes_small_image),
                    buttons=buttons_list,
                    details="Change everything you are",
                    state="And everything you were..."
                )
                sl()

                l2_buttons_list = [
                    {
                        "label": random.choice(code_button_1_text),
                        "url": random.choice(code_button_1_url)
                    },
                ]
                RPC.update(
                    # start=start_time,
                    large_text="GitHub",
                    small_text="GitHub",
                    large_image='cat2_1024x1024',
                    small_image='cat2_1024x1024',
                    # party_size=[666, 666],
                    buttons=l2_buttons_list,
                    details="Contact me in",
                    state="⠀⠀GitHub!!"
                )
                sl()
                #
                # Activity Layer #3
                #
                l3_buttons_list = [
                    {
                        "label": random.choice(code_button_3_text),
                        "url": random.choice(code_button_3_url)
                    },
                ]
                RPC.update(
                    # start=start_time,
                    large_text="𝓜𝓮𝓽𝓪  𝓟𝓮𝓪𝓬𝓮  𝓣𝓮𝓪𝓶®",
                    small_text="𝓨𝓾𝓴𝓴𝓲 - My Discord Bot",
                    large_image='yukki_server_avatar_1024x1024',
                    small_image='yukki_512x512_image',
                    # party_size=[666, 666],
                    buttons=l3_buttons_list,
                    details="☚ 𝕸𝖞 𝕯𝖎𝖘𝖈𝖔𝖗𝖉 𝕾𝖊𝖗𝖛𝖊𝖗",
                    state="⠀⠀ ⠀⠀𝕵𝖔𝖎𝖓 𝖚𝖘!"
                )
                sl()
            #
            # Exception to check if discord is dropped
            #
            except Exception as e:
                print("\nActivity Status Error!")
                break
    #
    # General Library Exception and check if discord is not running
    #
    except Exception as e:
        print(
            "***(is the discord running?)***\n"
            "Retry connecting after " +
            str(reloading_after_exception_time)
            + " seconds...\n"
              ". . . ")
        try:
            time.sleep(reloading_after_exception_time)
            RPC = Presence(client_id)
            RPC.connect()
        except:
            continue
