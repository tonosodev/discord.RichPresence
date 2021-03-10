##### POWERED BY NeverMind#4082 #################################################

from pypresence import Presence
from config import general_settings

import random
import time
import pyautogui

try:
    logo = open("logo.yml", "r", encoding="utf8")
    data = logo.read()
    print(data)
    logo.close()
except IOError:
    print("Error reading logo image from file: " + logo.name)
finally:
    logo.close()
print("\nInjecting. . .\n################################")


while True:
    client_id = general_settings["client_id"]
    start_time = int(time.time())
    try:
        RPC = Presence(client_id)  # Initialize the Presence class
        RPC.connect()
        last = None
        print("Success!\nActivity Status is Ready!\n")
        quotes_button_1 = ["Have a question?...", "Contact me in vk.com!", "¸,ø¤º°`°º¤ø,¸ 𝕍𝕂 ¸,ø¤º°`°º¤ø,¸"]
        quotes_button_2 = ["GitHub", "Me In GitHub", "In Git We Trust"]
        yukki_quotes_button = ["𝓜𝓮𝓽𝓪 𝓟𝓮𝓪𝓬𝓮 𝓣𝓮𝓪𝓶®", "Click to Join!", "Join to my server!"]
        quotes_details = [""]
        quotes_state = [""]

        quotes_small_text = ["In Code We Trust", "Contact me!", "NeverMind in VK.com"]
        quotes_large_text = ["Meooow! 💜", "What do u think about that?"]
        quotes_large_image = ["cat1_1024x1024", "cat2_1024x1024", "cat3_1024x1024", "cat4_1024x1024", "cat5_1024x1024",
                              "cat6_1024x1024", "cat7_1024x1024", "cat8_1024x1024", "cat9_1024x1024", "cat10_1024x1024",
                              "cat12_1024x1024"]
        coffee_large_image = ["coffee_1_1024x1024", "coffee_2_1024x1024", "coffee_3_1024x1024"]
        coffee_large_text = ["Only Coffee Can Save My Soul...", "True?... Love?... Coffee!", "Always Coffee Time!"]

        while True:
            #
            # Try-catch statement to check if discord is not running
            #
            try:
                buttons_list = [
                    {
                        "label": random.choice(quotes_button_1),
                        "url": "https://vk.com/devildesigner"},
                    {
                        "label": random.choice(quotes_button_2),
                        "url": "https://github.com/DevilDesigner"},
                ]
                #
                # Activity Layer #1
                #
                RPC.update(
                    start=start_time,
                    large_text=random.choice(quotes_large_text),
                    small_text=random.choice(quotes_small_text),
                    large_image=random.choice(quotes_large_image),
                    small_image="profile_image",
                    # party_size=[666, 666],
                    buttons=buttons_list,
                    details="💜 𝕪𝕠𝕦,",
                    state="⠀⠀⠀⠀⠀𝕄𝕒𝕟𝕒☆"
                )
                time.sleep(general_settings['next_layer_time'])
                try:
                    current = pyautogui.getActiveWindowTitle()
                    #
                    # Check current activity and exceeding the length of characters
                    #
                    if current is None or len(current) >= 128:
                        continue
                    if current != last:
                        #
                        # Activity Layer #2
                        #
                        RPC.update(
                            start=start_time,
                            large_text=random.choice(quotes_large_text),
                            small_text=random.choice(quotes_small_text),
                            large_image=random.choice(quotes_large_image),
                            small_image="profile_image",
                            # party_size=[666, 666],
                            buttons=buttons_list,
                            details="Current Activity:",
                            state=f"{str(current)}",
                            instance=False
                        )
                        time.sleep(general_settings['next_layer_time'])
                        #
                        # If current windows error is detected
                        #
                except Exception as e:
                    print("[EXCEPTION] " + repr(e))
                    print("U understand what the fuck is that?\nI'm too...\nSkip it.\n")
                    # pyautogui.alert(repr(e))

                    #
                    # Activity Layer WindowERROR
                    #
                    RPC.update(
                        start=start_time,
                        large_text=random.choice(coffee_large_text),
                        small_text=random.choice(quotes_small_text),
                        large_image=random.choice(coffee_large_image),
                        small_image="profile_image",
                        # party_size=[666, 666],
                        buttons=buttons_list,
                        details="Current Activity:",
                        state="Coffee Time ☕"
                    )
                time.sleep(general_settings['next_layer_time'])

                yukki_buttons_list = [
                    {
                        "label": random.choice(yukki_quotes_button),
                        "url": "https://discord.gg/VSAcZUX22a"},
                ]
                #
                # Activity Layer #3
                #
                RPC.update(
                    start=start_time,
                    large_text="𝓜𝓮𝓽𝓪  𝓟𝓮𝓪𝓬𝓮  𝓣𝓮𝓪𝓶®",
                    small_text="𝓨𝓾𝓴𝓴𝓲 - Developer's Bot",
                    large_image='yukki_server_avatar_1024x1024',
                    small_image='yukki_512x512_image',
                    # party_size=[666, 666],
                    buttons=yukki_buttons_list,
                    details="☚ 𝕸𝖞 𝕯𝖎𝖘𝖈𝖔𝖗𝖉 𝕾𝖊𝖗𝖛𝖊𝖗",
                    state="⠀⠀ ⠀⠀𝕵𝖔𝖎𝖓 𝖚𝖘!"
                )
                time.sleep(general_settings['next_layer_time'])
            #
            # Exception to check if discord is dropped
            #
            except Exception as e:
                print("\nDiscord Dropped!\n")
                break
    #
    # General Library Exception and check if discord is not running
    #
    except Exception as e:
        print(
            "CAPTAIN, ERROR!\nOh, sorry, not an error...\nor...\nOMG, DISCORD NOT RUNNED!\nRetry connecting via " + str(
                general_settings['loading_time']) + " seconds...\n. . . ")
        time.sleep(general_settings['loading_time'])
        try:
            RPC = Presence(client_id)  # Initialize the Presence class
            RPC.connect()
            time.sleep(general_settings['loading_time'])
        except:
            continue
