import config
import pifinder
import splicer
import search

pifinder.getpi()
final = splicer.splice(config.pidigits, pifinder.pistring)
search.search(final, config.maxsearch)