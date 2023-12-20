import requests as Requests
import time as Time
import subprocess as Sub
import os as OS

Filed = OS.path.join(OS.path.dirname(__file__), "Codes.txt")
Numero = int(input("Enter the number of Opera GX Nitro codes: "))

with open("Codes.txt", "w") as File:
    for _ in range(Numero):
        URI = "https://api.discord.gx.games/v1/direct-fulfillment"
        Data = {"partnerUserId": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"}

        Resp = Requests.post(URI, json=Data)
        JSON = Resp.json()

        Token = JSON.get('token', '').replace("'", "")
        File.write(f"https://discord.com/billing/partner-promotions/1180231712274387115/{Token}\n\n")

        Time.sleep(0.05)

        print(f"https://discord.com/billing/partner-promotions/1180231712274387115/{Token}")


Sub.Popen(["notepad.exe", Filed])
