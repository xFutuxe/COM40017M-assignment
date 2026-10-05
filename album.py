class Album: # A single album item

    min_rating = 1
    max_rating = 5

    def __init__(self, title, artist, year, rating, genre="", notes=""):
        if not title.strip():
            raise ValueError("Title cannot be empty.")
        if not (self.min_rating <= rating <= self.max_rating):
            raise ValueError(f"Rating must be between {self.min_rating} and {self.max_rating}.")
        if not year.strip().isdigit() or len(year.strip()) != 4:
            raise ValueError("Year must be a 4-digit number.")
        self.title = title.strip()
        self.artist = artist.strip()
        self.year = int(year.strip())
        self.rating = rating
        self.notes = notes
        self.genre = genre
