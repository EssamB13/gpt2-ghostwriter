## Adapted from this tutorial https://towardsdatascience.com/song-lyrics-genius-api-dcc2819c29

import lyricsgenius as lg # https://github.com/johnwmillr/LyricsGenius
import os 
import csv
import pandas as pd
from requests.exceptions import Timeout

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print (os.getcwd())
file = open("lyrics_TEST.txt", "a", encoding='utf-8-sig')  # File to write lyrics to
genius = lg.Genius('9eaSCQyRFX_uPmVcRmDRqjvs96eX-sN-41ucB5h81RQDGBVl000JfDsnPgutY6x7',  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)
genius.timeout = 15


artists = [
        "Eminem", "Kendrick Lamar", "Big Shaq", "Cardi B", "Travis Scott", "Logic",
        "Kanye West", "Lil Uzi Vert", "Fetty Wap", "Post Malone", "JAY-Z", "Lil Wayne", "Snoop Dogg",
        "2Pac", "J. Cole", "50 Cent", "T.I.", "Dr. Dre", "Migos", "Future", "OutKast",
        "Busta Rhymes","A$AP Rocky", "A$AP Ferg", "Ice Cube", "Rick Ross", "2 Chainz", "Wu-Tang Clan", "Juice Wrld", "Young Thug",
        "Big Sean", "Ghostface Killah", "Donald Glover", "Jeezy", "DMX", "Chance the Rapper", "Rakim",
        "LL Cool J", "Wiz Khalifa", "Chris Brown", "N.W.A", "Scarface", "XXXTENTACION", "The Notorious B.I.G.", "Nas",
        "André 3000", "Childish Gambino", "Nate Dogg", "Joyner Lucas", "The Game",
        "Ludacris", "Kid Cudi", "Redman", "Lauryn Hill", "Nicki Minaj", "KRS-One", "Big Pun", "Pusha T", "Hopsin", 
        "ScHoolboy Q", "Meek Mill", "Raekwon", "Xzibit", "Slick Rick", "Denzel Curry", "MF DOOM", "Missy Elliott",
        "Big Daddy Kane", "Lupe Fiasco", "Gucci Mane", "Warren G", "RZA", "Q-Tip", "GZA", "B.o.B",
        "Twista", "21 Savage", "Big Boi", "Lil Dicky", "Prodigy of Mobb Deep", "NF", "Proof", "Talib Kweli",
        "Ski Mask the Slump God", "Obie Trice", "G-Eazy", "Yelawolf", "Earl Sweatshirt", "Chuck D", "MC Ren", "YG",
        "DaBaby", "Drake", "Danny Brown", "Aesop Rock", "Blackstar", "Cordae", "Cam’Ron", "Doja Cat", "Immortal Technique",
        "Jack Harlow", "Lil Yachty", "Lil Baby", "Lil Keed", "Lil Tecca", "Macklemore", "Megan Thee Stallion", 
        "Mac Miller", "NBA Youngboy", "Ol' Dirty Bastard", "Pop Smoke", "Tyler the Creator", "Yung Lean",
        "Vince Staples", "Trippie Redd", "Tech N9ne", "Stunna 4 Vegas", "Roddy Ricch", "Playboi Carti",
        "Machine Gun Kelly", "Lil Skies", "Lil Durk", "Jadakiss", "Dumbfoundead", "Eyedea", "Eyedea & Abilities",
        "Brother Ali", "Atmosphere", "Sadistik", "Lil Ugly Mane", "Mos Def", "Madvillain", "Jedi Mind Tricks", 
        "Quasimoto", "Deltron 3030", "El-P", "Run the Jewels", "Killer Mike", "Viktor Vaughn",
        "The Cool Kids", "Busdriver", "Milo", "A Tribe Called Quest", "​R.A.P. Ferreira", 
    ]

print (len(artists))

def get_lyrics(arr, k):  # Write lyrics of k songs by each artist in arr
    c = 0 # Counter
    for name in arr:
        retries = 0 
        while retries < 3:
            try:
                print ("trying")
                artist_obj = genius.search_artist(name, max_songs=k, sort='popularity')
            except Timeout as e:
                retries += 1
                print ("RETRYING: ", name)
                continue
            if artist_obj is not None:
                for i in range(artist_obj.num_songs):
                    song = artist_obj.songs[i]

                    if song.lyrics is not None:
                        file.write('\n'+ song.lyrics + "\n<delim>")
                        print("song saved: ", song.title)
                        c += 1 
                    else:
                        print("SONG BROKEN: ", song.title)
            
            break 
    print ("Songs gathered: ", c)
#get_lyrics(artists, 35)
file.close()

with open("lyrics_5k.txt", "r", encoding='utf-8-sig', newline='') as file:
    contents = file.read()
    df = pd.DataFrame(contents.split('<delim>'),columns=['lyrics_col'])

print (df)