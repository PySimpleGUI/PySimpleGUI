readfile = lambda fpath: open(fpath, 'r', encoding='utf-8').read()
writefile = lambda fpath, x: open(fpath, 'w', encoding='utf-8').write(x)

from collections import Counter
asd = Counter(readfile('LoG_call_ref.json').split('\n'))
import pdb; pdb.set_trace();
