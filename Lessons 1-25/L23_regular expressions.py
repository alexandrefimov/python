import re

mytext = "Vasya, 1999, d.kljfjahd a;dfklih;jaldksfj ';dflasjkd" \
         "Petya d. ladsfjhads adsfnads, 1888" \
         "amnbdsfbad.sfb adbdasfbmnadsf ads, Sasha, 1994 " \
         "111fjhdfkjhdfkj@mail.ru ffffffffff"

"""
\d = любая цифра
\D = не цифра
\w = любая буква [A-Z, a-z]
\W = не буква
\s = пробел
\S = не пробел
[0-9] диапазон {4} сколько подряд
[A-Z][a-z]+ = первая буква большая, остальные маленькие
\w+@\w+\.\w+ для поиска e-mail
"""
textlookfor = r"\w+@\w+\.\w+"
allresults = re.findall(textlookfor, mytext)

print(allresults)