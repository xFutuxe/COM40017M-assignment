import os, json
from album import Album

class StorageManager():

    filepath = "data.json"
    albums = []

    def add_album(self, album):
        if not isinstance(album, Album):
            raise TypeError("Expected an Album object")
        self.albums.append(album)
        self.save()


    def load(self):
        if not os.path.exists(self.filepath): # If file does not exist
            self.albums = []
            return self.albums

        try:
            with open(self.filepath, encoding="utf-8") as file:
                raw_data = json.load(file)
                self.albums = [Album.from_dict(item) for item in raw_data]
        except Exception as e:
            print(f"An unexpected error has occured while reading file '{self.filepath}': {e}")
        return self.albums

    def save(self):
        data = [album.to_dict() for album in self.albums]
        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
