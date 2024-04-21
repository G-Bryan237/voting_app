import os

class Sessio:
    ENDPOINT = "/sessions"

    def __init__(self, id_session=None, path=None) -> None:
        self.id_session = id_session
        self.path = path

    @property
    def sessionname(self):
        return os.path.basename(self.path) if self.path else ''