profile = {
    "id": 2,
    "name": "mario",
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"),
    "is_female": False,
}

print("id:", profile["id"])
# output ➜ id: 2

print("name:", profile.get("name"))
# output ➜ name: mario