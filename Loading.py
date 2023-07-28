import sys
import time

#here is the animation
def Loading():
    LoadText = [
        "|",
        "/",
        "-",
        "\\",
        "|",
        "/",
        "-",
        "\\"
    ]

    WordToSay = "Working"

    done = False

    while done == False:
        for i in LoadText:
            sys.stdout.write(f'\r {WordToSay} {i}')
            time.sleep(0.4)

Loading()








