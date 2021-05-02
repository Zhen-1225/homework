Allpeople =set(["John","Mary","Tina","Fiona","Claire","Eva","Ben","Bill","Bert"])
Englishgood=set(["John","Mary","Fiona","Claire","Ben","Bill"])
mathgood=set(["Mary","Fiona","Claire","Eva","Ben"])
##英文國文都及格
print("英文國文都及格",Englishgood & mathgood)
##數學不及格
print("數學不及格",Allpeople ^ mathgood)
##英文及格且數學不及格
AAA=(Allpeople ^ mathgood)
print("英文及格且數學不及格",Englishgood & AAA)