# GeoPandas
GeoPandas è un'estensione della libreria *Pandas* che aggiunge supporto per i dati geospaziali.

### Collegamenti utili
🔗 [Pandas](https://pandas.pydata.org/docs/user_guide/dsintro.html)<br>
🔗 [GeoPandas](https://geopandas.org/en/stable/docs/user_guide.html)

## Come utilizzare *GeoPandas*
Prima di utilizzare la libreria è necessario importarla tramite il terminale di sistema (ogni volta che sia avvia un nuovo notebook su Colab è necessario reinstallarla)
```py
# Bisogna eseguire questa linea di codice prima di importare GeoPandas all'interno del NoteBook
!pip install geopandas
```
In seguito è necessario importarla nel proprio codice:
```py
import geopandas
# Oppure
import geopandas as gpd
```

## Struttura dati: il *GeoDataFrame*
La struttura dati di base in *GeoPandas* è `geopandas.GeoDataFrame`, una sottoclasse di `pandas.DataFrame`, che può memorizzare colonne geometriche ed eseguire operazioni spaziali. Il `geopandas.GeoSeries`, una sottoclasse di `pandas.Series`, gestisce le geometrie. Pertanto, il *GeoDataFrame* è una combinazione di `pandas.Series`, con dati tradizionali (numerici, booleani, di testo ecc.), e `geopandas.GeoSeries`, con geometrie (punti, poligoni ecc.). Si possono creare tutte le colonne geometriche necessarie all'interno del `geopandas.GeoDataFrame`.

![`geopandas.GeoDataFrame`](https://geopandas.org/en/stable/_images/dataframe.svg)

Ogni `GeoSeries` può contenere qualsiasi tipo di geometria (si possono anche mescolare all'interno di un singolo array) e ha un attributo `GeoSeries.crs`, che memorizza le informazioni sulla proiezione (CRS sta per Coordinate Reference System). Pertanto, ogni `GeoSeries` in un `GeoDataFrame` può trovarsi in una proiezione diversa, consentendo, ad esempio, di avere più versioni (proiezioni diverse) della stessa geometria.

Solo un `GeoSeries` in un `GeoDataFrame` è considerato la geometria attiva, il che significa che tutte le operazioni geometriche applicate a un `GeoDataFrame` operano su questa colonna attiva.
