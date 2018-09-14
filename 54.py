import xml.etree.ElementTree as ET

if __name__ == '__main__':
    root = ET.parse('nlp.txt.xml')
    for token in root.iter('token'):
        word = token.findtext('word')
        lemma = token.findtext('lemma')
        pos = token.findtext('POS')
        print(f'{word}\t{lemma}\t{pos}')
