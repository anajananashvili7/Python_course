import requests


url = "https://fakestoreapi.com/products"
response = requests.get(url)

if response.status_code == 200:
    products = response.json()  

    prices = [product["price"] for product in products]
    max_price = max(prices)
    min_price = min(prices)
    avg_price = sum(prices) / len(prices)

    print(f"Maximum price: {max_price}")
    print(f"Minimum price: {min_price}")
    print(f"Average price: {avg_price:.2f}")

    
    categories = sorted(set(product["category"] for product in products))
    print(f"Categories: {categories}")

 
    title_id_list = sorted(
        [{"title": product["title"], "id": product["id"]} for product in products],
        key=lambda x: x["title"]
    )
    print("Products sorted by title:")
    for item in title_id_list:
        print(f"{item['id']}: {item['title']}")

    
    ratings_sorted = sorted(
        [{"id": product["id"], "title": product["title"], "rate": product["rating"]["rate"]} for product in products],
        key=lambda x: x["rate"]
    )
    print("Ratings sorted by rate:")
    for rating in ratings_sorted:
        print(f"Rate: {rating['rate']}, Title: {rating['title']}, ID: {rating['id']}")

else:
    print(f"Failed to fetch products. Status code: {response.status_code}")
