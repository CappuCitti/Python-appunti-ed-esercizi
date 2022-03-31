# [Folium](https://python-visualization.github.io/folium/)
Folium è una potente libreria Python che aiuta a creare diversi tipi di mappe [Leaflet](https://leafletjs.com/).

**Come installare folium**:
```cmd
pip install folium
```

A volte Folium necessita anche di librerie aggiuntive per funzionare:
```cmd
pip install matplotlib mapclassify
```

## Utilizzo con Geopandas
Folium viene utilizzato per creare mappe interattive basandosi su dati spaziali, gestiti da Geopandas, e facilmente implementabili nelle mappe di Leaflet tramite folium.<br>
:link: [Guida base](https://geopandas.org/en/stable/gallery/polygon_plotting_with_folium.html)

## Come iniziare
Per creare una mappa di Folium basta una semplice linea di codice, dove viene specificato come primo parametro le coordinate (nel sistema CRS `EPSG:4326`) del punto d'origine della mappa, come parametro `zoom_start` il livello di zoom di essa e infine come parametro `tiles` il tipo di mappa da utilizzare
```py
import folium

m = folium.Map(location=[45.46409946028481, 9.19187017173384], zoom_start=12.5, tiles='cartodbpositron')
```

In seguito e' possibile rappresentare punti, linee e poligoni sulla mappa aggiungedoli come layer alla variabile mappa.<br>

**Aggiunta di un punto sulla mappa**<br>
Come primo parametro vengono passate le coordinate del punto, il parametro `popup` indica cosa apparira' quando viene cliccato marcatore.
```py
folium.Marker([45.46418006476384, 9.191221481030022], popup='Duomo di Milano').add_to(m)
```

## Come vedere la mappa
**Metodo 1**<br>
In seguito aver rappresentato le figure necessarie sulla mappa, aver apportato modifiche dei poligoni raffigurati ed aver salvato la mappa in un file html e' necessario assegnarli un endpoint per raggiungerla facilmente.
```py
# Le modifiche effettuate vengono salvate nel file HTML 'map.html'
@app.route('/', methods=['GET'])
def home():
  my_map.save("maps/map.html")
  return render_template('index.html')

# In seuito la mappa viene data dall'endpoint '/map' quando richiesta
@app.route('/map', methods=['GET'])
def map():
  return send_file('maps/map.html')
```

```html
<!-- Richiedere la mappa in una pagina HTML -->
<iframe src="/map" frameborder="0"></iframe>
```


**Metodo 2**<br>
Il secondo metodo consiste nell'effettuare tutte le modifiche e restituire direttamente la mappa creata senza salvarla in un file HTML.
```py
@app.route('/visualizer', methods=['GET'])
def show_map():
  return my_map._repr_html_()
```