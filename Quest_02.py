# Initial dictionary definition
books = {
    'book1': {
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'year': 1925
    },
    'book2': {
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'year': 1960
    },
    'book3': {
        'title': '1984',
        'author': 'George Orwell',
        'year': 1949
    }
}

# a) Add a new book to the dictionary:
new_book = {
    'title': 'The Catcher in the Rye',
    'author': 'J.D. Salinger',
    'year': 1951
}

books['book4'] = new_book
print(books)

# b) Print the titles of all the books:
for book_key in books:
    print(books[book_key]['title'])

# c) Determine the book with the earliest publication year and print its title and author:
earliest_year = float('inf')
earliest_book = None

for book_key, book_info in books.items():
    if book_info['year'] < earliest_year:
        earliest_year = book_info['year']
        earliest_book = book_info

print("Earliest book:")
print("Title:", earliest_book['title'])
print("Author:", earliest_book['author'])
