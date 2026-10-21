# Rebuild first-daw/index.html from template.html, notes.json, the four OGG stems and the four easter egg OGGs.
# Run from this src folder: python3 build.py
import base64, json
s = open('template.html').read()
for k in ['bass', 'drums', 'guitar', 'vocal']:
    s = s.replace(f'__B64_{k.upper()}__', base64.b64encode(open(k + '.ogg', 'rb').read()).decode())
for k in ['anime', 'cage', 'jungle', 'kicks']:
    s = s.replace(f'__B64_EGG_{k.upper()}__', base64.b64encode(open('egg_' + k + '.ogg', 'rb').read()).decode())
s = s.replace('__NOTES__', json.dumps(json.load(open('notes.json'))))
open('../index.html', 'w').write(s)
