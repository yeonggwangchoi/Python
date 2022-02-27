site="http://naver.com"

site=site[7:]

index=site.index(".")

site=site[0:index]

len =len(site)

count=site.count("e")

total=site[0:3]+str(len)+count
print(total+"!")