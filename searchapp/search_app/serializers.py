class AutocompleteSerializer:
    def __init__(self, hits):
        self.hits = hits

    def sort(self):
        self.hits = sorted(self.hits, key=lambda t: t._source.text1)
        self.hits = sorted(
            self.hits,
            key=lambda h: h['_score'],
            reverse=True)

    @property
    def data(self):
        self.sort()
        data = [r._source.to_dict() for r in self.hits]
        return data
