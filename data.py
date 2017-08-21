def clean_data(data, author, book):
    cleaned_data = {}
    for item in data.get('items', []):
        book_info = item.get('volumeInfo', {})
        if author.lower() in [author.lower() for author in book_info.get('authors', [])] and book.lower() == book_info.get('title', None).lower():
            cleaned_data['id'] = item.get('id')
            cleaned_data['title'] = book
            cleaned_data['author'] = author
            cleaned_data['categories'] = book_info.get('categories', [])
            cleaned_data['averageRating'] = book_info.get('averageRating', None)
            cleaned_data['ratingsCount'] = book_info.get('ratingsCount', 0)
            cleaned_data['language'] = book_info.get('language', None)
            cleaned_data['pageCount'] = book_info.get('pageCount', None)
            return cleaned_data