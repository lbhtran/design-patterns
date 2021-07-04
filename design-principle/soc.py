# SRP SOC
# each class should only take on a single responsibility


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        pass


if __name__ == "__main__":
    j = Journal()
    j.add_entry('Alex is great.')
    j.add_entry('Alex loves you.')

    print(f'Journal entries:\n{j}')