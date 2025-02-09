import json
import os

NOTES_FILE = "notes.json"

def load_notes():
    """Lädt Notizen aus der Datei oder erstellt eine leere Liste"""
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    return []

def save_notes(notes):
    """Speichert die Notizen in einer Datei."""
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note(title, content):
    """Fügt eine neue Notiz hinzu."""
    notes = load_notes()
    notes.append({"title": title, "content": content})
    save_notes(notes)
    print(f"Notiz '{title}' wurde hinzugefügt!")

def show_notes():
    """Zeigt alle Notizen an."""
    notes = load_notes()
    if not notes:
        print("Keine Notizen vorhanden.")
        return
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note['title']} - {note['content']}")

def search_notes(keyword):
    """Sucht nach einer Notiz anhand eines Stichworts."""
    notes = load_notes()
    found_notes = [note for note in notes if keyword.lower() in note["title"].lower()]
    if found_notes:
        for note in found_notes:
            print("Keine passende Notiz gefunden.")

def delete_note(title):
    """Löscht eine Notiz nach Titel."""
note = load_notes()
new_notes = [note for note in notes if keyword.lower() in note["title"].lower()]
if len(new_notes) < len(notes):
    save_notes(new_notes)
    print(f"Notiz '{title}' wurde gelöscht!")
else:
    print(f"Keine Notiz mit dem Titel '{title}' gefunden.")
    


