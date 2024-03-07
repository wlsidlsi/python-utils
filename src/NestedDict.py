class NestedDict:
    def __init__(self, data):
        self.data = data
    
    def __getitem__(self, key):
        keys = key.split('.')
        value = self.data
        for k in keys:
            value = value.get(k, None)
            if value is None:
                break
        return value
