#!/usr/bin/env python3

import json
import sys

infile = 'records.json'

def get_data(f=infile):
    raw = open(f)
    data = json.load(raw)
    return data

def get_records(data=get_data()):
    records = []
    for albums in data.values():
        for album in albums:
            records.append(album)
    for i in records:
        print(i)
    print(f'Total: {len(records)}')
    

def get_artists(data=get_data()):
    artists = []
    for artist in data.keys():
        artists.append(artist)
    for i in artists:
        print(i)
    print(f'Total: {len(artists)}')

def add_record(data=get_data()):
    artist = input('Artist name: ')
    record = input('Record name: ')
    if artist in data:
        if record in data[artist]:
            print('That record already exists')
            sys.exit()
        records = data[artist]
    else:
        records = []
    records.append(record)
    data[artist] = records
    with open(infile,'w') as f:
        json.dump(data,f)
    

def help():
    print('Usage: add_record, get_artists, get_records')
    


if __name__ == '__main__':
    if len(sys.argv) == 1:
        help()
        sys.exit()
    cmd = eval(sys.argv[1])
    cmd()
