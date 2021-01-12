import random
from core.lib import *

def generate_random_dict_table():
    random_dict_table = [i for i in range(256)]
    random.shuffle(random_dict_table)
    return random_dict_table

def generate_offset_table(shellcode,random_dict_table):
    offset_table = []
    for i in range(len(shellcode)):
        for p in range(len(random_dict_table)):
            if ord(chr(random_dict_table[p])) == ord(chr(shellcode[i])):
                offset_table.append(p)
                break
    return offset_table

def generate_section(compile_section):
    c_section_code = '''

    __attribute__((section("<SECTION>"))) <RANDOM_DICT_TABLE>
    __attribute__((section("<SECTION>"))) <OFFSET_TABLE>
    '''
    return c_section_code.replace("<SECTION>",compile_section)

def generate_offset(shellcode,compile_section):

    random_dict_table = generate_random_dict_table()
    offset_table = generate_offset_table(shellcode,random_dict_table)
    section_code = generate_section(compile_section)

    random_dict_str = "DWORD random_dict_table[]=" + str(random_dict_table).replace('[', '{').replace(']', '}') + ";"
    offset_tables_str = "DWORD offset_table[]=" + str(offset_table).replace('[', '{').replace(']', '}') + ";"

    c_tables_code = section_code.replace("<SECTION>", compile_section)
    c_tables_code = c_tables_code.replace("<RANDOM_DICT_TABLE>", random_dict_str)
    c_tables_code = c_tables_code.replace("<OFFSET_TABLE>", offset_tables_str)
    return c_tables_code

def generate_aes(shellcode,compile_section):
    pass