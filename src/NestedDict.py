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

    def __setitem__(self, key, new_value):
        keys = key.split('.')
        target = self.data
        for k in keys[:-1]:
            target = target.setdefault(k, {})
        target[keys[-1]] = new_value

    def mutate_at(self, key_path, mutation_fn):
        keys = key_path.split('.')
        target = self.data
        for k in keys[:-1]:
            target = target.get(k)
            if target is None:
                return  # Exit gracefully if path doesn't exist
        last_key = keys[-1]
        if last_key in target:
            target[last_key] = mutation_fn(target[last_key])
