class ListProcess:
    item_list = []

    @staticmethod
    def get_list(n):
        _l = list(range(n))  # _l = list(range(2, n, 5))
        print("ListProcess Sınıfından get_list methodundayım...")
        print(_l)

    @staticmethod
    def sort_list(_l):
        _l.sort(key=lambda key: key["id"])
        return _l

    @classmethod
    def create_list(cls):
        cls.item_list.append(dict(
            id=1,
            name="Adana"
        ))
        cls.item_list.append(dict(
            id=10,
            name="Balıkesir"
        ))
        cls.item_list.append(dict(
            id=16,
            name="Bursa"
        ))
        cls.item_list.append(dict(
            id=58,
            name="Sivas"
        ))
        cls.item_list.append(dict(
            id=6,
            name="Ankara"
        ))
        cls.item_list.append(dict(
            id=34,
            name="İstanbul"
        ))
        return cls.item_list
