site="http://naver.com"

site=site[7:]

index=site.index(".")

site=site[0:index]

password = site[:3]+str(len(site)+str(len(site))+str(site.count("e"))+"!")

print("{0}의 비밀번호")