class RecordsFilter:
    def __init__(self, records):
        self.records = records

    def filter(self, **kwargs):
        result = self.records
        for key, value in kwargs.items():
            result = list(filter(lambda r: r.get(key) == value, result))
        return RecordsFilter(result)

    def __iter__(self):
        return iter(self.records)

    def __repr__(self):
        return repr(self.records)

    def first(self):
        return self.records[0] if self.records else None