# https://stackoverflow.com/questions/25226208/represent-directory-tree-as-json
# ..os.walk() and os.listdir(), ..
import os
import json

def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
    return d


pathDict=        path_to_dict('.')
pathDict=        path_to_dict('../.')
tmp = json.dumps(pathDict)
print tmp