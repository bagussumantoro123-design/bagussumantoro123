def debug3(separator, **params):
    res = []

    for key in params:
        res.append(f"{key}: {params[key]}")

    return separator.join(res)


debug4 = lambda separator, **params: separator.join(
    [f"{key}: {params[key]}" for key in params]
)


res = debug3(
    ", ",
    name="Darion Mograine",
    occupations=[
        "Highlord",
        "Horseman of the Ebon Blade",
        "Ashbringer"
    ],
    active=True
)

print(res)

res = debug4(
    ", ",
    name="Darion Mograine",
    occupations=[
        "Highlord",
        "Horseman of the Ebon Blade",
        "Ashbringer"
    ],
    active=True
)

print(res)