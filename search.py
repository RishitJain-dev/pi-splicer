import config
## other files workign together

import sys
import time
## libraries

def search(final, maxsearch):
    for x in range(len(config.search)):
        sys.stdout.write(f"\r[searching... stage {x}]")
        sys.stdout.flush()

        time.sleep(1)

    search_term = config.search.upper()

    if len(search_term) > int(maxsearch):
        print("\ntoo long of a search, will take years to finish")
        return

    index_position = final.find(search_term)
    if index_position == -1:
        print(
            f"\n{config.search} is not in these digits of pi. please increase the pidigits to find it! (WARNING: THIS WILL TAKE A LONG TIME, POSSIBLY OVER 10 HOURS)"
        )
        return

    print(f"\nwe found {config.search}")
    print(f"\nyour phrase is at: {index_position}")

    start = max(0, index_position - 5)
    end = min(len(final), index_position + len(search_term) + 5)
    print(f"\ntranslating... {final[start:end]}...")
