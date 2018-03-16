import json
import urllib.request as urx
import sys
import keyboard

globalauth = "Bearer BQAtYYkSXO-dYEtt5FlTpiMX8PKXYbzvyLuADumxiCwr2RP6qp8j7F4tlRwmGfcisUMUS7oINIs3YEvsO0rqwweUvf36ZBIq1sgxtr_YpfYm2h-R4f6O8w4Zoq1OFWM8o4vmZCgW9oCifVhJE3oOlxyr7eZvOvLOZflq7FZ904_24zvKErJzIF48tXNpNgIPcFh6LXUQ9ZkxiEi00ksHgWTezbd5VtbJBOvCyPI6TRP8xr9wEgyvgUx6IScq6Ws09e4TJT70rv8"

isquit = False

def saveCurrentSong():

    # Get Current Song ID
    # curl -X GET "https://api.spotify.com/v1/me/player/currently-playing"
    print("Requesting Current Song")
    req = urx.Request("https://api.spotify.com/v1/me/player/currently-playing")
    req.add_header("Accept", "application/json")
    req.add_header("Authorization", globalauth)
    req.add_header("User-Agent", "Mozilla/5.0")

    data_new = json.loads(urx.urlopen(req).read())

    # Current song ID is data_new['item']['id']

    currentSongID = data_new['item']["id"]

    # Save current song to Self
    print("Saving Song")
    req = urx.Request("https://api.spotify.com/v1/me/tracks?ids=%s" % currentSongID, method='PUT')
    req.add_header("Accept", "application/json")
    req.add_header("Authorization", globalauth)
    req.add_header("User-Agent", "Mozilla/5.0")

    urx.urlopen(req)
    print("Saved")

def quickQuit():
    print("quitting")
    global isquit
    isquit = True



keyboard.add_hotkey('ctrl+alt+o+p', saveCurrentSong)
keyboard.add_hotkey('ctrl+alt+o+t', quickQuit)

while True:
    if isquit == True:
        sys.exit()
    else:
        pass