def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

print(make_album('Nirvana', 'Nevermind'))
print(make_album('Pink Floyd', 'The Dark Side of the Moon', tracks=10))
print(make_album('The Beatles', 'Abbey Road'))