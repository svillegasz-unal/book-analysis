import json
from operator import itemgetter

with open('data.txt', 'r') as file:
    data = json.load(file)

cleaned_data = [item for item in data if item is not None and item.get('averageRating')]
sorted_data = sorted(cleaned_data, key=itemgetter('ratingsCount'), reverse = True)
print(sorted_data)