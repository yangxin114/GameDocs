import os, glob, re

disk_files = set()
for f in glob.glob('assets/images/**/*', recursive=True):
    if os.path.isfile(f):
        disk_files.add(f.replace(os.sep, '/'))

broken = []
ok_count = 0

for html_file in glob.glob('games/**/*.html', recursive=True):
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    srcs = re.findall(r'src="../../([^"]+)"', content)

    for src in srcs:
        resolved = os.path.normpath(os.path.join(os.path.dirname(html_file), '../../' + src))
        resolved = resolved.replace(os.sep, '/')

        if os.path.exists(resolved):
            ok_count += 1
        else:
            broken.append((html_file, src, resolved))

print(f'OK: {ok_count}')
print(f'BROKEN: {len(broken)}')
for bf in broken:
    print(f'  {bf[0]}: {bf[1]} -> {bf[2]}')
