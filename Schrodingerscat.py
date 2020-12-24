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
                                v1.1 stable!
                        author idiotc4t@QuasarSec Lab!                         
'''
print(logo)
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--template', type=str, choices=template_choices,default="tpl_earlybird", help='C language source code template. Default:tpl_earlybird')
    parser.add_argument('-f', '--file' ,type=str, default="", help='Input shellcode file to be processed.')
    parser.add_argument('-s', '--section', type=str, default=".text", help='The offset table is compiled into the named code segment Default:.text')
    parser.add_argument('-a', '--alloc', type=str, choices=alloc_choices,default="alloc_virtualalloc",help='Restore shellcode temporary storage allocation. Default:alloc_virtualalloc')
    parser.add_argument('-o', '--output', type=str, default="output.exe", help='Output file name. Default:output.exe')
    parser.add_argument('-p', '--platform', type=str, choices=['x86','x64'],default="x86", help='Compiling platform Default:x86')
    parser.add_argument('-l', '--list', type=str,default="",choices=['alloc','template'], help='list template or alloc.')
    parser.add_argument('-opt', '--options', type=str,default="O3", help='GCC compilation options. Default:O3')

    args = parser.parse_args()
    if args.list != "":
        list(args.list)
        sys.exit();

    if args.file == "":
        print("[-] Not found this file")
        parser.print_help()
        sys.exit()

    if os.path.exists('./output') == False:
        os.mkdir('./output')

    c_code = generator(args.template, args.file, args.section,args.alloc, args.output)
    if c_code != "":
        print("[+] Generate temporary source code")
    else:
        print("[-] Generate temporary source code failed")
        sys.exit()

    write_file(c_code,'output/temp.cpp')
    print("[+] Write temp source file ./output/temp.cpp")
    if check_compiler('i686-w64-mingw32-gcc')== False:
        print('[-] No cross-compiler detected. Try: apt-get install mingw-w64')
        sys.exit()

    print("[+] Compiling temporary source code ./output/temp.cpp")

    if args.platform == 'x64':
        os.system("x86_64-w64-mingw32-gcc -mwindows ./output/temp.cpp -o ./output/%s -static -%s" % (args.output ,args.options))
        print("[+] Compiled and output the file ./temp/%s" % args.output)
    else:
        os.system("i686-w64-mingw32-gcc -mwindows -lws2_32 ./output/temp.cpp -o ./output/%s -static -%s" % (args.output , args.options))
        print("[+] Compiled and output the file ./output/%s" % args.output)
