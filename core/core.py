from core.encrypt import *
from core.decrypt import *
from core.alloc import *

def generator(template="",shellcode_path="",seciton="",alloc="",encrypt="",output=""):

    shellcode = load_file(shellcode_path)
    tables_code = eval("generate_"+encrypt + "(shellcode, seciton)")
    module =__import__('templates.'+template)
    c_code = eval('module.'+template+'.template.get()')
    alloc_code = eval(alloc+"()")
    c_code = c_code.replace("<TABLES>", tables_code)
    c_code = c_code.replace("<ALLOC>", alloc_code)
    c_code = c_code.replace("<DECODE>", get_decode(encrypt))

    return c_code
