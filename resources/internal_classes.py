import operator

from resources.db_handler import get_album_data_from_db, get_artist_data_from_db


class SongData:

    """This class save data for song playing"""

    def __init__(self, data, category_list, artist_data, album_data):
        #Todo: check category list
        self._data = data
        self._tracks = []
        self._filenames = []
        self._artists = []
        self._song_names = []
        self._durations = []
        self._url = []
        self._album_data = album_data
        self._artist_data = artist_data
        self._category_list = category_list

    def _check_id_in_list(self, id, this_list, name):

        if id in this_list:
            id_pos = this_list.index(id)
            return name[id_pos]
        else:
            return None

    def run_parser(self, id_data, dbname):
        list_data= self._data_parser(self._data, self._category_list, id_data, dbname)

        return list_data

    def _data_parser(self, data, category_list, id_data, dbname):
        tracks = []
        id_artist_list, id_album_list, artists_name_list, album_name_list = id_data
        for item in data:
            artist_id = item[4]

            res = self._check_id_in_list(artist_id, id_artist_list, artists_name_list)
            if res:
                artist_name = res
            else:
                artist_name = get_artist_data_from_db(artist_id, dbname=dbname)[0][1]
                id_artist_list.append(artist_id)
                artists_name_list.append(artist_name)

            album_id = item[3]
            res = self._check_id_in_list(album_id, id_album_list, album_name_list)
            if res:
                album_name = res
            else:
                album_name = get_album_data_from_db(album_id, dbname=dbname)[0][2]
                id_album_list.append(album_id)
                album_name_list.append(album_name)

            self._artists.append(artist_name)
            self._song_names.append(item[2])

            tracks.append([artist_name, item[2],
                           album_name, item[5]])

            self._filenames.append(item[5])
            self._url.append(item[6])
            self._durations.append(item[7])


        self.set_tracks(tracks)

        list_id_data = id_artist_list, id_album_list, artists_name_list, album_name_list

        return list_id_data

    def set_tracks(self, tracks):
        self._tracks = tracks

    def url(self):
        return self._url

    def split_filename(self,filename):
        only_file_name = []
        for item in filename:
            only_file_name.append(item.split('/')[-1])

        return only_file_name

    def sort_data(self, main_list='filename', order='Descending'):
        "Sort list for artist or songname"
        #todo sorting is working only for artist
        filename = self.split_filename(self._filenames)
        list1 = filename
        list2 = self._song_names

        if order == 'AscendingOrder':
            list2.sort()
            junk, self._song_names, self._filenames, self._artists, \
                self._tracks, self._url = [list(x) for x in zip(*sorted(zip(list1, list2, self._filenames, self._artists,
                                              self._tracks, self._url), key=operator.itemgetter(0), reverse=True))]
        else:
            junk, self._song_names, self._filenames, self._artists,\
                    self._tracks, self._url = [list(x) for x in zip(*sorted(zip(list1, list2, self._filenames, self._artists,
                                                                              self._tracks, self._url),
                                                                          key=operator.itemgetter(0)))]

    def song_names(self):
        return self._song_names

    def tracks(self):
        return self._tracks

    def artists(self):
        return self._artists

    def duration(self):
        return self._durations

    def filenames(self):
        return self._filenames

