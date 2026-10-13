text = """
hello python
"""

text = """
hello python
"""
print(f"--{text.lstrip()}--")
# output ↓
#
# --hello python
# --

text = """
hello python
"""

print(f"--{text.rstrip()}--")
# output ↓
#
# --
# hello python--

text = """
hello python
"""

print(f"--{text.strip()}--")
# output ➜ --hello python--