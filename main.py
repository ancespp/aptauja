import os

print("Mēs strādājam no 10:00 līdz 22:00, bet piektdienās līdz 20:00")
print()
saz=int(input("Vai jūs vēlaties lai mēs sazināmies ar Jums caur telefonu (ievadiet 1) vai caur e-pastu(Ievadiet 2)?: "))
if saz==1:
  tlf=int(input("Ievadi savu telefona numuru: "))
elif saz==2:
  epast=input("Ievadi savu e-pastu: ")
else:
  print("Tā nav viena no izvēlēm!")
  exit()
vards=input("Ievadi savu vārdu:")
uzvards=input("Ievadi savu uzvārdu: ")
dzim=input("Ievadi dzimumu: ")
meist=input("Ir pieejami divi meistari-Juris (nagu meistars) un Laimdota (friziere), kurš būs Jūsu meistars?: ")
if meist=="Juris" or meist=="Laimdota":
  print("Meistars izvēlēts!")
else:
  print("Tada meistara nav!")
  exit()


if meist=="Juris":
  jrs = open("Juris.txt", "r")
  content = jrs.read()
  print(f"Šie laiki Jurim nav pieejami: {content}")
  content_list = content.split(",")
  jrs.close()
  diena=float(input("Kurā dienā Jūs vēlētos ierasties? (Piem. 21.09): "))
  laiks=input("cikos Jūs vēlētos ierasties? Meistara pieejamība ir tikai pa veselai stundai (Piem. 14:00):  ")
  n=open("Juris.txt", "a")
  n.write(f"({diena} {laiks}) \n")
  n.write(" ")
  n.close()

else:
  lmd=open("Laimdota.txt", "r")
  contents=lmd.read()
  print(f"Šie laiki Laimdotai nav pieejami: {contents}")
  conteta_lists=contents.split(",")
  lmd.close()
  diena=float(input("Kurā dienā Jūs vēlētos ierasties? (Piem. 21.09): "))
  laiks=input("cikos Jūs vēlētos ierasties? Meistara pieejamība ir tikai pa veselai stundai (Piem. 14:00): ")
  n=open("Laimdota.txt", "a")
  n.write(f"({diena} {laiks}) \n")
  n.write(" ")
  n.close()


f=open("lietotajs.txt", "a")
f.write(" ")
f.write(f" Vārds: {vards} \n")
f.write(f" Uzvārds: {uzvards} \n")
f.write(f" Dzimums: {dzim}\n")
if saz==1:
  f.write(f" Telefona numurs: {tlf} \n")
else:
  f.write(f" E-pasts: {epast} \n")
f.write(f" Izvēlētais meistars: {meist} \n")
f.write(f" Datums: {diena} \n")
f.write(f" Izvēlētais laiks: {laiks} \n")
f.write(" ")

f.close()
print()


def dzest():
    izdzest = 'clear'
    if os.name in ('nt', 'dos'):  
        izdzest = 'cls'
    os.system(izdzest)

dzest()
print("Paldies ka izvēlējāties Jūčūb skaistumkopšanas salonu!")