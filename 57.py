import re
import xml.etree.ElementTree as ET

pattern = re.compile(r'^\((.*?)\s(.*)\)$')


def parse_and_extract_np(string, list_np):
    match = pattern.match(string)
    tag = match.group(1)
    value = match.group(2)

    depth = 0
    chunk = ''
    words = []
    for c in value:
        if c == '(':
            chunk += c
            depth += 1
        elif c == ')':
            chunk += c
            depth -= 1
            if depth == 0:
                words.append(parse_and_extract_np(chunk, list_np))
                chunk = ''
        else:
            if not (depth == 0 and c == ' '):
                chunk += c
    if chunk != '':
        words.append(chunk)

    result = ' '.join(words)
    if tag == 'NP':
        list_np.append(result)
    return result


if __name__ == '__main__':
    root = ET.parse('nlp.txt.xml')
    for parse in root.iterfind('./document/sentences/sentence/parse'):
        result = []
        parse_and_extract_np(parse.text.strip(), result)
        print(*result, sep='\n')
