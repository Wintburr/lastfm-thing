# Last.fm last listened to song displayer 🎵
This simple Python script asks the Last.fm API for the last song you listened to, then displays it in your CLI. You can use it as a base for a bigger script that could display the current song you're listening to on your Discord status, your Twitter status, or whatnot. This is all made so that it can run without any user input in mind, so that it's easy to just run and forget.

This script will run every 15 seconds, it is therefore not recommended to run it in a loop.

## Installation/Dependencies 🛠
This script uses the <a href="https://github.com/xiaomyer/lastfmpy">lastfmpy</a> Python dependency, as well as asyncio which is required for lastfmpy.
You will also need a <a href="https://www.last.fm/api/account/create">Last.fm API key</a>, but it is *very* easy to make one.
<br>
This script also uses <a href="https://pypi.org/project/pypresence/">Pypresence</a>, although this can be removed if you do not need or want Discord Rich Presence support.
<br>
**You can install all dependencies with : `pip install lastfmpy aiohttp asyncio pillow==9.2.0 numpy typing pypresence nest_asyncio`**
## How to run it
You will only need to change two things in the Python file itself : the username that the API will check for, and your API key.
<br> To replace the username : replace the `SETUSERNAMEHERE` part (at line 11) with the username you want to check for.
<br> To replace the API key : replace the `SETLASTFMAPIKEYHERE` (at line 5) with your own.
<br> If you want Discord Rich Presence support, then you will need to use your own Discord app client ID by replacing the `SETDISCORDCLIENTIDHERE`. 

# Screenshot/Example :
![image](https://user-images.githubusercontent.com/109423445/183299788-0a3f48d8-ef09-45e2-b085-3f6aed871e33.png)
<br>
(it's just a command prompt, what did you expect)

## TO-DO 📌 :
- [ ] Actually use the `lastfm.user.get_now_playing` function of lastfmpy instead of the current "getting recent tracks and hoping that the last one is the one you're currently listening to" method --> This would mean being able to grab the artist and album's names with the `lastfm.user.get_now_playing` function which idk how the fuck to do right now.
- [X] ~~Actually turn this into something that can be used to integrate my Last.fm Now Listening To thing in a Discord Rich Presence thing and whatnot other very fancy stuff (edit : progress is being made on this, the script now makes an "image" of the result when you run it, fancy!)~~ There is Discord Rich Presence support, although it is *very* barebones, but it works. <br> This also makes an image of whatever you might be listening to.

## LICENSE 📜 :
This is currently using the WTFPL, just do whatever the fuck you want with this, crediting is appreciated, but not needed. :)
