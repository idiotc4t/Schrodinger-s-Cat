import sys
import os
import core.alloc

alloc_choices =[]
template_choices =[]


for i in dir(core.alloc):
    if 'alloc_' in str(i):
        alloc_choices.append(i)

filelist = os.listdir("templates")
for filename in filelist:
    if 'tpl_' in filename:
        template_choices.append(filename.replace('.py',''))


def load_file(file_path):
    try:
        file = open(file_path,"rb+").read()
    except Exception as e:
        print(str(e))
        sys.exit()
    return file

def write_file(file_context,output):
    open(output,'w+').write(file_context)

def list(some_module):
    if some_module == "template":
        for i in template_choices:
            print(i)

    elif some_module == "alloc":
        for i in alloc_choices:
            print(i)
    else:
        print("There is no such option")
        sys.eixt()
