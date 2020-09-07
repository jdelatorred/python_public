import re

file = open(r'c:/Data/ChatYorch.txt',mode='r',encoding="utf8")
data = file.read()
file.close()

pattern_datetime = re.compile('^[0-9][0-9]?[/][0-9][0-9]?[/]\d\d\d\d\s[0-9]?[0-9]?[:]\d\d\s[^:]+')

outF = open(r'c:/Data/OutChat.txt', mode='w', encoding="utf8")
for line in data:
    line_new = re.sub(pattern_datetime,"", line)
    outF.write(line_new)
outF.close()

violentos = ("Fabricio Martinez","Ignacio Arango","Santiago Muñoz",
             "Jorge De La Torre Dávalos","Julian Villalba","Edgar Barriga",
             "Juan Pablo Ospina","Oscar Santacruz","Nicolas Leuro","Roberto Cobos","<Multimedia omitido>")

for i in violentos:
    data = data.replace(i,"")