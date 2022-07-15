"""
Today is 6/26/2021
Session by: https://github.com/DevilDesigner
Create Time: 7:00 PM
This Class: RichPresence
"""

from pypresence import Presence

import random
import time
import pyautogui
import configparser

try:
    # Logo Initialize
    try:
        with open("/Users/mindcontrol/Documents/GitHub Projects/discord.RichPresence/logo.yml", "r", encoding="utf8") as logo:
            data = logo.read()
            print(data)
    except FileNotFoundError:
        print("\033[33m{}".format("Logo file not found!\nSkipped."))
    # Settings file Initialize
    try:
        with open("settings.ini") as con:
            print("\033[32m{}\033[0m".format("Settings file found!"))
    except:
        print("\033[31m{}".format("Settings file not found!\nCreating new..."))
        with open("settings.ini", "w+") as settings_file:
            settings_file.write('[GeneralSettings]\n'
                                '# Get in https://discord.com/developers/applications/\n'
                                '# Create and select your application, after copy APPLICATION ID in "General Information".\n'
                                'application_id =\n'
                                '# General Status settings.\n'
                                '# Edit if you need:\n'
                                'next_layer_time = 7\n'
                                'reloading_after_exception_time = 10')
        print("\033[32m{}\033[0m".format("Settings file created!\n"))
    # Configuration file Initialize
    try:
        with open("config.py") as con:
            print("\033[32m{}\033[0m".format("Configuration file found!"))
    except:
        print("\033[31m{}".format("Configuration file not found!\nCreating new..."))
        with open("config.py", "w+") as configuration_file:
            configuration_file.write('# Layers configuration\n'
                                     '# You can use <["text1", "text2", "..."]> structure for randomize activity status or <["text"]> structure for single text!\n'
                                     '# Contact me (https://vk.com/devildesigner) if you have some troubles.\n\n'
                                     '# Buttons\n'
                                     'first_button_layer_1_text = ["Layer 1 first Button Text"]\n'
                                     'first_button_layer_1_url = ["https://first_button_url_here"]\n'
                                     'second_button_layer_1_text = ["Layer 1 second Button Text"]\n'
                                     'second_button_layer_1_url = ["https://second_button_url_here"]\n'
                                     'first_button_layer_2_text = ["Layer 2 first Button Text"]\n'
                                     'first_button_layer_2_url = ["https://discord.gg/YkyN4ws8C9"]\n'
                                     '# LayersQuotes\n'
                                     'quotes_large_image_text = ["Large Image text!"]\n'
                                     'quotes_small_image_text = ["Small Image text!"]\n'
                                     'window_error_large_text = ["#404: Problems Not Found."]\n'
                                     'window_error_small_text = ["Small Image text!"]\n'
                                     '# LayerImages\n'
                                     'quotes_large_image = ["your_image_1_name", "your_image_2_name"]\n'
                                     'quotes_small_image = ["your_image_3_name"]\n'
                                     'window_error_large_image = ["your_image_4_name"]\n'
                                     'window_error_small_image = ["your_image_5_name"]')
        print("\033[32m{}\033[0m".format("Configuration file created!\n"))
finally:
    print("Injecting. . .\n##########################################################")

from config import first_button_layer_1_text, first_button_layer_1_url, second_button_layer_1_text, second_button_layer_1_url, \
    quotes_large_image_text, quotes_small_image_text, quotes_large_image, \
    quotes_small_image, window_error_large_image, window_error_small_image, \
    first_button_layer_2_text, first_button_layer_2_url, window_error_large_text, window_error_small_text

settings = configparser.ConfigParser()
settings.read("settings.ini")

while True:
    client_id = settings["GeneralSettings"]["application_id"]
    start_time = int(time.time())
    try:
        if not settings["GeneralSettings"]["application_id"]:
            print("\033[31m{}".format("Please, check and correct your application_id in file settings.ini!"))
            exit()
        else:
            try:
                RPC = Presence(client_id)  # Initialize the Presence class
                RPC.connect()
                print("Prescense connected successfully!")
            except TimeoutError:
                print("Token error!")

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
                time.sleep(int(settings["GeneralSettings"]["next_layer_time"]))

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
                time.sleep(int(settings["GeneralSettings"]["next_layer_time"]))
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
                time.sleep(int(settings["GeneralSettings"]["next_layer_time"]))
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
            "Retry connecting via " +
            str(settings["GeneralSettings"]["reloading_after_exception_time"])
            + " seconds...\n"
              ". . . ")
        time.sleep(int(settings["GeneralSettings"]["reloading_after_exception_time"]))
        try:
            RPC = Presence(client_id)
            RPC.connect()
            time.sleep(int(settings["GeneralSettings"]["reloading_after_exception_time"]))
        except:
            continue
