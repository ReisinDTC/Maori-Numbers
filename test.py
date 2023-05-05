"""Component 1 - Welcome v1
"""

symbol = "*"
text = "Welcome"
sides = symbol * 3

formatted_text = f"{sides} {text} {sides}"
top_bottom = symbol * len(formatted_text)

print(top_bottom)
print(formatted_text)
print(top_bottom)