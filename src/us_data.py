import sys
from pyspark.sql import SparkSession

# load data
spark = SparkSession.builder.appName("us_data").getOrCreate()
us = spark.read.format('csv').options(header='true',inferschema='true')\
     .load(sys.argv[1])
states = spark.read.format('csv').options(header='true',inferschema='true')\
         .load(sys.argv[2])
us.createOrReplaceTempView('us')
states.createOrReplaceTempView('states')

# get US daily increase data
us_increase = spark.sql('select t1.date as date, (t1.cases-t2.cases) as new_cases, '\
                        '(t1.deaths-t2.deaths) as new_deaths from us as t1,us as t2 '\
                        'where t1.date=date_add(t2.date,1) order by date')
us_increase.createOrReplaceTempView('us_increase')
us_result = spark.sql('select date(us.date) as date,cases,deaths,new_cases,new_deaths '\
                      'from us,us_increase where us.date=us_increase.date')
us_result.coalesce(1).write.csv("results/us_daily_increase.out")

# get NY daily increase data
ny = spark.sql("select date(date),cases,deaths from states where state='New York' order by date")
ny.createOrReplaceTempView('ny')
ny_increase = spark.sql('select t1.date as date, (t1.cases-t2.cases) as new_cases, '\
                        '(t1.deaths-t2.deaths) as new_deaths from ny as t1,ny as t2 '\
                        'where t1.date=date_add(t2.date,1) order by date')
ny_increase.createOrReplaceTempView('ny_increase')
ny_result = spark.sql('select ny.date as date,cases,deaths,new_cases,new_deaths '\
                      'from ny,ny_increase where ny.date=ny_increase.date')
ny_result.coalesce(1).write.csv("results/ny_daily_increase.out")
