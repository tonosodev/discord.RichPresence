import random

import psutil
from pypresence import Presence
from config import general_settings
import time

print("Initialize...")
try:
    client_id = general_settings["client_id"]
    RPC = Presence(client_id)  # Initialize the Presence class
    RPC.connect()
    print("Connected!")
    quotes_button_1 = ["Have a question?...", "Contact me!", "¸,ø¤º°`°º¤ø,¸ 𝕍𝕂 ¸,ø¤º°`°º¤ø,¸"]
    quotes_button_2 = ["Join to Meta Peace Team®", "My Discord Server", "Yukki is waiting for you!"]

    quotes_details = [""]
    quotes_state = [""]

    quotes_small_text = ["In Code We Trust", "Contact me!"]
    quotes_large_text = ["Meooow! 💜", "What do u think about that?"]
    quotes_large_image = ["cat1_1024x1024", "cat2_1024x1024", "cat3_1024x1024"]
    while True:
        cpu_per = round(psutil.cpu_percent(), 1)
        mem = psutil.virtual_memory()
        buttons_list = [{"label": random.choice(quotes_button_1), "url": "https://vk.com/devildesigner"},
                        {"label": random.choice(quotes_button_2), "url": "https://discord.gg/ZrfkCEAcfW"},
                        ]
        mem_per = round(psutil.virtual_memory().percent, 1)


        RPC.update(
            _donotuse=True,
            # start=time(),
            large_text=random.choice(quotes_large_text),
            small_text=random.choice(quotes_small_text),
            large_image=random.choice(quotes_large_image),
            small_image="profile_image",

            # party_size=[1, 4],
            buttons=buttons_list,
            details="RAM: " + str(mem_per) + "%",
            state="CPU: " + str(cpu_per) + "%")
        time.sleep(5)
        # print("Update Success!")

except:
    print("Code exception.")
