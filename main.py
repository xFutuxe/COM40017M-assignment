import subprocess, os, time, readline
import album, storage
from datetime import date
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box

data = storage.StorageManager()
console = Console()
view_album_table = Table(title="Albums")

def main_menu():

    menu_title = Markdown("# Album Log Tracker", justify="left")
    menu_desc = Markdown("## Please choose an option")
    console.clear()
    console.print(Panel.fit(menu_title, border_style="white", box=box.ROUNDED))
    console.print(menu_desc)
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
        console.clear()
        print("Invalid choice. Please try again.")
        time.sleep(2)
        main_menu()

def add_album():
    console.clear()

    # TODO: Need to create a method to vaidate each input as the user progresses instead of just at the end. 
    try:
        artist = input("Artist Name: ")
        albumName = input("Album Name:")
        releaseYear = int(input("Release Year: "))
        rating = int(input("Rating (1-5): "))
        genre = input("Genre: ")
        notes = input("Notes: ")
        console.clear()

        console.print(f"[bold white underline] ----- Logging an album at {date.today()} -----")
        console.print(f"Artist Name: {artist}")
        console.print(f"Album Name: {albumName}")
        console.print(f"Release Year: {releaseYear}")
        console.print(f"Rating: {rating}/5")
        console.print(f"Genre: {genre}")
        console.print(f"Notes: {notes} \n")

        usrConfirm = console.input(f"[bold cyan] Confirm? (y/n): ")

        if usrConfirm == "y":
            with console.status("Logging album...", spinner="dots"):
                time.sleep(3)
                data.add_album(album.Album(albumName, artist, releaseYear, rating, genre, notes)) 
                # TODO: should i check if it's been saved?

            console.clear()
            console.print("[bold underline cyan] Album logged!")
            logAnother = console.input("Would you like to log another album? (y/n)")
            if logAnother.strip().lower() == "y":
                add_album()
            else:
                return
        elif usrConfirm == "n": # TODO: If user selects no, don't reset form on function call, take the user back with all inputs filled so they can edit it quicker
            add_album()      
        # TODO: if usrConfirm is anything else, let the user know  
    except ValueError as error:
        print(f"Error: {error}. Please try again.")
        time.sleep(2)
        add_album()

def search_album():
    console.clear()
    query = console.input("[bold]Search for an album, artist or genre: ")
    if not query:
        console.clear()
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
    console.clear()
    console.print("Loading albums")
    time.sleep(2)
    console.clear()

    albums = data.load()

    if not albums:
        console.print("No albums found, add some!")
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
