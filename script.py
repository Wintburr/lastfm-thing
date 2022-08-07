from lastfmpy import LastFM
import asyncio
import requests

API_KEY = "SETAPIKEYHERE"


async def main():
    lastfm = await LastFM(API_KEY)
#   recent = await lastfm.user.get_now_playing("Luttyz")
    what = await lastfm.user.get_recent_tracks("SETUSERNAMEHERE",extended=True)
    print(f"\"{what.items[0].name}\" by {what.items[0].artist} from \"{what.items[0].album}\"")

if __name__ == "__main__":
    asyncio.run(main())