# Hubert Jackowski

import re
# Zadanie 1
with open("nazwiska_jawne.txt", "r", encoding="utf-8") as reader:
    with open("nazwiska_ukryte.txt", "w", encoding="utf-8") as writer:
        writer.write(re.sub(r"(nazwisk[oau] |nazwiskiem )([A-Z][a-z]*)", r"\1***", re.sub(r"(nazwisk[oau] |nazwiskiem )([A-Z][a-z]*)( *[-] *)([A-Z][a-z]*)", r"\1***\3***", reader.read())))

# Zadanie 2
with open("stronaWWW.html", "r", encoding="utf-8") as reader:
    with open("stronaWWW.txt", "w", encoding="utf-8") as writer:
        writer.write(re.sub(r" *<.*?>[\n]| *<.*?>$", r"", re.sub(r" *<(.*?)>(.*)</(\1)>[\n]", r"\2\n", reader.read())))
