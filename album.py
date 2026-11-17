from datetime import date

class Album: # A single album item

    min_rating = int(1)
    max_rating = int(5)
    current_year = date.today().year

    def __init__(self, title, artist, year, rating, genre="", notes="", date_added=None):
        # Validate inputs
        if not title.strip():
            raise ValueError("Title cannot be empty.")
        if not artist.strip():
            raise ValueError("Artist cannot be empty.")
        if not (self.min_rating <= rating <= self.max_rating) and isinstance(rating, int):
            raise ValueError(f"Rating must be between {self.min_rating} and {self.max_rating}.")
        if not isinstance (year, int):
            raise TypeError("Year must be a integer.")
        if not (1900 <= year <= self.current_year): # Check if the year is suitable.
            raise ValueError(f"Year must be between 1900 and {self.current_year}")
        if not genre.strip():
            raise ValueError("Genre cannot be empty")
        self.title = title.strip()
        self.artist = artist.strip()
        self.year = int(year)
        self.rating = int(rating)
        self.genre = genre.strip()
        self.notes = notes # Notes will be optional
        self.date_added = date.today()

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.year} - {self.rating}/5)"

    def to_dict(self):
        return {
            "title": self.title,
            "artist": self.artist,
            "year": self.year,
            "rating": self.rating,
            "genre": self.genre,
            "notes": self.notes,
            "Date Logged": self.date_added,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            artist=data["artist"],
            year=data["year"],
            rating=data["rating"],
            genre=data["genre"],
            notes=data["notes"],
            date_added=data["Date Logged"]
        )


    def matches_query(self, query):
        cleanQuery = query.strip().lower()
        return (
            cleanQuery in self.title.lower()
            or cleanQuery in self.artist.lower()
            or cleanQuery in self.genre.lower()
        )