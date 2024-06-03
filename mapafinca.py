import folium
import pandas as pd

from folium import Map, Html, Element
from folium.plugins import FloatImage
version="versión: Junio 2 de 2024"

title_html= '''
<div style="position:fixed;
            bottom:80%;
            left: 5%;
            width: 200px;
            height: 70px;
            background-color: white;
            border:2px solid grey;
            z-index: 9999;
            font-size: 14px;
        

">
<b>Finca El Palmar</b>
<br>Vereda El Consuelo<br>
'''+version+''' 
</div>


'''

ungrado=111139
unmetro=1/ungrado
center_lat=5.2494855 + unmetro*10
center_lon=-75.7373283 - unmetro*30
area_size=360
grid_spacing=10
data = pd.read_csv("fincajun1.csv")
ErsiWorldImagery = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
m = folium.Map(location = [center_lat, center_lon ],max_zoom = 30 , zoom_start = 19, tiles = ErsiWorldImagery, attr="Ersi"
       )

for i in range (0 , area_size + grid_spacing, grid_spacing):
    start_lat = center_lat - (area_size/2)* unmetro 
    end_lat = center_lat + (area_size/2)* unmetro 
    lon = center_lon - (area_size/2 * unmetro) + i * unmetro
    folium.PolyLine(locations=[[start_lat,lon],[end_lat,lon]], color="green", weight=1, popup=str(lon)+" 10m= "+str(unmetro*10)).add_to(m)
    if lon == center_lon :
        folium.PolyLine(locations=[[start_lat,lon],[end_lat,lon]], color="red", weight=2, popup=str(lon)+" 10m= "+str(unmetro*10)).add_to(m)
        



    start_lon = center_lon - (area_size/2)* unmetro 
    end_lon = center_lon + (area_size/2)* unmetro 
    lat = center_lat - (area_size/2 * unmetro) + i * unmetro
    folium.PolyLine(locations=[[lat,start_lon],[lat,end_lon]],popup=str(lat)+" 10m "+str(unmetro*10), color="green", weight=1).add_to(m)
    if lat == center_lat :
        folium.PolyLine(locations=[[lat,start_lon],[lat,end_lon]],popup=str(lat)+" 10m "+str(unmetro*10), color="red", weight=2).add_to(m)


#dibujos desde archivo .csv
arreglo_calera = []
cal_amarilla = []
amarilla_norte = []
amarilla_nortedos = []
falla = []
aguita = []
aguitados = []



    
filodehambre2=[5.2533954,-75.7106932]
cerroconchari=[5.2405030,-75.7193136]
cerrocorazon=[5.2447222,-75.7108333]
filodehambre=[5.2574223,-75.7254020]
antena=[5.2522232,-75.7274845]
mangoMolienda=[5.250050,-75.736180]
dudosoMolienda=[5.249921,-75.736640]
dudosoSuperior=[5.250327,-75.737031]
pOso1=[5.24977,-75.739105]
Amarillana = [	5.249787+(unmetro*3) ,	-75.73887 ]
Amarillanbbandera =	[5.249769+(unmetro*3),	-75.73878]
Amarillanc =	[5.2497077+(unmetro*3),	-75.73872]
Amarilland =	[5.2496624+(unmetro*3),	-75.73864]
Amarillane =	[5.2496266+(unmetro*3),	-75.73858]
Amarillanf =	[5.249585+(unmetro*3),	-75.73849]
Amarillang =	[5.2495465+(unmetro*3),	-75.73837]
pOso2=[	5.2496996	,	-75.7381276	]
pOso3=[	5.2499378	,	-75.7377798	]
pOso4=[	5.2500415	,	-75.737441	]
pOso5=[	5.250148	,	-75.7371139	]
oso=[
pOso1,
Amarillana, 
Amarillanbbandera, 
Amarillanc,
Amarilland,
Amarillane ,
Amarillanf,
Amarillang,
pOso2,
pOso3,
pOso4,
pOso5
,
[	5.2502892	,	-75.7368807	],
[	5.2507306	,	-75.7364539	],
[	5.2509923	,	-75.7362662	],
[	5.2511953	,	-75.7359819	]

]
calera=[[	5.2486029	,	-75.7380161	],
[	5.2486697	,	-75.7379785	],
[	5.2488102	,	-75.7376113	],
[	5.2491894	,	-75.7374772	],
[	5.2492788	,	-75.73745839999999	],
[	5.2494137	,	-75.73741819999999	],
[	5.2496729	,	-75.73731359999999	],
[	5.2498652	,	-75.73712039999999	],
[	5.250148	,	-75.7371139	]] 

