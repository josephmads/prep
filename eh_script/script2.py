import json
import re

with open("programs.txt", "r") as fin:
    input = fin.read()

pattern = re.compile(r"(\w+):")
output = json.loads(pattern.sub(r'"\1":', input))
print(output)
