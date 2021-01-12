def get_decode(decrypt_method):
    if decrypt_method == "offset":
        decode_code ='''
    for (int i = 0; i < sizeof(offset_table)/sizeof(DWORD); i++)
	{
		lpBuffer[i] = random_dict_table[offset_table[i]];
	}'''
        return decode_code
