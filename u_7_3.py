class WordsFinder:

    def __init__(self, *name_files):
        self.name_files = tuple([name_file for name_file in name_files])

    def get_all_words(self):
        all_words = {}
        for n_file in self.name_files:
            with open(n_file, 'r', encoding='utf-8') as file_:
                spis_words_in_file = []
                for line in file_:
                    for i in [',','.','=','!','?',';',':','+',' - ']:
                        while i in line:
                            line = line.replace(i, '')
                    spis_words_in_file.extend(line.lower().split())
                all_words.update({n_file: spis_words_in_file})
        return all_words

    def find(self, word):
        find_words = {}
        all_words = self.get_all_words()
        for i in all_words:
            if word.lower() in all_words[i]:
                find_words.update({i: all_words[i].index(word.lower()) + 1})
        return find_words

    def count(self, word):
        count_words = {}
        all_words = self.get_all_words()
        for i in all_words:
            if word.lower() in all_words[i]:
                count_words.update({i: all_words[i].count(word.lower())})
        return count_words


with open('u_7_3_prim_1.txt', 'w', encoding='utf-8') as file:
    file.write("""Microsoft .NET Framework incorporates third party material from the projects listed below. 
1.	Socket Specification 
2.	IETF RFC 2553: Basic Socket Interface Extensions for IPv6 (https://tools.ietf.org/html/rfc2553)
3.	IETF RFC 1321: RSA Data Security, Inc. MD5 Message-Digest Algorithm (https://tools.ietf.org/html/rfc1321)
4.	Apache Qpid (https://qpid.apache.org/index.html)
5.	jQuery Validation (https://jqueryvalidation.org)
6.	IETF RFC 3492: Bootstring encoding of Unicode for Internationalized Domain Names in Applications  (https://tools.ietf.org/html/rfc3492)
7.	The Unicode Consortium (https://unicode.org/)
8.	LZMA SDK Windows (https://www.7-zip.org/sdk.html)
9.	Zlib (https://github.com/madler/zlib)""")
with open('u_7_3_prim_2.txt', 'w', encoding='utf-8') as file:
    file.write("""ПОДРОБНОЕ ОПИСАНИЕ
    В справке Windows PowerShell описываются командлеты,
    функции, сценарии и модули Windows PowerShell, а также объясняются основные понятия, в том числе
    элементы языка Windows PowerShell.""")
with open('u_7_3_prim_3.txt', 'w', encoding='utf-8') as file:
    file.write("""Windows PowerShell не содержит файлов справки, однако можно просмотреть
    справочные разделы в Интернете или загрузить файлы справки с помощью командлета Update-Help 
    на компьютер и затем отобразить справочные разделы с помощью командлета Get-Help
    в командной строке.""")
    
wf = WordsFinder('u_7_3_prim_1.txt', 'u_7_3_prim_2.txt', 'u_7_3_prim_3.txt')
print(wf.get_all_words())
print(wf.find('Windows'))
print(wf.count('windows'))