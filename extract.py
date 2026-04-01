import re, glob, json

all_words = {}
for file in glob.glob('unit*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'const vocabularyData\s*=\s*\[(.*?)\];', content, re.DOTALL)
    if match:
        arr = match.group(1)
        words = re.findall(r'word:\s*\"([^\"]+)\"', arr)
        all_words[file] = words

print(json.dumps(all_words, indent=2))
