import pathlib
import re

cwd = r"docs"

regex_link = re.compile(r"[^\]]\[([^\s\]]+)\]:\s*(.*)")
regex_text_ref = re.compile(r"\[.*?\]\[([^\s\]]+)\]")


def check_refs(md, unused=True, unreferenced=True):
    print(md)
    with open(md, 'r', encoding="utf-8") as fp:
        contents = fp.read()
    all_links = [{'ref': x.group(1), 'link': x.group(2)} for x in regex_link.finditer(contents)]

    if unused:
        for item in all_links:
            if f"][{item['ref']}]" not in contents:
                print("  ", item['ref'], "is not used in", md)

    if unreferenced:
        all_refs = [x['ref'] for x in all_links]
        for i in regex_text_ref.finditer(contents):
            ref = i.group(1)
            if ref not in all_refs:
                print("  ", ref, "is unreferenced in", md)


def main(cwd):
    for md in pathlib.Path(cwd).glob("**/*.md"):
        check_refs(str(md), True, True)
        print("---")


if __name__ == '__main__':
    main(cwd)
