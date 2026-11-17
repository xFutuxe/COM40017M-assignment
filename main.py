import subprocess, os, time
import album, storage
from rich.console import Console
from rich.table import Table

data = storage.StorageManager()
console = Console()
view_album_table = Table(title="Albums")

def main_menu():
    subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
    console.print("[blue underline bold]Welcome to the Album Log Tracker!")
    print("Please choose an option:")
    print("1. Add a new album")
    print("2. View all albums")
    print("3. Search logged collection")
    print("4. Exit")

    input_choice = input("Enter your choice (1-4): ").strip()
    if input_choice == "1":
        add_album()
    elif input_choice == "2":
        view_album()
    elif input_choice == "3":
        search_album()
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
    try:
        artist = input("Artist Name: ")
        albumName = input("Album Name:")
        releaseYear = int(input("Release Year: "))
        rating = int(input("Rating (1-5): "))
        genre = input("Genre: ")
        notes = input("Notes: ")
        data.add_album(album.Album(albumName, artist, releaseYear, rating, genre, notes))
    except ValueError as error:
        print(f"Error: {error}. Please try again.")
        time.sleep(2)
        add_album()

def search_album():
    subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
    query = console.input("[bold]Search for an album, artist or genre: ")
    if not query:
        subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
        console.print("Search Query cannot be empty")
        time.sleep(2)
        search_album()
    search_results = data.search_results(query)
    if not search_results:
        console.print("No results found, adjust your query")
        time.sleep(2)
        search_album()
    results_table = Table(title="Search Results")
    results_table.add_column("Artist")
    results_table.add_column("Album")
    results_table.add_column("Release Year")
    results_table.add_column("Genre")
    results_table.add_column("Rating")
    results_table.add_column("Date Added")
    for item in search_results:
        results_table.add_row(f"{item.artist}", f"{item.title}", f"{item.year}", f"{item.genre}", f"{item.rating}/5", f"{item.date_added}")

    console.print(results_table)
    input("Press enter to return to the main menu")

def view_album():
    subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
    print("Loading albums")
    time.sleep(2)
    subprocess.run("clear" if os.name == "posix" else "cls", shell=True)

    albums = data.load()

    if not albums:
        print("No albums found, add some!")
    else:
        view_album_table.add_column("Artist")
        view_album_table.add_column("Album")
        view_album_table.add_column("Release Year")
        view_album_table.add_column("Rating")
        view_album_table.add_column("Date Added")
        for index, album in enumerate(albums, start=1):
            view_album_table.add_row(f"{album.artist}", f"{album.title}", f"{album.year}", f"{album.rating}/5", f"{album.date_added}")
    console.print(view_album_table)
    input("Press enter to return to the main menu")
if __name__ == "__main__":
    while True:
        main_menu()