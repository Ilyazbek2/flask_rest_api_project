
DATA = []

def init_db(initial_records=None):
    global DATA
    if initial_records:
        DATA = initial_records.copy()

def get_all_books():
    return DATA

def add_book(book):
    DATA.append(book)
    return book
