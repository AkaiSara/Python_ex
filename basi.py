type(4) #funziona solo su riga di comando, serve per sapere il tipo della variabile tra parentesi
print type(4) #stampa il tipo da un file di script

#print type(ciao) #non funziona perche non e' racchiuso tra virgolette

#i nomi dati alle variabili non devono cominciare per numero, contenere caratteri non validi (ex. $) e non devono appartenere alle parole riservate
a = 12 #dichiarazione 
print a #stampa

x = 3**2 #elevamento a potenza 

messaggio = "ciao"
print messaggio #stampa il valore della varabile 
messaggio #riga di comando stampa il valore della variabile tra virgolette
#per stampare le virgolette uso print ' "messaggio" ', viceversa print " 'messaggio' "

#operazioni sulle stringhe
mex = "oh " #spazio all'interno
print mex + messaggio #concatenamento
print mex * 3 #ripetizione

print mex, a #la virgola spazia
print messaggio, a #non funziona senza virgola

#funzioni
print id(a) #identificatore nella memoria 
type(a) #tipo della variabile
int(a) #conversione in intero (troncamento della parte decimale)
float() #conversione di interi e stringhe to float
str() #conversione in stringhe
# 1 e 1.0 sono numeri differenti per tipo
#conversione forzata (intero) / (float) = (float)
pow(3, 5) #base esponente

import math #modulo matematico
#funzioni: log10, sin, cos, pi, sqrt, log, exp
print math.log10(2) #chiamata identificata col punto

#nuove funzioni
def nuova_funzione(): #definizione della funzione
	print "ciao" , messaggio
#identazione obbligatoria -> { }

print nuova_funzione #stampa il nome e l'area di memoria
nuova_funzione() #parentesi per richiamare la funzione
#la definizione precede la chiamata

#booleani
# == uguale, != diverso, >=, < etc.
print 5 == 5
5 == 5 #su riga di comando stampa 1
#and or not
#in controlla se un valore e' presente in una variabile

#IF
a = -35
if a > 2:
	print "y"
elif a < 0: #else if (condizione)
	 print "n"	
else: 
	print "a"

#inserimento -> input
#funzione raw input, funziona con tutti i tipi di input
ins = raw_input("scrivi qualcosa \t") #\n per andare a capo, \t per tab
print ins

#funzione input, funziona solo con numeri
ins = "anni? "
anni = input(ins) 

def ValAss(x):
	if x > 0 : 
		return x
	elif x < 0 : 
		return -x
#nel caso in cui sia zero viene stampato None poiche non si hanno istruzioni 

x = input("inserisci un numero ")
print ValAss(x)

#while
while x>0 :
	print x
	x -= 1 #x-- non funziona

i = 1
while i < 5 :
	print i, '	' , #senza virgola va a capo ad ogni iterazione 
	i += 1
print #va a capo dopo aver finito il ciclo


import random #modulo
for i in range(3):
	print random.random() #modulo.funzione

