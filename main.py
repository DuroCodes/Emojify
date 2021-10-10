from re import search
import json

with open('emojis.json') as f: REPLACE = json.load(f)

def toEmoji(text):
  for key, value in REPLACE.items(): text = text.replace(key, value)
  return text

def toString(text):
  for key, value in REPLACE.items(): text = text.replace(value, key)
  return text

INPUT = input("Input text/emoji: ").lower()

if search("[a-z]", INPUT): print(toEmoji(INPUT))
else: print(toString(INPUT))