from PySide2.QtCore import QAbstractTableModel, QModelIndex, Qt

variant = []
headers = ["Button", "Title", "Artist", "Tool Button"]
BUTTON, TITLE, ARTIST, TOOLS = headers
class PlaylistTableModel(QAbstractTableModel):

    def __init__(self, filename=''):
        super().__init__()
        self.filename = filename
        self.total_songs = []

    def rowCount(self, index=QModelIndex()):
        return len(self.total_songs)

    def columnCount(self, index=QModelIndex()):
        return 4

    def data(self, index, role=Qt.DisplayRole):

        if not index.isValid() or \
                not (0 <= index.row() < len(self.total_songs)):
            return None

        songs = self.total_songs[index.row()]
        column = index.column()
        if role == Qt.DisplayRole:
            if column == BUTTON:
                return variant(songs.button)
            elif column == TITLE:
                return variant(songs.tile)
            elif column == ARTIST:
                return variant(songs.artist)
            elif column == TOOLS:
                return variant(songs.tools)

        elif role != Qt.DisplayRole:
            return None


