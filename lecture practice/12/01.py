def index(keys, values, match):
    return {x: [y for y in values if match(x, y)] for x in keys}