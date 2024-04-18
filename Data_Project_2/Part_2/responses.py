# Import necessary libraries and modules
import requests
import os
from dotenv import load_dotenv
from google.generativeai import GenerativeModel, configure
from random import choice

# Load the environment variables where the API key is securely stored
load_dotenv()

# Configure the API using the key from the environment variables
api_key = os.getenv('GOOGLE_API_KEY')
configure(api_key=api_key)

# Function to fetch all available products from Fake Store API
def fetch_product_data():
    # Makes an API request to retrieve products
    response = requests.get('https://fakestoreapi.com/products')
    # Check if the response is successful
    if response.status_code == 200:
        return response.json()  # Return JSON parsed list of products
    else:
        return []  # Return an empty list if the call fails

# Function to fetch a joke from the icanhazdadjoke API
def fetch_joke():
    # Headers to request a JSON response
    headers = {'Accept': 'application/json'}
    response = requests.get('https://icanhazdadjoke.com/', headers=headers)
    # Check if the response is successful
    if response.status_code == 200:
        return response.json()['joke']  # Extract and return the joke text
    else:
        return "Sorry, I can't think of a joke right now. Try again later!"

# Handle unrecognized commands by generating a dynamic response using a configured AI model
def handle_unknown_command(user_input):
    # Use the Gemini model to generate a response
    model = GenerativeModel('gemini-pro')
    # Define the context to guide the AI to respond like a cashier
    context = "You are a helpful cashier. Provide concise, polite responses to customer queries."
    # Construct the message with the context and the user's input
    prompt = f"{context}\nCustomer: {user_input}"
    # Generate content based on the constructed prompt
    response = model.generate_content(prompt)
    # Check if the response is successful and has content, otherwise provide a fallback message
    return response.text if response.text else "I'm a bit puzzled by that. Could you rephrase that or ask me something else?"

# Process user input and manage the shopping cart
def get_response(user_input: str, cart: dict) -> str:
    # Convert input to lowercase to standardize processing
    lowered = user_input.lower()
    # Greet the user in response to a greeting
    greetings = ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']
    if any(greet in lowered for greet in greetings):
        greeting_responses = [
            "Hello! I'm thrilled to assist you today. What can I help you with?",
            "Hi there! How can I make your shopping experience fantastic today?",
            "Greetings! Looking for something special today?",
            "Good day! What can I do for you on this fine day?",
            "Hey! Ready to find what you need? Just let me know how I can help!",
        ]
        return choice(greeting_responses)

    # Provide help instructions
    elif 'help' in lowered:
        return ("Here's what you can ask me to do:\n"
                "- `!products`: Display all available products\n"
                "- `!add [Product ID]`: Add a product to your cart\n"
                "- `!remove [Product ID]`: Remove a product from your cart\n"
                "- `!cart`: View the items in your cart\n"
                "- `!checkout`: Calculate your total cost including tax\n"
                "- `!joke`: Hear a funny joke\n"
                "- `? [Your message]`: Start a private chat with me")

    # List all products
    elif 'products' in lowered:
        products = fetch_product_data()
        # Check if any products are available
        if not products:
            return "It looks like we're currently out of stock. Please check back later!"
        product_list = '\n'.join([f'ID: {p["id"]}, Name: {p["title"]}, Price: ${p["price"]}' for p in products])
        # Return the product list to the user
        return f"Here's a list of all our fabulous products currently available. You can add items to your cart using their ID numbers:\n{product_list}"

    # Add a specified product to the cart
    elif 'add' in lowered:
        # Attempt to extract the product ID from the user input
        try:
            product_id = int(lowered.split()[-1])
        except ValueError:
            return "I'm sorry, but I couldn't quite catch that. Could you please provide a valid product ID?"
        products = fetch_product_data()
        # Find the product with the specified ID
        product = next((item for item in products if item['id'] == product_id), None)
        # If the product is found, add it to the cart
        if product:
            cart[product_id] = cart.get(product_id, 0) + 1
            return f"Great choice! I've added {product['title']} to your cart. Is there anything else I can assist you with?"
        else:
            # If the product is not found, return a message
            return "I'm sorry, but I couldn't find the product you're looking for. Would you like to browse our product list for something else?"

    # Remove a specified product from the cart
    elif 'remove' in lowered:
        # Attempt to extract the product ID from the user input
        try:
            product_id = int(lowered.split()[-1])
        except ValueError:
            return "I'm sorry, but I didn't catch that. Could you please provide a valid product ID to remove?"
        # Check if the product is in the cart and the quantity is greater than 0
        if product_id in cart and cart[product_id] > 0:
            cart[product_id] -= 1
            # Remove the product from the cart if the quantity becomes 0
            if cart[product_id] == 0:
                del cart[product_id]
            return "Got it! The product has been removed from your cart. Is there anything else you'd like to do?"
        else:
            # Return a message if the product is not in the cart
            return "I'm sorry, but it seems that product isn't in your cart. Would you like to check your cart contents or browse our products?"
        
    # Display the contents of the cart
    elif 'cart' in lowered:
        if not cart:
            return "It looks like your cart is empty. Would you like to add some products?"
        else:
            products = fetch_product_data()
            # Return the contents of the cart
            cart_contents = '\n'.join([f'Name: {next(item["title"] for item in products if item["id"] == id)}, Quantity: {quantity}' for id, quantity in cart.items()])
            return f"Here\'s what\'s in your cart:\n{cart_contents}\nIs there anything else you'd like to do?"

    # Checkout and calculate total cost including tax
    elif 'checkout' in lowered or 'check out' in lowered:
        if not cart:
            return "It seems your cart is empty. There's nothing to check out. Would you like to add some products?"
        else:
            products = fetch_product_data()
            subtotal = sum(next(item["price"] for item in products if item["id"] == id) * quantity for id, quantity in cart.items())
            tax = subtotal * 0.06  # Calculate retail tax at 6%
            total = subtotal + tax
            return f"Your subtotal is ${subtotal:.2f}. The tax on the items in your cart is ${tax:.2f}, making your total ${total:.2f}.\nIf you are ready to check out, please provide a form of payment."
    
    # Check if the user mentions a payment method for checkout purposes
    elif any(payment_method in lowered for payment_method in ['cash', 'money', 'dollar', 'credit card', 'debit card', '💳', '💵', '💰', '💸', '💰']):
        return "You are all good to go! Thank you for shopping at the DS 2002 Store, and have a great day!"

    # Fetch a joke
    elif 'joke' in lowered:
        return fetch_joke()

    # Provide AI-based response for unknown or unclear commands
    else:
        return handle_unknown_command(user_input)