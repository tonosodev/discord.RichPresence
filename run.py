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
    quotes_button_1 = ["Contact me!", "VKONTAKTE", "VK.COM"]
    quotes_button_2 = [""]
    quotes_small_text = ["In Code We Trust", "Contact me!"]
    quotes_large_text = ["Meooow! 💜", "What do u think about that?"]
    quotes_large_image = ["cat_img_1", "cat_img_2", "cat_img_3"]
    while True:
        cpu_per = round(psutil.cpu_percent(), 1)
        mem = psutil.virtual_memory()
        buttons_list = [{"label": random.choice(quotes_button_1), "url": "https://vk.com/devildesigner"},
                        {"label": "| GitHub |", "url": "https://github.com/DevilDesigner"},
                        ]
        mem_per = round(psutil.virtual_memory().percent, 1)

        RPC.update(
            _donotuse=True,
            start=1,
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
