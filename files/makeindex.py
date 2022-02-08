#!/usr/bin/env python3

import os
import sys
from pathlib import Path
from jinja2 import Template


tpl = '''
<!doctype html>
<head>
<title>{{title}}</title>
</head>
<body>
<h1>Files</h1>

<ul>
    {%- for subdir in subdirs -%}
    <li>
      <a href="{{ subdir }}/index.html">{{ subdir }}</a>
    </li>
    {%- endfor %}
    {%- for file in files -%}
    <li>
      <a href="{{ file }}">{{ file }}</a>
    </li>
    {%- endfor %}
</ul>

</body>
</html>
'''


def _make_list(root, name='main'):
    subdirs = []
    files = []
    for it in root.iterdir():
        if it.is_dir() and (it / 'index.html').is_file():
            subdirs.append(it.name)
        elif it.is_file():
            files.append(it.name)
    return sorted(subdirs), sorted(files)


def make_index(path):
    path = path.resolve()
    with (path / 'index.html').open('wt') as out:
        subdirs, files = _make_list(path)
        out.write(Template(tpl).render(**locals()))


if __name__ == '__main__':
    try:
        path = Path(sys.argv[1])
    except IndexError:
        path = Path().cwd()
    make_index(path)
