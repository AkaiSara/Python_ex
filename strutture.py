#stringhe (array di char) [immutabili]
frutto = "banana"
lettera = frutto[3]
print lettera
#come le liste anche le stringhe sono enumerate da 0
print frutto[0]

print len(frutto) #len restituisce la lunghezza della stringa
print frutto[-2] #stampa il penultimo carattere
#con i numeri negativi si stampa dalla fine

#iterazione della stringa con ciclo while
indice = 0
while indice < len(frutto):
	print frutto[indice]
	indice += 1

#iterazione della stringa con for
for lettera in frutto:
	print lettera	

#porzioni di stringa
print frutto[:7] 
#[num:] prende dall'indice num compreso, fino alla fine
#[:num] prende dall'inizio a indice num escluso
#[n:m] da n incluso a m escluso
#[:] tutto
#se num eccede verra' stampato fino all'ultimo carattere

#posso confrontare le stringhe con gli operatori booleani per mettere le stringhe in ordine, ricordando che le lettere maiuscole vengono prima di quelle minuscole

#le stringhe sono immutabili, non posso fare frutto[3] = 'f'

import string #modulo che contiene funzioni per le stringhe

posizione = string.find(frutto, 'a') #cerco nella variabile del primo argomento dove compare la lettera specificata nel secondo argomento
#funziona anche per cercare sottostringhe
string.find(frutto, "an")
#(variabile, stringa che cerco, indice da dove cominciare(incluso), indice massimo(escluso))

#string: find, lowercase, uppercase,digits, whitespace, split, join
#split e join convergono stringhe da/a liste


#alias
cibo = "banana" #entrambe le variabili puntano allo stesso oggetto
print frutto, id(frutto)
print cibo, id(cibo)



#liste (array di tipo) [mutabili]

#creazione
lista = [1, 2, 'a', "asd", [2,4]]
lista = range(1,5) #crea una lista con elementi da 1(incluso) a 5(escluso)
lista = range(5) #crea una lista da 0 incluso a 5 escluso
lista = range(1, 10, 3) #crea una lista  da 1 a 10 escluso ogni 3 elementi
lista = [] #lista vuota
#print lista

lista = range(5)
print lista
lista[2] = 'a'
lista[5-4] = 'b'
print lista
#lista[10] da errore
print lista[-3]
len(lista)

for var in lista:
	print var #var = lista[index]

#l'operatore + concatena le liste
#l'operatore * ripete una lista n volte
#[:] prende tutta la lista
#[n:], [:n], [n:m]

#e' possibile aggiornare le liste tramite assegnazione
lista[2] = 'a'
#e' possibile modificare le liste con assegnazione di porzione
lista[3:] = [22,24,25]
print lista
#e' possibile rimuovere uno o piu elementi assegnando la lista vuota
lista[2:5] = []
print lista
#e' possibile inserire elementi nel mezzo della lista, prima o dopo
lista[1:1] = [1.0,3.5,5.6]
print lista

#cancellazione delle liste
del lista[:] 
print lista

#alias
lista = range(3)
lista2 = range(3) #si crea un altro puntatore con oggetto diverso
print lista, id(lista)
print lista2, id(lista2)

#clonazione
a = range(2)
b = a[:] #a[:] crea il clone, a soltanto crea una copia(id uguali)
print a, b, id(a), id(b)

#ogni lista passata ad una funzione viene passata per riferimento 


lista = [1, 2, 'a', "asd", [2,4]]
#per accedere alla sottolista uso
print lista[4][0] #[indice lista][indice sottolista]

#matrici di righe con le liste
matrix = [[2,3], [5,6]] #[prima riga] [seconda riga]
print matrix[0], "\n", matrix[1]
#accedo alla matrice con matrix[riga][colonna]
print matrix[0][1]



#tuple [immutabili]
tupla = ('a','b','c') #le parentesi non sono necessarie, ma rendono il codice piu visibile
tupla = ('a',) #necessaria la virgola altrimenti viene considerata come un carattere

t2 = ('1','2','3')
print tupla, t2
tupla ,t2 = t2, tupla
print tupla, t2

#metodi: append, extend, reverse, sort



#dizionari(array di tipo con indici di tipo) [mutabili]
diz = {} #dizionario vuoto
diz['uno'] = '1' #assegnazione
diz['due'] = '2' #nomedizionario[chiave] = elemento
print diz

diz = {'u':'1' , 'd':'2', 't':'3'}
print diz
print diz['u']

#del per eliminare elementi, len per sapere la dimensione del dizionario
del diz['u']
print diz
print len(diz) #numero di coppie chiave elemento

#metodi 
print diz.keys() #chiavi
print diz.values() #elementi
print diz.items() #chiavi ed elementi

print diz.has_key('d') #guarda se esiste una chiave e ritorna un bool

copia = diz.copy() #clone
print copia
alias = diz #alias

conta = diz.items()
conta.sort()
print "conta", conta

#matrici
matrix = {(0,0) : 2, (0,1): 3, (1,1): 1}
print matrix[(0,0)] #primo elemento

#matrix[1,0] non esiste nel dizionario
print matrix.get((1,0), 0) #la chiave non e' presente nel dizionario


