import re

def block_to_block_type(markdown_text):
    match markdown_text[0]:
        case '#':
            return heading_check(markdown_text)
        case '`':
            return codeblock_check(markdown_text)
        case '>':
            return quoteblock_check(markdown_text)
        case '*' | '-':
            return unordered_list_check(markdown_text)
        case char if markdown_text[0] == '1':
            return ordered_list_check(markdown_text)
        case _:
            return "normal"
        
def heading_check(markdown_text):
    markdown_text = markdown_text.split()
    first_segment = markdown_text[0]
    if re.fullmatch(r'#{1,6}', first_segment) and len(markdown_text) > 1:
        return "heading"
    return False

def codeblock_check(markdown_text):
    if re.fullmatch(r"^```.*```$", markdown_text, re.DOTALL):
        return "codeblock"
    return False

def quoteblock_check(markdown_text):
    for line in markdown_text.split('\n'):
        if line[0] != '>':
            return False
    return "quoteblock"

def unordered_list_check(markdown_text):
    for line in markdown_text.split('\n'):
        if not bool (re.match(r"^(\* | - )", markdown_text)):
            return False
    return "unordered_list"

def ordered_list_check(markdown_text):
    for index, line in enumerate(markdown_text.split('\n'), start=1):
        if line[0:3] != f"{index}. ":
            return False
    return "ordered_list"
