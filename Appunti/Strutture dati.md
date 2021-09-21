# Data structurs
*La struttura dati è un metodo di organizzazione dati, quindi prescinde da ciò che è effettivamente contenuto.*<br>
*Una struttura dati è un'entità usata per organizzare un insieme di dati all'interno della memoria del computer, ed eventualmente per memorizzarli in una memoria di massa.*

:link: [Wikipedia](https://it.wikipedia.org/wiki/Struttura_dati)

## Memorizzazione *temporanea* e *permanente*
Le strutture dati possono memorizzare i dati in modo:
- Temporaneo
	- Variabili del programma => RAM
- Permanente
	- File => HDD/SSD


## Strutture dati *statiche* e *dinamiche*:
- Statiche:
	Hanno un numero definito di elementi
	```vb
	'Visual Basic
	Dim x[99] As Integer
	```
	
- Dinamiche:
	Hanno un umero variabile di elementi
	```py
	#Python
	list = [1, 2, 3, 'pippo']
	```
	
## Contenitori:
- Pila (Es: I valori vengono inseriti all'inizio)<br>
LIFO:  Last In First Out

- Coda o FIFO (Es: I valori vengono inseriti alla fine)<br>
FIFO: First In First Out<br>
FCFS: First Come First Serve
 
Esempi:
- Lista
- [Albero](https://it.wikipedia.org/wiki/Albero_(informatica)) (Es: Albero genialogico, scala gerarchica)
- [Grafo](https://it.wikipedia.org/wiki/Grafo) (Es: Archiviazione dati dei social)
	
La differenza tra Albero e Grafo è che nel grafo i non ci devono essere per forza relazioni e che possono anche essere orientato
