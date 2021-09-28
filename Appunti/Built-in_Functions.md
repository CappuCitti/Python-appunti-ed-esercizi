# Nomi delle funzioni

## Slicing
Lo *slicing* per mettere di tagliare un array nelle posizioni necessarie:<br>
```py
#Slicing
arr = [i for i in range(0, 100)]
print(arr[50:])    #Dalla 50° posizione
print(arr[:50])    #Fino alla 50° posizione
print(arr[30:70])  #Dalla 30° posizione fino alla 70°
```
Quando facciamo assumere ad un valore_b il valore di un altro array, due array con gli sessi valori, bisogna prendere tutti gli elementi, questo ci è perfesso di farlo con i *due punti* (:) all'interno delle parentesi quadre.<br>
```py
arr_b = arr[:]
#Adesso arr_b ha gli stessi valori di arr
```

## List comprension
La *list compresion* è un meccaniscmo che permette di costruire una lista scrivendo all'interno delle parentesi quadre le istruzioni per generare i singoli elementi della lista.<br>
**E' un modo più sintetico di eseguire opreazioni nei riguardi degli array.**<br>
```py
#Esempio di list comprension
arr = [i for i in range(0, 100)]
print(arr)
```
