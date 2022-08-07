from lastfmpy import LastFM
import asyncio
from PIL import Image, ImageDraw
from typing import Union
import numpy as np

API_KEY = "SETAPIKEYHERE"

def resize(fp: str, scale: Union[float, int]) -> np.ndarray:
    """ Resize an image maintaining its proportions
    Args:
        fp (str): Path argument to image file
        scale (Union[float, int]): Percent as whole number of original image. eg. 53
    Returns:
        image (np.ndarray): Scaled image
    """
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
    what = await lastfm.user.get_recent_tracks("SETUSERNAMEHERE",extended=True)
    print(f"\"{what.items[0].name}\" by {what.items[0].artist} from \"{what.items[0].album}\"")
#   THIS IS THE PART WHERE WE WRITE INFOS IN A PNG SO YOU CAN RUN THIS SCRIPT ON A WEB SERVER AND EMBED THE IMAGE ON YOUR GITHUB AND OTHER
    width = 300
    height = 50
    text = (f"\"{what.items[0].name}\" by {what.items[0].artist} from \"{what.items[0].album}\"")
    img = Image.new('RGB', (width, height), color='black')
    imgDraw = ImageDraw.Draw(img)
    imgDraw.text((20, 20), text, fill=(255, 255, 255))
    img.save('result.png')

if __name__ == "__main__":
    asyncio.run(main())

resized = resize("result.png", 200)
resized.save("wa.png")
