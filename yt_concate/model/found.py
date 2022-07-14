class Found:
    def __init__(self, yt, caption):
        self.yt = yt
        self.url = yt.url
        self.caption = caption['text']
        self.start_time = caption['start']
        self.end_time = caption['start'] + caption['duration']

    def __str__(self):
        return '<Found(yt= ' + str(self.yt) + ')>'

    def __repr__(self):
        content = ':'.join([
            'yt= ' + str(self.yt),
            'caption= ' + str(self.caption),
            'start_time= ' + str(self.start_time),
            'end_time= ' + str(self.end_time),
        ])
        return '<found ' + content + '>'
