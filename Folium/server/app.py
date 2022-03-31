from flask import *
import folium
import geopandas as gpd

app = Flask(__name__)

# Carica i file necessati e li trasforma in GeoDataFrame
quartieri = gpd.read_file("./static/data/ds964_nil_wm.zip")
subways = gpd.read_file("./static/data/tpl_metropercorsi_shp.zip")

# Estrae la metropolitana lilla dal GeoDataFrame
m5 = subways.loc[subways['nome'] == 'BIGNAMI - SAN SIRO STADIO']

# Crea la mappa impostando il punto centrale di essa, il tipo di mappa ed il livello di zoom
my_map = folium.Map(location=[45.46409946028481, 9.19187017173384], tiles='cartodbpositron', zoom_start=12)

# Aggiunge un segnapunto in base alle coordinate date e lo aggiunge alla mappa
folium.Marker([45.46418006476384, 9.191221481030022], popup='Duomo di Milano').add_to(my_map)

# Aggiunge l'intero GeoDataFrame alla mappa
shapes = gpd.GeoSeries(quartieri['geometry']).simplify(tolerance=0.000)
shapes = shapes.to_json()
shapes = folium.GeoJson(data=shapes, style_function=lambda x: {"fillOpacity": 0, 'color': 'gray'})
shapes.add_to(my_map)

# Aggiunge la poli line alla mappa
folium.GeoJson(data=m5, style_function=lambda x: {'color': '#FDA7DF', 'weight': 5}).add_to(my_map)


# Metodo 1
@app.route('/', methods=['GET'])
def home():
  my_map.save("maps/map.html")
  return render_template('index.html')

@app.route('/map', methods=['GET'])
def map():
  return send_file('maps/map.html')


# Metodo 2
@app.route('/visualizer', methods=['GET'])
def show_map():
  return my_map._repr_html_()


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=5004)