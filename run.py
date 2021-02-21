import random

from pypresence import Presence
from config import general_settings
import time
from win32gui import GetWindowText, GetForegroundWindow

print("Injecting. . .")
try:
    try:
        client_id = general_settings["client_id"]
        RPC = Presence(client_id)  # Initialize the Presence class
        RPC.connect()
        print("#\nInjected!\n#")
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
        while True:
            buttons_list = [
                {
                    "label": random.choice(quotes_button_1),
                    "url": "https://vk.com/devildesigner"},
                {
                    "label": random.choice(quotes_button_2),
                    "url": "https://github.com/DevilDesigner"},
            ]

            RPC.update(
                # start=int(time.time()),
                large_text=random.choice(quotes_large_text),
                small_text=random.choice(quotes_small_text),

                large_image=random.choice(quotes_large_image),
                small_image="profile_image",

                # party_size=[666, 666],
                buttons=buttons_list,

                details="💜 𝕪𝕠𝕦,",
                state="⠀⠀⠀⠀⠀𝕄𝕒𝕟𝕒☆"
            )
            time.sleep(7)

            RPC.update(
                # start=int(time.time()),
                large_text=random.choice(quotes_large_text),
                small_text=random.choice(quotes_small_text),

                large_image=random.choice(quotes_large_image),
                small_image="profile_image",

                # party_size=[666, 666],
                buttons=buttons_list,
                details="Current Activity:",
                state=GetWindowText(GetForegroundWindow())
            )
            time.sleep(7)
            # print("Update Success!")

            yukki_buttons_list = [
                {
                    "label": random.choice(yukki_quotes_button),
                    "url": "https://discord.gg/VSAcZUX22a"},
            ]
            RPC.update(
                # start=int(time.time()),
                large_text="𝓜𝓮𝓽𝓪  𝓟𝓮𝓪𝓬𝓮  𝓣𝓮𝓪𝓶®",
                small_text="𝓨𝓾𝓴𝓴𝓲 - Developer's Bot",

                large_image='yukki_server_avatar_1024x1024',
                small_image='yukki_512x512_image',

                # party_size=[666, 666],
                buttons=yukki_buttons_list,
                details="☚ 𝕸𝖞 𝕯𝖎𝖘𝖈𝖔𝖗𝖉 𝕾𝖊𝖗𝖛𝖊𝖗",
                state="⠀⠀ ⠀⠀𝕵𝖔𝖎𝖓 𝖚𝖘!"
            )
            time.sleep(7)

    except ConnectionError:
        print("User disconnect...")
except:
    print("Code exception.")