pital=[
[5.2480569,-75.7367745],
[5.2488048,-75.7365357],
[5.2494264,-75.73645430000001],
[5.249769,-75.736458],
[5.2503833,-75.7363936],
[5.2506718,-75.7362246],
[5.250808,-75.7360985],
]
carreteraEntrada=[[ 	5.249138	,	-75.7370185	]	,
[	5.2492635	,	-75.7369286	]	,
[	5.2494264	,	-75.73698899999999	]	,
[	5.2494532	,	-75.7369327	]	,
[	5.2494024	,	-75.73683080000001	]	,
[	5.2494184	,	-75.736745	]	,
[	5.249544	,	-75.73667519999999	]	,
[	5.2495707	,	-75.7366055	]	,
[	5.2495493	,	-75.7364848	]	,
[	5.2495653	,	-75.736407	]	,
[	5.2496428	,	-75.7363426	]	,
[	5.2496882	,	-75.73619239999999	]	,
[	5.2497096	,	-75.7361441	]	]

carretera=[[ 	5.2503266	,	-75.735956	]	,
[	5.2501102	,	-75.7360553	]	,
[	5.2499579	,	-75.7361686	]	,
[	5.2498458	,	-75.7361894	]	,
[	5.2496107	,	-75.7361277	]	,
[	5.2494532	,	-75.73611699999999	]	,
[	5.2492742	,	-75.736176	]	,
[	5.2490979	,	-75.73611699999999	]	,
[	5.2489483	,	-75.73606940000001	]	]


caminoHerradura=[[ 	5.2491593	,	-75.738247	]	,
[	5.249327	,	-75.73809	]	,
[	5.249395	,	-75.73801	]	,
[	5.2494478	,	-75.7379815	]	,
[	5.2494826	,	-75.7378822	]	,
[	5.249528	,	-75.7377884	]	,
[	5.249583	,	-75.73775000000001	]	,
[	5.249628	,	-75.73774	]	,
[	5.2496448	,	-75.7376716	]	,
[	5.249672	,	-75.73764	]	,
[	5.249706	,	-75.7376	]	,
[	5.249783	,	-75.73754	]	,
[	5.249784	,	-75.737465	]	,
[	5.249806	,	-75.73742	]	,
[	5.249854	,	-75.73747	]	,
[	5.249899	,	-75.73752	]	,
[	5.2499413	,	-75.7374803	]	,
[	5.2500096	,	-75.73733679999999	]	,
[	5.2500148	,	-75.7373078	]	,
[	5.249965	,	-75.73721279999999	]	,
[	5.2499588	,	-75.73714649999999	]	,
[	5.2500679	,	-75.73708790000001	]	,
[	5.2502811	,	-75.7370293	]	,
[	5.2503746	,	-75.7370507	]	,
[	5.2505456	,	-75.7369568	]	]

tanqueramontrejos= [5.249860, -75.739115]
cartagueno= [5.249550, -75.736371]
mandarino=[5.2500143,-75.73898]
esquinarojo= [5.249133, -75.738248]
limitebernabe=[5.249183,-75.737656]
mataverdecasa= [5.249333, -75.737207]
esquinaruben= [5.249016, -75.736881]
mangoEntrada=[	5.2496666,	-75.73620630000001	]
folium.Marker(location = tanqueramontrejos  , popup = "tanque Ramón Trejos").add_to(m)

