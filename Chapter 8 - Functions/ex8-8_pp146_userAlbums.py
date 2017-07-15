"""

"""

def make_album(artist_name, album_title, tracks=""):
    album={"Title": album_title, "Artist": artist_name}
    if tracks:
        album["Tracks"] = tracks
    return album

while True:
    print("Enter 'q' at any time to quit!")
    artist = input("Artist Name: ")
    if artist == "q":
        break
    title = input("Album Title: ")
    if title == "q":
        break
    tracks = input("Number of Tracks (optional): ")
    if tracks == "q":
        break
    print()
    print("Creating album.")
    print("Creating album..")
    print("Creating album...")
    print()
    print(make_album(artist, title, tracks))
