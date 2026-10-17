import config


def search(final, maxsearch):
    search_term = config.search.upper()

    if len(search_term) > int(maxsearch):
        print("too long of a search, will take years to finish")
        return

    index_position = final.find(search_term)
    if index_position == -1:
        print(
            f"'{config.search} is not in these digits of pi, "
            "please increase the pidigits to find it! "
            "(WARNING: THIS WILL TAKE A LONG TIME, POSSIBLY OVER 10 HOURS)"
        )
        return

    print(f"we found {config.search}")
    print(f"your phrase is at: {index_position}")

    start = max(0, index_position - 5)
    end = min(len(final), index_position + len(search_term) + 5)
    print(f"translating... {final[start:end]}...")
