text = "my NAME is najrudeen"
print(text.upper())

new_text = text.lower()
print(new_text)

new_text = text.title()
print(new_text)

text1 = "              this ia a line    "
new_text = text1.strip()
print(new_text)

new_text = text1.lstrip()
print(new_text)

new_text = text.find("najrudeen")
print(new_text)

new_text = text.replace("najru", "ajru")
print(new_text.title())

new_text = "Richa" in text
print(new_text)

new_text = "najrudeen" in text
print(new_text)
