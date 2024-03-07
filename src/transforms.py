'''
Function to find all a key with a specific name
and perform a transform that is defined by the caller.
'''
def find_and_transform(data: dict, key_path: str, transform):
    keys = key_path.split('.')
    parent = data
    for k in keys:
        value = parent.get(k, None)
        if k == keys[-1]:
            parent[k] = transform(value)
            break
        if value is None:
            break
        parent = value
    return data