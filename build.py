import os, json

data = {}
for f in os.listdir("synaxarium"):
    if f.endswith(".txt"):
        with open("synaxarium/" + f, encoding="utf-8") as file:
            data[f[:-4]] = file.read()

with open("synaxarium-data.js", "w", encoding="utf-8") as out:
    out.write("const SYN = " + json.dumps(data, ensure_ascii=False) + ";")

print("تم! عدد الأيام:", len(data))