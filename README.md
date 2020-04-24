# This is MyTuneFy

Contributions are very much appreciated!

* 

* 

* a

* Python 3.3+ and Windows.

## Dependency

youtube-dl\
spotdl ---> modified for handling youtube cache download error:\
at youtube_tools, line 193\

`
with youtube_dl.YoutubeDL(pafy.g.def_ydl_opts) as ydl:
    ydl.cache.remove()
                 `\
                 
pafy\
sqlalchemy\
PySide2\

## Code conventions

* Maximum line length is 80 characters

* Follow the line-spacing style that is already in place.

* Ensure all functions and classes have a PEP257 compliant docstring and the
code is PEP8 compliant.
