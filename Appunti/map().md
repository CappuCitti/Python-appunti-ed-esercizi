# map()
La funzione `map()` applica una data funzione a ciascun elemento di un iterabile (lista, tupla ecc.) e restituisce un iteratore.

## Sintassi
La funzione `map()` accetta due parametri:
* **Funzione** - una funzione che esegue un'azione su ciascun elemento di un iterabile
* **Iterable** - un iterabile come set, liste, tuple, etc.

Puoi passare più di un iterabile alla funzione map().
```py
map(funzione, iterabile, ...)
```

### Esempio
Viene creato una lista di numeri, in seguito con la funzione si raddoppia ogni numero all'interno della lista con una funzione `lambda`.
Il risultato dara di tipo *map*, bisgona riconvertirlo in una lista!
```py
nums = [5, 8, 9, 3, 8]
print(list(map(lambda x: x*x, nums)))
```
