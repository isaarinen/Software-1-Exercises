class Publication:
    def __init__(self,name):
        self.name = name
    def print_information(self):
        print(f'\nName: {self.name}\n')
class Book(Publication):
    def __init__(self, name, author, page_count):
        self.name = name
        self.author = author
        self.page_count = page_count
    def print_information(self):
        print(f'\nName: {self.name}\nAuthor: {self.author}\nPage Count: {self.page_count}\n')
class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.name = name
        self.chief_editor = chief_editor
    def print_information(self):
        print(f'\nName: {self.name}\nChief Editor: {self.chief_editor}\n')

dd = Magazine('Donald Duck', 'Aki Hyyppä')
cn = Book('Compartment No. 6', 'Rosa Liksom', 192)
dd.print_information()
cn.print_information()