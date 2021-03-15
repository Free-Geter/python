import re

with open("company_temp.html", "r") as f:

    contents = f.read()

start_date = re.findall(r'<a href="[A-Za-z0-9+&@#/%?=~_|!:,.;]+;EstablishDate=[0-9]{6}"\starget="_blank">([0-9]{4}-[0-9]{2}-[0-9]{2})</a>',contents)
major = re.findall(r'''<td class="ct">主营业务：</td>
		<td colspan="3" class="ccl">(.*?)</td>''',contents)
print(start_date)
print(major)