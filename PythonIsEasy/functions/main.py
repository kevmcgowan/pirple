# This is a list of musicians, music genre, track and track duration

Artist = "Neol Gallagher"
Genre = "Rock"
Track = "A Simple Game of Genius"
DurationInSeconds, seconds  = 438, "seconds"

Artist = "Ed Sheeran"
Genre = "Pop"
Track = "The a Team"
DurationInSeconds, seconds = 256, "seconds"

Artist = "David Bowie"
Genre = "Pop"
Track = "Absolute Beginners"
DurationInSeconds, seconds = 338, "seconds"

Artist = "The Pretty Reckless"
Genre = "Rock"
Track = "Absolution"
DurationInSeconds, seconds = 274, "seconds"

Artist = "Status Quo"
Genre = "Rock"
Track = "Accident Prone"
DurationInSeconds, seconds = 304, "seconds"

Artist = "Motorhead"
Genre = "Heavy Metal"
Track = "Ace of Spades"
DurationInSeconds, seconds = 323, "seconds"

Artist = "Iron Maiden"
Genre = "Heavy Metal"
Track = "Aces High - Live"
DurationInSeconds, seconds = 278, "seconds"

"""From this point on I have changed to the single line format.
This makes the output more readable."""

Artist, Genre, Track, DurationInSeconds, seconds = "Goldfrapp", "Pop", "A&E", 199, "seconds"

Artist, Genre, Track, DurationInSeconds, seconds = "Kid Rock", "Rock", "Abortion", 270, "seconds"

Artist, Genre, Track, DurationInSeconds, seconds = "Nirvana", "Grunge", "About a Girl", 171, "seconds"


# Function definitions
def artist():
    return "Iron Maiden"  # Replace with the desired artist

def genre():
    return "Heavy Metal"  # Replace with the desired genre

def track():
    return "Aces High - Live"  # Replace with the desired track

# Extra credit function that returns a boolean value
def isFavorite():
    return True  # Replace with the desired boolean value


# Testing the functions
print(artist())
print(genre())
print(track())
print(isFavorite())
