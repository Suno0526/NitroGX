import requests as Requests
import time as Time
import subprocess as Sub
import os as OS

Filed = OS.path.join(OS.path.dirname(__file__), "Codes.txt")

print("Need help? Follow this tutorial: https://www.youtube.com/watch?v=yWqqMp6ca30&t=246s")

Numero = int(input("Enter the number of Opera GX Nitro codes: "))
PartnerID = str(input("Enter your Partner ID: "))

with open("Codes.txt", "w") as File:
    for _ in range(Numero):
        URI = "https://api.discord.gx.games/v1/direct-fulfillment"
        Data = {"partnerUserId": PartnerID}

        Resp = Requests.post(URI, json = Data)
        try:
            JSON = Resp.json()

        except Requests.exceptions.JSONDecodeError:
            print("ERROR: The server didn't return a valid JSON response. Please try again later.")
            continue

        Token = JSON.get('token', '').replace("'", "")
        File.write(f"https://discord.com/billing/partner-promotions/1180231712274387115/{Token}\n\n")

        Time.sleep(0.05)

        print(f"https://discord.com/billing/partner-promotions/1180231712274387115/{Token}")


Time.sleep(1.5)
Sub.Popen(["notepad.exe", "Codes.txt"])
