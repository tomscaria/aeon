import hashlib, glob, re, os
os.chdir('/home/runner/work/aeon/aeon')
parts = []
for f in ['aeon.yml','skills.json']:
    with open(f,'rb') as fh:
        parts.append(hashlib.sha1(fh.read()).hexdigest()+'  '+f)
buf = []
for f in sorted(glob.glob('skills/*/SKILL.md')):
    with open(f,'r',encoding='utf-8',errors='ignore') as fh:
        text = fh.read()
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            buf.append(f+': '+line)
    for line in text.splitlines():
        if re.match(r'^(depends_on:|- skill:|consume:|parallel:|trigger:)', line):
            buf.append(line)
    refs = sorted(set(re.findall(r'memory/(?:topics|state)/[a-zA-Z0-9_.-]+', text)))
    buf.extend(refs)
h = hashlib.sha1('\n'.join(buf).encode()).hexdigest()
parts.append(h+'  -')
out = '\n'.join(parts)
final = hashlib.sha1(out.encode()).hexdigest()
print('FINGERPRINT:', final)
with open('.sg-fingerprint.txt','w') as fh:
    fh.write(final)
