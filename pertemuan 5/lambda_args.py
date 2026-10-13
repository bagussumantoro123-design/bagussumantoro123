def debug1(separator, *params):
    res = []

    for i in range(len(params)):
        res.append(f"param {i}: {params[i]}")

    return separator.join(res)


debug2 = lambda separator, *params: separator.join(
    [f"param {i}: {params[i]}" for i in range(len(params))]
)


res = debug1(
    ", ",
    "Darion Mograine",
    ["Highlord", "Horseman of the Ebon Blade", "Ashbringer"],
    True
)

print(res)

res = debug2(
    ", ",
    "Darion Mograine",
    ["Highlord", "Horseman of the Ebon Blade", "Ashbringer"],
    True
)

print(res)