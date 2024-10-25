def all_variants(strings):
    len_pod_strings = 1
    while len_pod_strings <= len(strings):
        for i in range(len(strings) + 1 - len_pod_strings):
            yield strings[i:i+len_pod_strings]
        len_pod_strings += 1

func1 = all_variants('1234567890_qwertyuiopasdfghjklzxcvbnm')
for i in func1:
    print(i)