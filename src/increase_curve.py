import pandas as pd
import matplotlib.pyplot as plt
import os.path

us_increase = os.path.join('results','us_daily_increase.out')
us_increase = os.path.join(us_increase,'part-00000-74efd6f3-48f3-4b40-9f0e-936fb0422310-c000.csv')
ny_increase = os.path.join('results','ny_daily_increase.out')
ny_increase = os.path.join(ny_increase,'part-00000-d637971d-329e-4195-9876-28c0afe049c5-c000.csv')

us_data = pd.read_csv(us_increase,header=None,\
                      names=['date','confirmed','deaths','confirmed_increase','deaths_increase'],\
                      parse_dates=[0])
ny_data = pd.read_csv(ny_increase,header=None,\
                      names=['date','confirmed','deaths','confirmed_increase','deaths_increase'],\
                      parse_dates=[0])

us_confirmed = pd.DataFrame(us_data,columns=['date','confirmed_increase'])
us_deaths = pd.DataFrame(us_data,columns=['date','deaths_increase'])
ny_confirmed = pd.DataFrame(ny_data,columns=['date','confirmed_increase'])
ny_deaths = pd.DataFrame(ny_data,columns=['date','deaths_increase'])

usx = plt.gca()
us_confirmed.plot(x='date',y='confirmed_increase',kind='line',ax=usx,title='U.S. Daily Increase')
us_deaths.plot(x='date',y='deaths_increase',kind='line',ax=usx)
plt.figure()
nyx=plt.gca()
ny_confirmed.plot(x='date',y='confirmed_increase',kind='line',ax=nyx,title='NY Daily Increase')
ny_deaths.plot(x='date',y='deaths_increase',kind='line',ax=nyx)
plt.show()
