import subprocess, os, time
import album, storage

data = storage.StorageManager()

def main_menu():
    subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
    print("Welcome to the Album Log Tracker!")
    print("Please choose an option:")
    print("1. Add a new album")
    print("2. View all albums")
    print("3. Search for an album")
    print("4. Exit")

    input_choice = input("Enter your choice (1-4): ").strip()
    if input_choice == "1":
        add_album()
    elif input_choice == "2":
        view_albums()
    elif input_choice == "3":
        pass
    elif input_choice == "4":
        print("Exiting the Album Log Tracker. Goodbye!")
        exit()
    else:
        subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
        print("Invalid choice. Please try again.")
        time.sleep(2)
        main_menu()

def add_album():
    subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
    artist = input("Artist Name: ")
    albumName = input("Album Name:")
    releaseYear = int(input("Release Year: "))
    rating = int(input("Rating (1-5): "))
    genre = input("Genre: ")
    notes = input("Notes: ")

    data.add_album(album.Album(artist, albumName, releaseYear, rating, genre, notes))

def view_albums():
    print("loading albums")
    time.sleep(2)
    subprocess.run("clear" if os.name == "posix" else "cls", shell=True)

    albums = data.load()

    if not albums:
        print("No albums found, add some!")
    else:
        print("---Your Albums---")
        for index, album in enumerate(albums, start=1):
            print(f"{index}. {album}")

    input("Press enter to return to the main menu")
if __name__ == "__main__":
    while True:
        main_menu()