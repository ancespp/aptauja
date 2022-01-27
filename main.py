n=0
vards=input("Ievadi savu vārdu:")
uzvards=input("Ievadi savu uzvārdu: ")
dzim=input("Ievadi dzimumu: ")
tlf=int(input("Ievadi savu telefona numuru: "))
epast=input("Ievadi savu e-pastu: ")
meist=input("Ir pieejami divi meistari-Juris (nagu meistars) un Laimdota (friziere), kurš būs Jūsu meistars?: ")
if meist=="Juris" or meist=="Laimdota":
  print("ok")
  n+=1
else:
  print("Tada meistara nav!")
  exit()
diena=float(input("Kurā dienā Jūs vēlētos ierasties?: "))
laiks=input("cikos Jūs vēlētos ierasties?: ")
n=open("numurs.txt", "r")
num=n.read()
n.close
n=open("numurs.txt", "w")
n.write(f"{n+1}")
n.close()

f=open("lietotajs.txt", "a")
f.write(" ")
f.write(f"{n}. apmeklētājs \n")
f.write(f" Vārds: {vards} \n")
f.write(f" Uzvārds: {uzvards} \n")
f.write(f" Dzimums: {dzim}\n")
f.write(f" Telefona numurs: {tlf} \n")
f.write(f" E-pasts: {epast} \n")
f.write(f" Izvēlētais meistars: {meist} \n")
f.write(f" Datums: {diena} \n")
f.write(f" Izvēlētais laiks: {laiks} \n")
f.write("")

f.close()