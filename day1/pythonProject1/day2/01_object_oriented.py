class Album:
    def __init__(self, artist, name, songs):
        self.artist = artist
        self.name = name
        self.songs = songs

    def __str__(self):
        return f"{self.artist} / {self.name}"

    def __iter__(self):
        return (
            f"{index + 1} {name}" for index, name in
            enumerate(self.songs)
        ).__iter__()


album = Album(
    "Guns & Roses",
    "Appetite for Destruction",
    [
        "Welcome To The Jungle",
        "It's So Easy"
     ]
)

print(album)



###
for song in album:
    print(song)

#######################

# i = range(10).__iter__()
# while True:
#     try:
#         next_value = i.__next__()
#         print(next_value.__str__())
#     except StopIteration:
#         break
