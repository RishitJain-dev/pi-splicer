import config
## other files workign together

import sys
import time
from colorama import Fore, Style, init
import random
from rich.progress import Progress
import pyfiglet
## libraries

init(autoreset=True)

spinners = ["▖", "▘", "▝", "▗"]

def search(final, maxsearch):
    banner = pyfiglet.figlet_format("PI    SPLICER", font="bulbhead")
    print(f"{Fore.CYAN}{Style.BRIGHT}{banner}")

    for x in range(randomload):
        with Progress() as p:
            t = p.add_task(f"searching...", total=100)
            while not p.finished:
                p.update(t, advance=1)
                time.sleep(0.03)
        

        randomload = random.uniform(1, 5)
        time.sleep(randomload)

    search_term = config.search.upper()

    if len(search_term) > int(maxsearch):
        print("\ntoo long of a search, will take years to finish")
        return

    index_position = final.find(search_term)
    if index_position == -1:
        print(
            f"\n{Fore.RED}{Style.DIM}{config.search} is not in these digits of pi. please increase the pidigits to find it! (WARNING: THIS WILL TAKE A LONG TIME, POSSIBLY OVER 10 HOURS)"
        )
        return

    start = max(0, index_position - 5)
    end = min(len(final), index_position + len(search_term) + 5)

    print(f"\ntranslating... {final[start:end]}...")
    print(f"\nwe found {config.search}")
    print(f"\n{Fore.GREEN}{Style.BRIGHT}your phrase is at: {index_position}")
