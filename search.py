import config
## other files workign together

import sys
import time
from colorama import Fore, Style, init
import random
from rich.progress import Progress
from plyer import notification
from win11toast import toast
import winsound
## libraries

init(autoreset=True)

spinners = ["▖", "▘", "▝", "▗"] # depreciated, it was giving issues with being on the same line so now pifinding and translating no longer has a loading bar, only the search function does.
randomload = random.randint(1, 5)


def search(final, maxsearch):
    for x in range(randomload):
        with Progress() as p:
            t = p.add_task(f"searching... {x}", total=100)
            while not p.finished:
                p.update(t, advance=randomload)
                time.sleep(0.03)
        

        time.sleep(randomload)

    search_term = config.search.upper()

    if len(search_term) > int(maxsearch):
        print(f"\n{Fore.RED}{Style.BRIGHT}too long of a search, will take years to finish")
        winsound.Beep(frequency=500, duration=200)
        winsound.Beep(frequency=700, duration=300)
        return

    index_position = final.find(search_term)
    if index_position == -1:
        message = (
            f"{config.search} is not in these digits of pi. "
            "Please increase pidigits to find it! "
            "(WARNING: this may take a long time.)"
        )
        winsound.Beep(frequency=600, duration=300)
        winsound.Beep(frequency=500, duration=400)
        print(
            f"\n{Fore.RED}{Style.DIM}{message}"
        )
        notification.notify(
            title="Pi Splicer Results :(",
            message=message,
            timeout=0.01,
        )
        return

    start = max(0, index_position - 5)
    end = min(len(final), index_position + len(search_term) + 5)

    notification.notify(
        title = "Pi Splicer Results!",
        message = f"We found the phrase at {index_position}",
        timeout = 0.01,
    )
    winsound.Beep(frequency=1050, duration=300)
    winsound.Beep(frequency=1300, duration=400)

    print(f"\ntranslating... {final[start:end]}...")
    print(f"\nwe found {config.search}")
    print(f"\n{Fore.GREEN}{Style.BRIGHT}your phrase is at: {index_position}")
