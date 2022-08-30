from lastfmpy import LastFM
import asyncio
from PIL import Image, ImageDraw
from typing import Union
import numpy as np
import time
from pypresence import Presence
import nest_asyncio
nest_asyncio.apply()

client_id = 'SETDISCORDCLIENTIDHERE' # Replace this with your own Discord client id, only necessary if you want Discord Rich Presence support 
                                             # You can get one at https://discord.com/developers/applications
RPC = Presence(client_id)
RPC.connect()

API_KEY = "SETAPIKEYHERE " # Replace this with your own Last.fm API key, you can get one at https://www.last.fm/api

def resize(fp: str, scale: Union[float, int]) -> np.ndarray:
    _scale = lambda dim, s: int(dim * s / 100)
    im = Image.open(fp)
    width, height = im.size
    new_width: int = _scale(width, scale)
    new_height: int = _scale(height, scale)
    new_dim: tuple = (new_width, new_height)
    return im.resize(new_dim,Image.NEAREST)

async def main():
    lastfm = await LastFM(API_KEY)
#   recent = await lastfm.user.get_now_playing("Luttyz")
    what = await lastfm.user.get_recent_tracks("SETUSERNAMEHERE",extended=True) # REPLACE `Luttyz` WITH YOUR LAST.FM USERNAME
    print(f"\"{what.items[0].name}\" by {what.items[0].artist} from \"{what.items[0].album}\"")
#   THIS IS THE PART WHERE WE WRITE INFOS IN A PNG SO YOU CAN RUN THIS SCRIPT ON A WEB SERVER AND EMBED THE IMAGE ON YOUR GITHUB AND OTHER
    width = 500
    height = 50
    text = (f"\"{what.items[0].name}\" by {what.items[0].artist} from \"{what.items[0].album}\"")
    img = Image.new('RGB', (width, height), color='black')
    imgDraw = ImageDraw.Draw(img)
    imgDraw.text((20, 20), text, fill=(255, 255, 255))
    img.save('result.png')
    resized = resize("result.png", 200)
    resized.save("wa.png")
#   THIS IS THE PART FOR DISCORD RICH PRESENCE SUPPORT, IT'S VERY BAREBONES AND YOU HONESTLY MIGHT NOT WANT IT SO JUST COMMENT THE NEXT LINE IF YOOU DON'T WANT
    RPC.update(details="Listening to",state=f"\"{what.items[0].name}\" by {what.items[0].artist} from \"{what.items[0].album}\"")
    time.sleep(15)

if __name__ == "__main__":
    while True:
        asyncio.run(main())
