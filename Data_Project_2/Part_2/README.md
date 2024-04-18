# Part 2: Discord Bot

## Overview
This project involves the development and deployment of an interactive Discord bot, CashierBot, designed to simulate cashier interactions within a Discord server. The goal is to create an engaging virtual shopping environment where users can manage a shopping cart, check product details, and interact dynamically using natural language commands. The seriousness of the project is demonstrated by how CashierBot handles data, performs remote retrieval and processing of requests and replies, and maintains a seamless and responsive interaction flow.

## Procedure

### System Setup and Configuration
- **Bot Registration and Setup**: Registered the bot with the Discord Developer Portal, configuring it with necessary permissions to interact within a server.
- **Environment Setup**: Set up environment variables to securely store sensitive API keys and bot tokens.

### Bot Implementation and Command Handling
- **Command Design**: Implemented various commands (`!products`, `!add`, `!remove`, `!cart`, `!checkout`, `!joke`) that allow users to interact with the bot as if it were a cashier.
- **Integration with External APIs**: Enabled the bot to fetch real-time data from external sources, allowing it to provide up-to-date product information and respond dynamically to user queries beyond predefined commands.

### User Interaction and Feedback
- **Direct Commands**: Configured the bot to allow users to perform specific shopping actions and receive immediate feedback.
- **Dynamic Interaction**: Utilized advanced AI-driven responses to ensure the bot can engage with users effectively, providing helpful instructions and entertaining content as needed.

### Testing and Reporting
- **Bot Testing**: Systematically tested all bot commands and interactions to ensure functionality and responsiveness.
- **Documentation Compilation**: Documented the bot's usage and operational elements in the `Discord_Bot_Documentation.md`, providing a clear guide for users and evaluators.

### Conclusion and Submission
- **Project Wrap-Up**: Reviewed the entire process to ensure that all benchmarks were met, including precise execution of bot commands and consistent user interaction.
- **Repository Management**: All code, documentation, and additional resources (such as `Direct_Message_Contents.csv`, `Direct_Message_Screenshot.png`, `Discord_Server_Contents.csv`, `Discord_Server_Screenshot.png`) were organized and uploaded for evaluation.

## Provided Files and Used Resources

### Provided Files
- `main.py`: Python file containing the bot's main execution logic and server interaction routines.
- `responses.py`: Python file defining all response logic for handling user commands and integrating with external APIs.
- `Direct_Message_Contents.csv`: CSV file containing the data recorded from the direct messages with the bot after its deployment.
- `Direct_Message_Screenshot.png`: PNG screenshot verifying the bot's functionality in direct messaging.
- `Discord_Server_Contents.csv`: CSV file containing the data recorded from interactions with the bot in the Discord server after its deployment.
- `Discord_Server_Screenshot.png`: PNG screenshot verifying the bot's active participation and responses on the server.
- `Discord_Bot_Documentation.md`: Markdown document detailing the bot's features, usage, and technical configuration.

### Used Resources
- **[Discord API](https://discord.com/developers/docs/reference)**: Used to connect and interact within the Discord server for the facilitation of real-time communication and bot commands.
- **[Fake Store API](https://fakestoreapi.com/)**: Utilized as an external data source for product information, and was previously used in Data Project 1.
- **[ICanHazDadJoke API](https://icanhazdadjoke.com/api)**: Integrated for providing entertaining content in response to user commands.
- **[Google Gemini API](https://ai.google.dev/gemini-api/docs)**: Leveraged for advanced AI and natural language processing capabilities to dynamically generate text responses.

## Invite Link
Experience interactive shopping with CashierBot on the Discord server: [Shop at the DS 2002 Store Server](https://discord.gg/6cR9HsYpjP).
