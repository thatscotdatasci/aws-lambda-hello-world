class Message(object):

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def message(self):
        return f'Hello-World! Nice to meet you {self._first_name} {self._last_name}!'
