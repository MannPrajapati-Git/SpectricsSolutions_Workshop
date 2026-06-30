# 19. Given a list of books with duplicates, create a dictionary that counts how many times each book appears.

books = ["book1", "book2", "book3", "book1", "book2"]
book_count = {}

for book in books:
    if book in book_count:
        book_count[book] += 1
    else:
        book_count[book] = 1

print(book_count)