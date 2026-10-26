import base64, json, pathlib
here = pathlib.Path(__file__).parent
tpl = (here/'template.html').read_text()
notes = json.loads((here/'notes.json').read_text())
b64 = base64.b64encode((here/'bass_loop.ogg').read_bytes()).decode()
out = tpl.replace('__NOTES__', json.dumps(notes)).replace('__B64_LOOP__', b64)
(here.parent/'index.html').write_text(out)
print('index.html', (here.parent/'index.html').stat().st_size, 'bytes')
