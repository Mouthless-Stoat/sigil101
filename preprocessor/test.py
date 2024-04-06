import json
import sys
import re
from pathlib import Path


def processSection(section, processor):
    if "Chapter" in section:
        section["Chapter"]["content"] = processor(
            section["Chapter"]["content"], section["Chapter"]["source_path"]
        )
        if "sub_items" in section["Chapter"]:
            for subChapter in section["Chapter"]["sub_items"]:
                processSection(subChapter, processor)


def processor(content, path):
    for match in re.findall(r"{{#snip\s(?:(.*?)\s)?(.+?)(?::(\w+?))?}}", content):
        path = Path(__file__).parent / f"../src/{path}" / ".." / match[1]
        with path.open() as f:
            file = ""
            inAnchor = False
            for line in f.read().strip().split("\n"):
                if match[1] == "":
                    file += line + "\n"
                    continue
                if f"START: {match[2]}" in line:
                    inAnchor = True
                    continue
                elif f"END: {match[2]}" in line:
                    inAnchor = False
                    continue
                file += f"{'' if inAnchor else '//' if match[0] == '' else match[0]}{line}\n"
            file = file.strip("\n")
        content = content.replace(
            f"{{{{#snip {f'{match[0]} ' if match[0] != '' else ''}{match[1]}{f':{match[2]}' if match[2] != '' else ''}}}}}",
            file,
        )
    return content


if __name__ == "__main__":
    if len(sys.argv) > 1:  # we check if we received any argument
        if sys.argv[1] == "supports":
            # then we are good to return an exit status code of 0, since the other argument will just be the renderer's name
            sys.exit(0)

    # load both the context and the book representations from stdin
    context, book = json.load(sys.stdin)
    # and now, we can just modify the content of the first chapter
    for section in book["sections"]:
        processSection(section, processor)
    # we are done with the book's modification, we can just print it to stdout,
    print(json.dumps(book))
