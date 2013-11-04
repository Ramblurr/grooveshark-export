#!/usr/bin/python
"""
Simple script that fetches the list of tracks in a grooveshark playlist and saves
them as an XSPF

Usage: grooveshark-export.py 67775494 > cool_tunes.xspf

Requires: pygrooveshark, xspf
"""
import argparse

import grooveshark as gs
import xspf


parser = argparse.ArgumentParser(description="download a grooveshark's playlist metadata to a xspf playlist")
parser.add_argument("playlist_id", help="the gs playlist id to export")
args = parser.parse_args()


client = gs.Client()
client.init()

try:
    playlist = client.playlist(args.playlist_id)
except:
    print("Parsing playlist %s failed, does it exist?", args.playlist_id)

def u(s):
    return unicode(s)


x = xspf.Xspf()
x.title = u(playlist.name)
x.info = 'From Grooveshark playlist %s' % (args.playlist_id)
x.image = playlist._cover_url

for song in playlist.songs:
    x.add_track(xspf.Track(title=u(song.name), creator=u(song.artist), album=u(song.album),trackNum=song.track, image=song.album._cover_url))

print(x.toXml())

