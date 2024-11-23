'''8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.'''

'''Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number
of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album'''


def make_album(artist_name, album_title, num_tracks=None):
    """Build a dictionary describing a music album."""
    album = {
        'artist': artist_name.title(),
        'title': album_title.title()
    }
    if num_tracks:  # Add the number of tracks if provided
        album['tracks'] = num_tracks
    return album

# Create albums with and without the number of tracks
album1 = make_album("taylor swift", "1989")
album2 = make_album("ed sheeran", "divide", 16)
album3 = make_album("beyoncé", "renaissance")

# Print each album dictionary
print(album1)
print(album2)
print(album3)
