"""

"""

def make_album(artist_name, album_title, tracks=""):
    album={"Title": album_title, "Artist": artist_name}
    if tracks:
        album["Tracks"] = tracks
    return album

print(make_album("Gorillaz", "Gorillaz", "15"))
print(make_album("Gorillaz", "Demon Dayz"))
print(make_album("Gorillaz", "Plastic Beach", "16"))
print(make_album("Gorillaz", "The Fall", "15"))
print(make_album("Gorillaz", "Humanz", "20"))
