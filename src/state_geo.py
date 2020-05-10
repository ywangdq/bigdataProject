import sys
from pyspark.sql import SparkSession

# load datasets
spark = SparkSession.builder.appName('state_geo').getOrCreate()
states = spark.read.format('csv').options(header='true',inferschema='true')\
         .load(sys.argv[1])
geo = spark.read.format('csv').options(header='true',inferschema='true')\
         .load(sys.argv[2])
states.createOrReplaceTempView('states')
geo.createOrReplaceTempView('geo')

# get state-level data with geo information
state_geo = spark.sql('select date(states.date),states.state,states.cases,states.deaths,'\
                      'geo.Latitude,geo.Longitude '\
                      'from states,geo where states.state=geo.City '\
                      'order by states.date,states.state')
state_geo.coalesce(1).write.csv('results/state_geo.out')
