#! python3
# ch6bullet.py will perform the bullet adding to wiki markup project in ch.6
# this adds wikipedia bullet points to the start of each line of text in the clipboard

import pyperclip

text = pyperclip.paste()

text_list = text.split('\n')

new_string = []
for line in text_list:
	if not line.isspace():
		new_string.append("* " + line)


pyperclip.copy("\n".join(new_string))