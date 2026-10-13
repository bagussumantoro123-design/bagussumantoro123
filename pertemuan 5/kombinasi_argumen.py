def get_full_name(first_name, last_name=""):
    return f"{first_name} {last_name}".strip()


res = get_full_name(
    "Darion",
    last_name="Mograine"
)

print(res)