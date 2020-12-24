from core.lib import *
from core.encrypt import *
from core.alloc import *
from templates import *

def generator(template="",shellcode_path="",seciton="",alloc="",output=""):

    tables_code = generate_tables(shellcode_path, seciton);

    module =__import__('templates.'+template)

    c_code = eval('module.'+template+'.template.get()')

    alloc_code = eval(alloc+"()")
    c_code = c_code.replace("<TABLES>",tables_code)
    c_code = c_code.replace("<ALLOC>", alloc_code)
    return c_code
