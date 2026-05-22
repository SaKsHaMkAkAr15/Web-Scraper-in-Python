import requests  
import csv  
from bs4 import BeautifulSoup  

response = requests.get("http://books.toscrape.com")

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

all_books = []

for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text
    rating = book.find("p", class_="star-rating")["class"][1]
    all_books.append({"Title": title, "Price": price, "Rating": rating})

with open("books.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Title", "Price", "Rating"])
    writer.writeheader()
    writer.writerows(all_books)

print(f"Scraped {len(all_books)} books successfully!")

print("\nBooks found:")
for book in all_books:
    print(f"{book['Title']} - {book['Price']} - {book['Rating']} stars")