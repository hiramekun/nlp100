import xml.etree.ElementTree as ET

if __name__ == '__main__':
    root = ET.parse('nlp.txt.xml')
    for token in root.iterfind('./document/sentences/sentence/tokens/token[NER="PERSON"]'):
        print(token.findtext('word'))
