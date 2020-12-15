import argparse
import sys
from core.core import *
from core.lib import *

logo = '''

  ____       _                   _ _                       _        ____      _   
 / ___|  ___| |__  _ __ ___   __| (_)_ __   __ _  ___ _ __( )___   / ___|__ _| |_ 
 \___ \ / __| '_ \| '__/ _ \ / _` | | '_ \ / _` |/ _ \ '__|// __| | |   / _` | __|
  ___) | (__| | | | | | (_) | (_| | | | | | (_| |  __/ |    \__ \ | |__| (_| | |_ 
 |____/ \___|_| |_|_|  \___/ \__,_|_|_| |_|\__, |\___|_|    |___/  \____\__,_|\__|
                                           |___/         
           Schrodinger'sCat is a Shellcode antivirus evasion framework 
                                v1.0 stable!
                        author idiotc4t@xxSec Lab!                         
'''
print(logo)
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--template', type=str, choices=template_choices,default="tpl_earlybird", help='PE file modification mode Default:tpl_test')
    parser.add_argument('-f', '--file' ,type=str, default="data.db", help='Input shellcode file to be processed')
    parser.add_argument('-s', '--section', type=str, default=".text", help='Shellcode offsets the segment stored in the table Default:.text')
    parser.add_argument('-a', '--alloc', type=str, choices=alloc_choices,default="alloc_virtualalloc",help='Application method of memory Default:alloc_virtualalloc')
    parser.add_argument('-o', '--output', type=str, default="output.exe", help='Output file name Default:output.exe')
    parser.add_argument('-p', '--platform', type=str, choices=['x86','x64'],default="x86", help='Compiling platform Default:x86')
    parser.add_argument('-l', '--list', type=str,default="",choices=['alloc','template'], help='list template or alloc')
    parser.add_argument('-opt', '--options', type=str,default="O3", help='GCC compilation options Default:O3')

    args = parser.parse_args()
    if args.list != "":
        list(args.list)
        sys.exit();

    if args.file == "":
        print("[-] Not found this file")
        parser.print_help()
        sys.exit()

    if check_alloc(args.alloc) == False:
        print("[-] Not found this alloc mode")
        parser.print_help()
        sys.exit()

    if check_template(args.template) == False:
        print("[-] Not found this template")
        parser.print_help()
        sys.exit()

    print("[+] Generate temporary source code")
    c_code = generator(args.template, args.file, args.section,args.alloc, args.output)
    print("[+] Write temp source file ./temp/temp.cpp")
    write_file(c_code,'temp/temp.cpp')

    if check_compiler('i686-w64-mingw32-gcc')== False:
        print('[-] No cross-compiler detected. Try: apt-get install mingw-w64')
        sys.exit()

    print("[+] Compiling temporary source code ./temp/temp.cpp")

    if args.platform == 'x64':
        os.system("i686-w64-mingw32-gcc -mwindows ./temp/temp.cpp -o %s -static -%s" % (args.output ,args.options))
    else:
        os.system("i686-w64-mingw32-gcc -mwindows -lws2_32 ./temp/temp.cpp -o ./temp/%s -static -%s" % (args.output , args.options))
    print("[+] Compiled and output the file %s" % args.output)
