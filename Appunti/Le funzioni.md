# Funzioni
**Una funzione è un costrutto sintattico di un linguaggio di programmazione che permette di raggruppare un insime di istruzioni che vengono ripetute nel programma**.
```py
#Funzione in Python
def somma(x, y)
  return x + y
  
print(somma(5, 10)) #15
```

### Input e output
**Input**: una funzuione può avere nessun o più argomenti (o parametri), valori di ingresso su cui avviene la funzione.<br>
**Output**: dopo che le istruzioni sono state processate la funzione può avere anche un valore di output.

## **Le funzioni *lambda***
Una funzione _lambda_ è proprio come qualsiasi normale funzione Python, tranne per il fatto che **non ha un nome** quando la definisce ed è contenuta in una riga di codice.
```py
#Funzione lambda in Python
print((lambda x, y: x + y)(2, 3))

#La funzione esegue una operazione, vengono passati come parametri i numeri 2 e 3
```
