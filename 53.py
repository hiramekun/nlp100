import xml.etree.ElementTree as ET

if __name__ == '__main__':
    root = ET.parse('nlp.txt.xml')
    print('\n'.join([word.text for word in root.iter('word')]))
