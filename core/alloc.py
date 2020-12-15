def alloc_virtualalloc():
    return "(PCHAR)VirtualAlloc(NULL, sizeof(offset_table), MEM_COMMIT, PAGE_EXECUTE_READWRITE);"

def alloc_malloc():
    return "(PCHAR)malloc(sizeof(offset_table));"