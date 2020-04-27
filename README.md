# bigdataProject

The us_data.py and world_data.py in the src directory do data cleaning, filtering and clustering. The data after processing are in the 'results' directory. To run us_data.py and world_data.py, put the raw data in HDFS and run:

spark-submit --conf spark.pyspark.python=/share/apps/python/3.6.5/bin/python src/world_data.py raw_data/Countries-Confirmed.csv raw_data/Countries-Deaths.csv raw_data/Countries Recovered.csv

spark-submit --conf spark.pyspark.python=/share/apps/python/3.6.5/bin/python src/us-data.py raw_data/us.csv raw_data/us-states.csv
