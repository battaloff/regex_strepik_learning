"""<= > ?

@ABCDEFGHIJKLMNOPQRSTUVWXYZ[] ^ _


`abcdefghijklmnopqrstuvwxyz
{ |}~абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ !"#$%&\'()*+,-./0123456789:;
"""

import re

# pattern = re.compile(r'(?<=[^ё$MuUSТCГя50ЦnДE;9АJ])(?:\**?)(?=[ШП9В9фвфЛ]*/)')
# text = 'fsdfdsf.mе&r!kX\q<ЫlХювк*ШЛ/PWЖЁRЩ-NнОaбъСНлdй(ф^4{sZjИ`@жЮБF7"ЕoиэП:Ьуь~№[0A+%_сGQv)ё$MuUSТCГя50ЦnДE;9АJ]В'
# print(pattern.findall(text))
from re import findall

regex = re.compile(r" esta ")
text = "ngasiitextasfast esta fa388testskdg993test"
x = re.findall(regex, text)
print(x)

