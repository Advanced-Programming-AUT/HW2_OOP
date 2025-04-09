class Volume:
    def __init__(self, name, writer):
        self.name = name
        self.writer = writer
        self.borrowed_by = None

    def checkout(self, user_id):
        if self.borrowed_by is None:
            self.borrowed_by = user_id
            return True
        return False

    def give_back(self):
        if self.borrowed_by is not None:
            self.borrowed_by = None
            return True
        return False

    def display_info(self):
        status_text = "Available" if self.borrowed_by is None else "Borrowed"
        print(f"\t{self.name} by {self.writer} ({status_text})")


class Archive:
    def __init__(self):
        self.collection = {}

    def insert_volume(self, volume):
        self.collection[volume.name] = volume

    def loan_volume(self, name, user_id):
        volume = self.collection.get(name)
        return volume.checkout(user_id) if volume else False

    def recover_volume(self, name):
        volume = self.collection.get(name)
        return volume.give_back() if volume else False

    def list_volumes(self):
        for vol in self.collection.values():
            vol.display_info()


def interface():
    archive = Archive()

    while True:
        cmd = input().strip().split()
        if not cmd:
            continue
        action = cmd[0].upper()

        if action == 'ADD' and len(cmd) >= 3:
            title = cmd[1].strip('"')
            author = cmd[2].strip('"')
            archive.insert_volume(Volume(title, author))
            print(f"Added '{title}' by {author}")
        elif action == 'BORROW' and len(cmd) >= 2:
            title = cmd[1].strip('"')
            if archive.loan_volume(title, "user_1"):
                print(f"Borrowed '{title}'")
            else:
                print("Error: Book unavailable or not found.")
        elif action == 'RETURN' and len(cmd) >= 2:
            title = cmd[1].strip('"')
            if archive.recover_volume(title):
                print(f"Returned '{title}'")
            else:
                print("Error: Could not return the book.")
        elif action == 'SHOW':
            print("Available Books in Archive:")
            archive.list_volumes()
        elif action == 'EXIT':
            break
        else:
            print("""
Valid commands:
    ADD "title" "author"
    BORROW "title"
    RETURN "title"
    SHOW
    EXIT
""")


if __name__ == "__main__":
    interface()

