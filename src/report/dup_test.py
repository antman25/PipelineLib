#!/usr/bin/python3
import json

def dict_raise_on_duplicates(ordered_pairs):
    """Reject duplicate keys."""
    print ("--------OrderPairs------")
    print (ordered_pairs)
    d = {}
    for k, v in ordered_pairs:
        if k in d:
           raise ValueError("duplicate key: %r" % (k,))
        else:
           d[k] = v
    return d


if __name__ == '__main__':
    f =  open('dupe.json')
    d = f.read()
    json.loads(d, object_pairs_hook=dict_raise_on_duplicates)
    
