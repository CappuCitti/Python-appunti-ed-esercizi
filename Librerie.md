# Librerie di Python

### Cosa sono
In Python, i moduli sono semplicemente file con estensione `.py` contenenti codice Python che possono essere importati all'interno di un altro programma Python. possiamo considerare un modulo come una libreria di codici o un file che contiene un insieme di funzioni che si vogliono includere nell'applicazione.

### Perhcé utilizzarle
Con l'aiuto dei moduli, possiamo organizzare funzioni correlate, classi o qualsiasi blocco di codice nello stesso file. E' utile quando si scrivono codici più estesi dividere i grandi blocchi di codice Python in moduli più piccoli.

### Principali librerie
Python offre librerie di base preinstallate come `math` e `random`, ma esistono altre svariate librerie per semplificare operazioni, constanti o per l'organizzazione di file o variabili.

## `Math`
🔗 [Documentazione](https://docs.python.org/3/library/math.html)
```py
# Importazione della libreria
import math
```

Funzione | Descrizione | Esempio | Risultato
--- | --- | --- | ---
`math.pi` | Restituisce la costante del π | `math.pi**2 * 15` | Circa **148.044**
`math.sqrt(n)` | Esegue la radice quadrata di un numero | `math.sqrt(4)` | **2.0**


## `Random`
🔗 [Documentazione](https://docs.python.org/3/library/random.html)
```py
# Importazione della libreria
import random as rn
```

Funzione | Descrizione | Esempio | Risultato
--- | --- | --- | ---
`rn.randrange([start], stop[, step])` | Restituisce un elemento selezionato casualmente dall'intervallo dato |  |
`rn.randint(a, b+1)` | Restituisce un numero intero casuale tra due valori interi dati | | a <= n <= b
`rn.random()` | Restituisce un valore decimate tra 0.0 compreso e 1.0 | | [0.0, 1.0)
`rn.shuffle(arr)` | Riordina in modo casuale la sequenza data | |

## `Numpy`
🔗 [Documentazione](https://numpy.org/doc/stable/)
```py
# Importazione della libreria
import numpy as np
```

Funzione | Descrizione | Esempio | Risultato
--- | --- | --- | ---
`np.arange([start, ]stop, [step, ])` | Crea un array di numeri interi da i valori dati | |
`np.reshape(arr, (n1, n2))` | Restituisce una nuova forma a un array tramite i valori dati senza modificarne i dati.<br>`arr` Array<br>`n1` Indica il numero di array da restituire<br>`n2` Indica il valore da restituire per ogni array| |
`np.random.rand(d0, d1, ..., dn)` | Restituisce valori casuali nel formato dato | `np.random.rand(2, 3)` | `array([[0.70418549, 0.15846463, 0.41533206], [0.19298845, 0.18760822, 0.78978225]])`
`np.add(arr1, arr2)` | Restituisce la somma tra due array | `np.add([1, 2, 3], [4, 5, 6])` | `[5, 7, 9]`
`np.subtract(arr1, arr2)` | Restituisce la differenza tra due array | `np.subtract([4, 5, 6], [1, 2, 3])` | `[3, 3, 3]`
