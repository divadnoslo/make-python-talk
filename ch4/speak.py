import os

def speak(inp):
    os.system(f'gtts-cli --nocheck "{inp}" | mpg123 -q -')