import webbrowser
import urllib.parse

print("----- compare Amazon and flipcart price -------")


product = input("Enter product name : ")


query = urllib.parse.quote_plus(product)


flipkart_url = f"https://www.flipkart.com/search?q={query}"
amazon_url = f"https://www.amazon.in/s?k={query}"


print("\nOpening Browser...")
print("Flipkart : " , flipkart_url) 
print("Amazon : " , amazon_url) 


webbrowser.open(flipkart_url)
webbrowser.open(amazon_url)