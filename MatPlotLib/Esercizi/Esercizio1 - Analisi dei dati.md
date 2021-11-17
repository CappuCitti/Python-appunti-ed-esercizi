## Istruzioni dell'esercizio 1
Creare un file e rinominarlo *Esercizio1.ipynb*, importando le librerie necessarie.
1. Creare un *DataFrame* da [questo file](https://raw.githubusercontent.com/CappuCitti/Python-appunti-ed-esercizi/main/MatPlotLib/Data/sample_chat_data.json) json ed assegnarlo ad una variabile `df`.
2. Creare un **grafico a barre** che mostri il numero di messaggi inviato da ogni utente in ordine decrescente, avente le seguenti caratterisiche:
    - I *tick* dell'asse delle ascisse siano inclinati di 45°
    - Un titolo appropirato che descriva il grafico
    - Impostare il colore `royalBlue` per colorare le barre
    - Ingrandire le dimenrsioni del grafico e del testo del 50% (`figsize` default: [6.4, 4.8], `font.size` default: 10)
3. Creare un **grafico a torta** che riporti il totale dei messaggi inviati suddivisi per giorni avente le seguenti caratteristiche:
    - L'angolo 0 deve partire da una inclinazione di 45°
    - Mettere in esposizione la fetta del grafico che assuneme il minor valore percentuale
    - Utilizzando come riferimento questo [NoteBook](https://github.com/CappuCitti/Python-appunti-ed-esercizi/blob/main/MatPlotLib/Notebook%20extra%20-%20Stile%20del%20grafico.ipynb) scegliere 7 colori diversi per ogni giorno della settimana ed utilizzarli per colorare le fette del grafico
    - Impostare come valori delle label del grafico il giorno di riferimento
4. Creare un unico grafico a barre che riporti il numero totale dei messaggi inviati per ogni utente suddivisi in *messaggi testuali*, *messaggi che contengo media* e *messaggi che contengono links*, avente le seguenti caratteristiche:
    - Utilizare i colori `#0097e6`, `#e1b12c` e `#44bd32` corrispettivamente per *messaggi testuali*, *messaggi che contengo media* e *messaggi che contengono links*
    - Inclinare i *tick* dell'asse delle ascisse di 45°
    - Un titolo appropirato che descriva il grafico
    - Aggiungere delle label appropiate ad ogni colonna e visualizzarle nella legenda, posizionarla a destra.
    - Impostare `Unetnti` come *label* dell'asse delle X
    - Impostare `Numero di messaggi` come *label* dell'asse delle Y

### Suggerimenti
🔗 [Design del grafico e colori](https://github.com/CappuCitti/Python-appunti-ed-esercizi/blob/main/MatPlotLib/Notebook%20extra%20-%20Stile%20del%20grafico.ipynb) (matplotlib - styles)<br>
🔗 [Conversione di una colonna in fomato data](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html) (Pandas)<br>
🔗 [Accedere alle proprietà di una Series in formato *Datetime*](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.html) (Pandas)<br>
🔗 [Come trovare il valore minimo di un array](https://docs.python.org/3/library/functions.html#min) (Built-in Functions)<br>
🔗 [Addizioni tra array](https://numpy.org/doc/stable/reference/generated/numpy.add.html) (numpy)<br>
🔗 [Sottrazione tra array](https://numpy.org/doc/stable/reference/generated/numpy.subtract.html) (numpy)<br>
🔗 [`matplotlib.pyplot.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html) (matplotlib)<br>
● Per i punti 3 e 4 bisogna reimpostare la [dimensione del testo](https://stackoverflow.com/a/6441839)
