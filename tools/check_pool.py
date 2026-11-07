#!/usr/bin/env python3
"""Pool check: run before every push that touches the product list.
Flags duplicate codes, duplicate names and colour/size twins (same product family).
Exit code 1 if anything is found.  Usage: python3 tools/check_pool.py [--fix] [index.html]
--fix drops later twins (keeps the first of each family) in place."""
import re, sys, collections
COL = r'\b(black|white|grey|gray|silver|gold|rose gold|rose glow|pink|peony pink|blue|navy|green|red|purple|lilac|cream|natural|oak|walnut|beige|brown|yellow|orange|teal|mint|charcoal|clear|slate|warm black|sage|coral|copper|chrome|multi|multicolour|stainless steel|dial)\b'
# Model-level families the generic rule can't see (same product, different strap/model letter).
FAMILIES = [r'apple watch series 12', r'apple watch ultra 4', r'dolce gusto genio s', r'dolce gusto piccolo xs',
            r'x rocker arteon', r'tikkers teen series 13']
def family(name):
    b = name.lower().replace('\u2013', '-').replace('\u2014', '-')
    for f in FAMILIES:
        if re.search(f, b): return f
    b = re.sub(r'\s*-\s*[^-]*$', '', b) if re.search(r'\s?-\s', b) else b   # drop " - Colour/Size" suffix
    b = re.sub(COL, '', b)
    return re.sub(r'\s+', ' ', b).strip(' ,-&')
ITEM = re.compile(r'\{name:"((?:[^"\\]|\\.)*)",gbp:([\d.]+),code:"(\d+)",v:(\d)\},?\n')
def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    path = args[0] if args else 'index.html'
    s = open(path).read()
    i = s.index('const POOL = ['); j = s.index('];', i)
    block = s[i:j]
    items = ITEM.findall(block)
    seen_code, seen_fam, keep, problems = set(), {}, [], []
    for m in ITEM.finditer(block):
        n, p, c, v = m.groups(); f = family(n)
        if c in seen_code: problems.append(f'duplicate code {c}: {n}'); continue
        if f in seen_fam: problems.append(f'twin of "{seen_fam[f]}": {n}'); continue
        seen_code.add(c); seen_fam[f] = n; keep.append(m.group(0))
    print(f'{len(items)} items, {len(keep)} unique products, {len(problems)} problems')
    for x in problems: print('  -', x)
    if '--fix' in sys.argv and problems:
        nb = block[:block.index('[')+1] + '\n' + ''.join(k if k.endswith('\n') else k+'\n' for k in keep)
        nb = nb.rstrip(',\n') + '\n'
        open(path, 'w').write(s[:i] + nb + s[j:]); print('fixed', path)
    sys.exit(1 if problems and '--fix' not in sys.argv else 0)
main()
