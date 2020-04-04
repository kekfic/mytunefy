#!/usr/bin/env python3

import os
import sys
import platform
import pprint
import logzero
from logzero import logger as log

# from spotdl import __version__
# from spotdl import const
# from spotdl import handle
# from spotdl import internals
# from spotdl import spotify_tools
# from spotdl import youtube_tools
# from spotdl import downloader

#import __version__
import const
import handle
import internals
import spotify_tools
import youtube_tools
import downloader


# My modification
from PySide2.QtWidgets import QMainWindow, QApplication
from window_handler import MainWin
#--

def debug_sys_info():
    log.debug("Python version: {}".format(sys.version))
    log.debug("Platform: {}".format(platform.platform()))
    log.debug(pprint.pformat(const.args.__dict__))


def match_args():
    if const.args.song:
        for track in const.args.song:
            track_dl = downloader.Downloader(raw_song=track)
            track_dl.download_single()
    elif const.args.list:
        if const.args.write_m3u:
            youtube_tools.generate_m3u(
                track_file=const.args.list
            )
        else:
            list_dl = downloader.ListDownloader(
                tracks_file=const.args.list,
                skip_file=const.args.skip,
                write_successful_file=const.args.write_successful,
            )
            list_dl.download_list()
    elif const.args.playlist:
        spotify_tools.write_playlist(
            playlist_url=const.args.playlist, text_file=const.args.write_to
        )
    elif const.args.album:
        spotify_tools.write_album(
            album_url=const.args.album, text_file=const.args.write_to
        )
    elif const.args.all_albums:
        spotify_tools.write_all_albums_from_artist(
            artist_url=const.args.all_albums, text_file=const.args.write_to
        )
    elif const.args.username:
        spotify_tools.write_user_playlist(
            username=const.args.username, text_file=const.args.write_to
        )


def main():
    const.args = handle.get_arguments()

    internals.filter_path(const.args.folder)
    youtube_tools.set_api_key()

    logzero.setup_default_logger(formatter=const._formatter, level=const.args.log_level)

    try:
        match_args()
        # actually we don't necessarily need this, but yeah...
        # explicit is better than implicit!
        sys.exit(0)

    except KeyboardInterrupt as e:
        log.exception(e)
        sys.exit(3)


if __name__ == "__main__":
    #main()
    if getattr(sys, 'frozen', False):
        CurrentPath = sys._MEIPASS
        # If it's not use the path we're on now
    else:
        CurrentPath = os.path.dirname(__file__)
        
    app = QApplication(sys.argv)

    gui=MainWin() 
    gui.mainwindow.show() 
    #gui.mainwindow.showMaximized()
    
    sys.exit(app.exec_())
