# Discord Bot Documentation

## Overview

CashierBot is a helpful Discord bot designed to simulate a shopping experience in a Discord server environment. It acts as a virtual cashier, allowing users to browse products, manage a shopping cart, and simulate a checkout process including tax calculations.

## Features

CashierBot offers the following features:

- **Product Browsing**: Users can view a list of available products.
- **Shopping Cart Management**: Users can add and remove products from a personal shopping cart.
- **Checkout Simulation**: Users can simulate the checkout process, including tax calculation.
- **Payment Simulation**: After checking out, users can 'pay' using various indicated methods, clearing their cart upon completion.
- **Joke Telling**: CashierBot can tell jokes on demand for a lighter interaction experience.
- **Private Conversations**: Users can initiate private conversations with CashierBot for help or to discuss sensitive matters.

## Commands

CashierBot responds to the following commands:

- `!products`: Displays all available products.
- `!add [Product ID]`: Adds a specified product to the user's cart.
- `!remove [Product ID]`: Removes a specified product from the user's cart.
- `!cart`: Shows the current contents of the user's cart.
- `!checkout`: Calculates the total cost of the items in the cart, including tax.
- `!joke`: CashierBot tells a random joke.
- `? [Your message]`: Starts a private conversation with CashierBot.

## Setup and Operation

### Setting Up Your Environment

1. **Environment Variables**
   - Ensure your `.env` file is set up with `DISCORD_TOKEN` for Discord bot authentication and `GOOGLE_API_KEY` for accessing the generative AI functionalities.

2. **Dependencies**
   - Discord.py library for bot integration.
   - Requests library for HTTP requests.
   - Google Generative AI for handling unknown commands.

### Running the Bot

To run CashierBot, execute the `main.py` script. This script initializes the bot and connects it to your Discord server using the token provided in the `.env` file.

## Technical Details

- **Language**: Python 3.9+
- **Libraries**: discord.py, requests, google-generativeai
- **APIs**: Fake Store API for product data, icanhazdadjoke API for jokes, Google's Generative AI for dynamic responses.

## Troubleshooting

- **Bot does not respond**: Ensure the bot's token is correctly set in `.env` and that it has the necessary permissions in your Discord server.
- **Commands not recognized**: Verify that commands are typed correctly and follow the format described in the commands section.
- **API failure**: Check console logs for any error messages that might indicate what went wrong during an API request.
