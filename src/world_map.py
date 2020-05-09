import pandas as pd
import folium
import os.path

js = os.path.join('src','world.geo.json')
world_confirmed = os.path.join('raw data', 'Countries-Confirmed.csv')
data = pd.read_csv(world_confirmed)

world_map = folium.Map(zoom_start=2)
folium.Choropleth(geo_data=js, data=data.iloc[:,[0,-1]].nlargest(20,'0418'),
                  columns=['CNTRY_NAME','0418'],key_on='feature.properties.name',
                  fill_color='YlOrRd',fill_opacity=0.7,line_opacity=0.2,
                  legend_name='COVID-19 World Top 20 Confirmed Countries').add_to(world_map)
world_map.save(os.path.join('graphs','WorldConfirmedTop20.html'))


world_deaths = os.path.join('raw data', 'Countries-Deaths.csv')
data = pd.read_csv(world_deaths)

world_map = folium.Map(zoom_start=2)
folium.Choropleth(geo_data=js, data=data.iloc[:,[0,-1]].nlargest(20,'0418'),
                  columns=['CNTRY_NAME','0418'],key_on='feature.properties.name',
                  fill_color='YlOrRd',fill_opacity=0.7,line_opacity=0.2,
                  legend_name='COVID-19 World Top 20 Deaths Countries').add_to(world_map)
world_map.save(os.path.join('graphs','WorldDeathsTop20.html'))


world_recovered = os.path.join('raw data', 'Countries-Recovered.csv')
data = pd.read_csv(world_recovered)

world_map = folium.Map(zoom_start=2)
folium.Choropleth(geo_data=js, data=data.iloc[:,[0,-1]].nlargest(20,'0418'),
                  columns=['CNTRY_NAME','0418'],key_on='feature.properties.name',
                  fill_color='YlOrRd',fill_opacity=0.7,line_opacity=0.2,
                  legend_name='COVID-19 World Top 20 Recovered Countries').add_to(world_map)
world_map.save(os.path.join('graphs','WorldRecoveredTop20.html'))
