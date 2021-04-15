
import lyricsgenius as lg # https://github.com/johnwmillr/LyricsGenius
import os 
import csv
import pandas as pd
import sys
from requests.exceptions import Timeout


genius = lg.Genius('9eaSCQyRFX_uPmVcRmDRqjvs96eX-sN-41ucB5h81RQDGBVl000JfDsnPgutY6x7',  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)

genius.timeout = 15

# artists = ["Lil Ugly Mane", "Kendrick Lamar", "Freddie Gibbs"]
"Freddie Gibbs", "Kanye West" # Left these two out for testing purposes, will add more artists to this list
artists = [
        "Eminem", "Kendrick Lamar", "Big Shaq", "Cardi B", "Travis Scott", "Logic",  
        "Lil Uzi Vert", "Fetty Wap", "Post Malone", "JAY-Z", "Lil Wayne", "Snoop Dogg",
        "2Pac", "J. Cole", "50 Cent", "T.I.", "Dr. Dre", "Migos", "Future", "OutKast",
        "Busta Rhymes","A$AP Rocky", "A$AP Ferg", "Ice Cube", "Rick Ross", "2 Chainz", "Wu-Tang Clan", "Juice Wrld", "Young Thug",
        "Big Sean", "Ghostface Killah", "Jeezy", "DMX", "Chance the Rapper", 
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

Rd_arr = ["Danny Brown", "Freddie Gibbs", "Lauryn Hill", "Aesop Rock", "Lupe Fiasco"]

print (len(artists))

def get_lyrics(arr, k):  # Write lyrics of k songs by each artist in arr
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print (os.getcwd())
    lyrics_file = open("lyrics_5kheaders.txt", "a", encoding='utf-8-sig')  # File to write lyrics to
      
    log_file = open("log.txt", "a", encoding="utf-8")

    c = 0 # Counter
    for name in arr:
        retries = 0 
        while retries < 3:
            try:
                print ("trying ", name)
                artist_obj = genius.search_artist(name, max_songs=k, sort='popularity')
            except Timeout as e:
                retries += 1
                print ("RETRYING: ", name)
                continue
            if artist_obj is not None:
                log_file.write(name + "\n")
                for i in range(artist_obj.num_songs):
                    song = artist_obj.songs[i]
                    if song.lyrics is not None:
                        lyrics_file.write("<< {} - {} >> \n".format(name, song.title))
                        lyrics_file.write('\n'+ song.lyrics + "\n<delim>\n")
                        log_file.write("song saved: " + song.title + "\n")
                        print("song saved: ", song.title)
                        c += 1 
                    else:
                        log_file.write("SONG BROKEN: " + song.title + "\n")
                        print("SONG BROKEN: ", song.title)
            
            break 
    print ("Songs gathered: ", c)
    log_file.write("Songs gathered: " + str(c))
    log_file.close()
    lyrics_file.close()

def retrieve_lyrics(): 
    with open("lyrics_5kheaders.txt", "r", encoding='utf-8-sig', newline='') as file:
        contents = file.read()
        df = pd.DataFrame(contents.split('<delim>'),columns=['lyrics_col'])
    
    return df


def get_lyrics_individual(arr, k):  # Write lyrics of k songs by each artist in arr in individual txt files
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print (os.getcwd())

    parent_dir = os.path.dirname(os.path.abspath(__file__))
      
    log_file = open("log_rd.txt", "a", encoding="utf-8")

    c = 0 # Counter
    for name in arr:
        retries = 0 
        while retries < 3:
            try:
                print ("trying ", name)
                artist_obj = genius.search_artist(name, max_songs=k, sort='popularity')
            except Timeout as e:
                retries += 1
                print ("RETRYING: ", name)
                continue
            if artist_obj is not None:
                log_file.write(name + "\n")
                artist_path = os.path.join(parent_dir, name)
                os.mkdir(artist_path)
                for i in range(artist_obj.num_songs):

                    song = artist_obj.songs[i]

                    if song.lyrics is not None:
                        fname = song.title+".txt"
                        lyrics_file = open(os.path.join(artist_path, fname), "w", encoding="utf-8")
                        lyrics_file.write("<< {} - {} >> \n".format(name, song.title))
                        lyrics_file.write(song.lyrics)
                        log_file.write("song saved: " + song.title + "\n")
                        print("song saved: ", song.title)
                        c += 1 
                    else:
                        log_file.write("SONG BROKEN: " + song.title + "\n")
                        print("SONG BROKEN: ", song.title)
                    
                    lyrics_file.close()
            break 
    print ("Songs gathered: ", c)
    log_file.write("Songs gathered: " + str(c))
    log_file.close()
    

def main():
    print("LYRICS SCRAPER")
    #get_lyrics(artists, 35)
    #get_lyrics_individual(Rd_arr, 5)
    
  
if __name__ == '__main__':
    main()



