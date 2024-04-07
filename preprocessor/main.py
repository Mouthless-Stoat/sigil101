import json
import sys
import re
from pathlib import Path


def processSection(section, processor):
    if "Chapter" in section:
        section["Chapter"]["content"] = processor(
            section["Chapter"]["content"],  # content of the chapter
            section["Chapter"]["source_path"],  # where the file is
            snipProcess,
            filenameProcess,
            captionProcess,
        )
        if "sub_items" in section["Chapter"]:
            for subChapter in section["Chapter"]["sub_items"]:
                processSection(subChapter, processor)


def processor(content, path, *funcs):
    for func in funcs:
        content = func(content, path)
    return content


def snipProcess(content, path):
    for match in re.findall(r"@@snip\s([^:\n\s\t\r]+)(?::(.+))?", content):
        anchorName = match[1] if match[1] != "" else "main"
        p = (Path(__file__).parent / f"../src/{path}" / ".." / match[0]).resolve()
        with p.open() as f:
            file = ""
            inAnchor = False
            for line in f.read().strip().split("\n"):
                if f"START: {anchorName}" in line:
                    inAnchor = True
                    continue
                elif f"END: {anchorName}" in line:
                    inAnchor = False
                    continue
                if "START" in line or "END" in line:
                    continue

                file += f"{'' if inAnchor else '~'}{line}\n"
            file = file.strip("\n")
        content = content.replace(
            f"@@snip {match[0]}{f':{match[1]}' if match[1] != '' else ''}",
            file,
        )
    return content


def filenameProcess(content, path):
    for match in re.findall(r"@f\s(.+)", content):
        content = content.replace(
            f"@f {match}",
            f"Filename: {match}",
        )
    return content


def captionProcess(content, path):
    for match in re.findall(r"@c\s(.+)", content):
        content = content.replace(
            f"@c {match}",
            f'<span class="caption">{match}</span>',
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
