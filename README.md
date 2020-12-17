# Schrodinger's Cat
Schrodinger'sCat is a Shellcode antivirus evasion framework

## Technical principle
Please visit my blog
https://idiotc4t.com/
## How to usa

```
└─$ python3 Schrodingerscat.py -f 64.bin -t tpl_nttestalert -a alloc_calloc -p x64 


  ____       _                   _ _                       _        ____      _   
 / ___|  ___| |__  _ __ ___   __| (_)_ __   __ _  ___ _ __( )___   / ___|__ _| |_ 
 \___ \ / __| '_ \| '__/ _ \ / _` | | '_ \ / _` |/ _ \ '__|// __| | |   / _` | __|
  ___) | (__| | | | | | (_) | (_| | | | | | (_| |  __/ |    \__ \ | |__| (_| | |_ 
 |____/ \___|_| |_|_|  \___/ \__,_|_|_| |_|\__, |\___|_|    |___/  \____\__,_|\__|
                                           |___/         
           Schrodinger'sCat is a Shellcode antivirus evasion framework 
                                v1.0 stable!
                        author idiotc4t@xxSec Lab!                         

[+] Generate temporary source code
[+] Write temp source file ./temp/temp.cpp
[+] Compiling temporary source code ./temp/temp.cpp
[+] Compiled and output the file ./temp/output.exe
```

## HELP
```bash 
└─$ python3 Schrodingerscat.py -h
  ____       _                   _ _                       _        ____      _   
 / ___|  ___| |__  _ __ ___   __| (_)_ __   __ _  ___ _ __( )___   / ___|__ _| |_ 
 \___ \ / __| '_ \| '__/ _ \ / _` | | '_ \ / _` |/ _ \ '__|// __| | |   / _` | __|
  ___) | (__| | | | | | (_) | (_| | | | | | (_| |  __/ |    \__ \ | |__| (_| | |_ 
 |____/ \___|_| |_|_|  \___/ \__,_|_|_| |_|\__, |\___|_|    |___/  \____\__,_|\__|
                                           |___/         
           Schrodinger'sCat is a Shellcode antivirus evasion framework 
                                v1.0 stable!
                        author idiotc4t@xxSec Lab!                         

usage: Schrodingerscat.py [-h] [-t {tpl_nttestalert,tpl_earlybird,tpl_setcontext,tpl_ptrrun,tpl_createremotethread}] [-f FILE] [-s SECTION]
                          [-a {alloc_calloc,alloc_malloc,alloc_maping,alloc_virtualalloc}] [-o OUTPUT] [-p {x86,x64}] [-l {alloc,template}]
                          [-opt OPTIONS]

optional arguments:
  -h, --help            show this help message and exit
  -t {tpl_nttestalert,tpl_earlybird,tpl_setcontext,tpl_ptrrun,tpl_createremotethread}, --template {tpl_nttestalert,tpl_earlybird,tpl_setcontext,tpl_ptrrun,tpl_createremotethread}
                        C language source code template. Default:tpl_earlybird
  -f FILE, --file FILE  Input shellcode file to be processed.
  -s SECTION, --section SECTION
                        The offset table is compiled into the named code segment Default:.text
  -a {alloc_calloc,alloc_malloc,alloc_maping,alloc_virtualalloc}, --alloc {alloc_calloc,alloc_malloc,alloc_maping,alloc_virtualalloc}
                        Restore shellcode temporary storage allocation. Default:alloc_virtualalloc
  -o OUTPUT, --output OUTPUT
                        Output file name. Default:output.exe
  -p {x86,x64}, --platform {x86,x64}
                        Compiling platform Default:x86
  -l {alloc,template}, --list {alloc,template}
                        list template or alloc.
  -opt OPTIONS, --options OPTIONS
                        GCC compilation options. Default:O3
```
## TODO
Add more templates
[*]
