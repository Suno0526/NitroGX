# Suno's Nitro Generator
This Python script is designed to generate and write Discord Nitro codes using the new Opera GX Nitro exploit.

# Prerequisites
Before you can use this script, you need to have Python installed on your machine. You also need to install the `requests` library, which can be done using pip:
```cd
pip install requests
```

# Usage
To use this script, follow these steps:
1. Fork or download the repository
2. Install the code onto your machine
3. Run the Python file
The script will then start generating and writing Discord Nitro codes to the "Codes.txt" file. It will do this 100 times, pausing for as long as it needs between each request.

# Understanding the Script
The script works by sending a POST request to the Discord API endpoint "https://api.discord.gx.games/v1/direct-fulfillment". The body of the request is a JSON object containing a single key-value pair: "partnerUserId" with a specific value.
The response from the API is JSON object, from which the script extracts a "token" value. This token is then written to the "Codes.txt" file, along with a URL that includes the token.
The script then pauses for as long as it needs before repeating the process. This delay is to prevent the script from overloading the Discord API with too many requests in a short period of time.

# Note
This script is intended for education purposes only. Misuse of this script may violate Discord's Terms of Service. Always use scripts responsibly and ethically.
