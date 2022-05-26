class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)


d = Dictlist()
d['test'] = 1
d['test'] = 1
d['test'] = 1
d['other'] = 100

print(d)

for k, v in d.items():
    print(sum(v))