_STORE = {
    "notes": []
}

def add_note(note: str):
    _STORE["notes"].append(note)

def list_notes():
    return list(_STORE["notes"])
