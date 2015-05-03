from random import choice
print("Time 4 some bestemmie")
print(" ")
a = True
soggetto = ["Dio","Gesù cristo"]
bevar = ["cane","kebab",
"carbonizzato","senza glutine",
"all'amatriciana","fattone",
"impotente","merda",
"schifoso","lezzo",
"sudicio","telecom",
"tastiera inceppata","fustigato",
"puttana","pelo pubico",
"assembly","gnocco","maiale"]
while a is True :
  s = input()
  if s != False :
    print (choice(soggetto),
    	choice(bevar)+"!")
    