folium.PolyLine(locations=pital, color='blue').add_to(m)
folium.PolyLine(locations=calera, color='blue' ,popup = "La Calera").add_to(m)

folium.PolyLine(locations=caminoHerradura, color='black').add_to(m)
folium.PolyLine(locations=carretera, color='black').add_to(m)
folium.PolyLine(locations=carreteraEntrada, color='black').add_to(m)
nuevas_coords = [ 
cartagueno,mangoEntrada,mangoMolienda,dudosoMolienda,pOso5,pOso4,pOso3,pOso2,Amarillang,mandarino,esquinarojo,limitebernabe,mataverdecasa,esquinaruben]

folium.Polygon(locations=nuevas_coords, color='green', fill=True, fill_color='green', fill_opacity=0.2).add_to(m)
mangoEntrada



# Añadir el polígono al mapa
folium.PolyLine(locations=oso, color='blue').add_to(m)
folium.CircleMarker(
    location = [5.24936,-75.737105],
    fill = True,
    popup = "Casa Azul").add_to(m)
casaDonAlberto = 123
folium.Marker(location = antena, popup="antena").add_to(m)
folium.Marker(location = filodehambre, popup="filodehambre").add_to(m)
folium.Marker(location = filodehambre2, popup="filodehambre2").add_to(m)
folium.Marker(location = cerroconchari, popup="cerro Concharí").add_to(m)
folium.Marker(location = cerrocorazon, popup="cerro Corazón").add_to(m)




for index, row in data.iterrows():

    if row['Etiqueta'] == "amarilla_calera":
        arreglo_calera.append([row['Latitud'],row['Longitud']])
    elif row['Etiqueta'] == "cal_amarilla":
        cal_amarilla.append([row['Latitud'],row['Longitud']])
    elif row['Etiqueta'] == "amarilla_norte":
        amarilla_norte.append([row['Latitud'],row['Longitud']])
    elif row['Etiqueta'] == "amarilla_norte-2":
        amarilla_nortedos.append([row['Latitud'],row['Longitud']])
    elif row['Etiqueta'] == "falla":
        falla.append([row['Latitud'],row['Longitud']])
    elif row['Etiqueta'] == "aguita":
        aguita.append([row['Latitud'],row['Longitud']])
    elif row['Etiqueta'] == "aguitados":
        aguitados.append([row['Latitud'],row['Longitud']])
    else:
        folium.CircleMarker(
            location=[row['Latitud'],row['Longitud']], 
            popup = row['Nombre']+" "+str(row['Latitud'])+" "+str(row['Longitud']) ,radius=5, color='green', fill=True,fill_color='green'
            ).add_to(m)


folium.PolyLine(locations=arreglo_calera, color="yellow", weight=4, popup="amarilla calera norte").add_to(m)
folium.PolyLine(locations=cal_amarilla, color="yellow", weight=4, popup="amarilla calera sur").add_to(m)
folium.PolyLine(locations=amarilla_norte, color="yellow", weight=4, popup="amarilla oso occidente").add_to(m)
folium.PolyLine(locations=amarilla_nortedos, color="yellow", weight=4, popup="amarilla oso oriente").add_to(m)
folium.PolyLine(locations=falla, color="red", weight=4, popup="falla fea").add_to(m)
folium.PolyLine(locations=aguita, color="blue", weight=4, popup="aguita").add_to(m)
folium.PolyLine(locations=[[5.249523-(unmetro*10) , -75.73854-(unmetro*10)],[5.249523,-75.73854]], color="blue", weight=4, popup="aguita").add_to(m)
folium.PolyLine(locations=aguitados, color="blue", weight=4, popup="aguita").add_to(m)

m.get_root().html.add_child(folium.Element(title_html))
m.save("a.html")
