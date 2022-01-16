#!/usr/bin/env python3

import json
import sys

infile = 'records.json'

def get_records(data):
    records = []
    for albums in data.values():
        for album in albums:
            records.append(album)
    return records 
    

def get_artists(data):
    artists = []
    for artist in data.keys():
        artists.append(artist)
    return artists 

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Need an action')
        sys.exit()
    cmd = eval(sys.argv[1])
    raw = open(infile)
    data = json.load(raw)
    
    result = cmd(data)
    for i in result:
        print(i)
