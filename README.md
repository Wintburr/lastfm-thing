# Last.fm last listened to song displayer
This simple Python script asks the Last.fm API for the last song you listened to, then displays it in your CLI. You can use it as a base for a bigger script that could display the current song you're listening to on your Discord status, your Twitter status, or whatnot.

## Installation/Dependencies
This script uses the <a href="https://github.com/xiaomyer/lastfmpy">lastfmpy</a> Python dependency, as well as asyncio which is required for lastfmpy.
<br> You will also need a <a href="https://www.last.fm/api/account/create>Last.fm API key</a>, but it is *very* easy to make one.
<br>
## How to run it
You will only need to change two things in the Python file itself : the username that the API will check for, and your API key.
<br> To replace the username : replace the `SETUSERNAMEHERE` part (at line 11) with the username you want to check for.
<br> To replace the API key : replace the `SETAPIKEYHERE` (at line 5) with your own.

# Screenshot/Example :
![image](https://user-images.githubusercontent.com/109423445/183299788-0a3f48d8-ef09-45e2-b085-3f6aed871e33.png)
(it's just a command prompt, what did you expect)

## TO-DO :
Actually use the `lastfm.user.get_now_playing` function of lastfmpy instead of the current "getting recent tracks and hoping that the last one is the one you're currently listening to" method --> This would mean being able to grab the artist and album's names with the `lastfm.user.get_now_playing` function which idk how the fuck to do right now.
<br> Actually turn this into something that can be used to integrate my Last.fm Now Listening To thing in a Discord Rich Presence thing and whatnot other very fancy stuff

## LICENSE
This is currently using the WTFPL, just do whatever the fuck you want with this, crediting is appreciated, but not needed. :)
