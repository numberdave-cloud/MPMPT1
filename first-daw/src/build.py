# Rebuild first-daw/index.html from template.html, notes.json and the four OGG stems.
# Run from this src folder: python3 build.py
import base64, json
s = open('template.html').read()
for k in ['bass', 'drums', 'guitar', 'vocal']:
    s = s.replace(f'__B64_{k.upper()}__', base64.b64encode(open(k + '.ogg', 'rb').read()).decode())
s = s.replace('__NOTES__', json.dumps(json.load(open('notes.json'))))
open('../index.html', 'w').write(s)
