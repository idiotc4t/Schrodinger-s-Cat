def alloc_virtualalloc():
    return "(PCHAR)VirtualAlloc(NULL, sizeof(offset_table), MEM_COMMIT, PAGE_EXECUTE_READWRITE);"

def alloc_malloc():
    return "(PCHAR)malloc(sizeof(offset_table));"

def alloc_calloc():
    return " (PCHAR)calloc(sizeof(offset_table), sizeof(char));"

def alloc_maping():
    return "(PCHAR)MapViewOfFile(CreateFileMapping(INVALID_HANDLE_VALUE, NULL, PAGE_EXECUTE_READWRITE, 0, sizeof(offset_table), NULL), FILE_MAP_WRITE, 0, 0, sizeof(offset_table));"