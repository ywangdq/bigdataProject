import pandas as pd
import folium
from folium.plugins import HeatMapWithTime
import os.path

# load data
url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
state_geo = f'{url}/us-states.json'
state_data = os.path.join('results','state_geo.out')
state_data = os.path.join(state_data,'part-00000-9905201c-ff54-4d5c-bbac-ccd90dc04686-c000.csv')
cdata = pd.read_csv(state_data,header=None,\
                    names=['rdate','state','confirmed','deaths','x','y'],\
                    parse_dates=[0])

# prepare geo coordinates lists
confirmed_list = []
deaths_list = []
for d in cdata.rdate.sort_values().unique():
    confirmed_list.append(cdata.loc[cdata.rdate==d,['x','y','confirmed']].\
                          groupby(['x','y']).sum().reset_index().values.tolist())
    deaths_list.append(cdata.loc[cdata.rdate==d,['x','y','deaths']].\
                       groupby(['x','y']).sum().reset_index().values.tolist())

# draw confirmed cases heat map
confirmed_map = folium.Map(location=[48, -102], zoom_start=3)
HeatMapWithTime(confirmed_list,radius=10,\
                gradient={0.2:'blue',0.4:'lime',0.6:'orange',1:'red'},\
                min_opacity=0.5,max_opacity=0.8,\
                use_local_extrema=False).add_to(confirmed_map)

# draw deaths cases heat map
deaths_map = folium.Map(location=[48, -102], zoom_start=3)
HeatMapWithTime(deaths_list,radius=10,\
                gradient={0.2:'blue',0.4:'lime',0.6:'orange',1:'red'},\
                min_opacity=0.5,max_opacity=0.8,\
                use_local_extrema=False).add_to(deaths_map)

# save map
confirmed_map.save(os.path.join('graphs','us_confirmed_heatmap.html'))
deaths_map.save(os.path.join('graphs','us_deaths_heatmap.html'))



