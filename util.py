#!/usr/bin/env python3

import json
import sys

infile = 'records.json'

def get_data(f=infile):
    raw = open(f)
    data = json.load(raw)
    return data

def list(arg):
    data = get_data()
    if arg == "artists":
        artists = []
        for artist in data.keys():
            artists.append(artist)
        for i in sorted(artists):
            print(i)
        print(f'========\nNumber of artists: {len(artists)}')
        exit(0)
    
    elif arg == "records":
        records = []
        artist = input('Artist name or "all" for all records: ')
        print()
        if artist == "all":
            for record in data.values():
                for i in record:
                    records.append(i)
        else:
            if artist not in data:
                print(f'{artist} does not exist in the catalogue')
                exit(1)
            else:
                for record in data[artist]:
                    records.append(record)
        for i in sorted(records):
            print(i)

        print(f'\n########\nArtist: {artist}')
        print(f'Number of records: {len(records)}')

def add(arg):
    data = get_data()
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
    
def del_record():
    data=get_data()
    artist = input('Artist name: ')
    record = input('Record name: ')

def help():
    print('Usage: [add, list] [artists, records]')
    

if __name__ == '__main__':
    if len(sys.argv) in [1,2]:
        help()
        sys.exit()
    cmd = eval(sys.argv[1])
    arg = sys.argv[2]
    cmd(arg)
