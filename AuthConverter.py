'''
Code to covert the authentication into a varialble
'''


from pathlib import Path
import re

collection = Path('/Users/{INumber}/Library/CloudStorage/OneDrive-SAPSE/Documents/A - CWS/APIs/cws-collections/CWS APIs')

# This pattern:
# 1. Captures indentation (group 1)
# 2. Captures "auth:bearer {" (group 2)
# 3. Matches EVERYTHING until the closing brace at the same indent (group 3)

pattern = re.compile(
    r'(^[ \t]*)(auth:bearer\s*\{)([\s\S]*?^\1\})',
    re.MULTILINE
)

#\1 → here this refers to a previously captured group (group 1 in this example), which stores the indentation (spaces/tabs) from the start of the block.

for bru_file in collection.rglob("*.bru"):
    text = bru_file.read_text(encoding="utf-8")

    # Replace content inside braces with the fixed text
    new_text = re.sub(
        pattern, 
        lambda m: f"{m.group(1)}{m.group(2)}\n{m.group(1)}  token:{{{{jwt}}}} \n{m.group(1)}}}",
        text
    )
# This defines an inline function that takes m (a match object from re.sub) and returns a formatted replacement string for each regex match.

    bru_file.write_text(new_text, encoding="utf-8")
    print("Updated", bru_file)
    
