from csv import reader
import sys
from pyspark import SparkContext
sc = SparkContext("local","world1")

confirmed = sc.textFile(sys.argv[1])
deaths = sc.textFile(sys.argv[2])
recovered = sc.textFile(sys.argv[3])

confirmed = confirmed.mapPartitions(lambda x: reader(x)).filter(lambda x: len(x)!=0)\
            .filter(lambda x: x[0]!="CNTRY_NAME")
deaths = deaths.mapPartitions(lambda x: reader(x)).filter(lambda x: len(x)!=0)\
            .filter(lambda x: x[0]!="CNTRY_NAME")
recovered = recovered.mapPartitions(lambda x: reader(x)).filter(lambda x: len(x)!=0)\
            .filter(lambda x: x[0]!="CNTRY_NAME")

confirmed_top20 = confirmed.sortBy(lambda x: int(x[-1]),False,1).take(20)
confirmed_top20 = sc.parallelize(confirmed_top20).map(lambda x: ','.join(x))
deaths_top20 = deaths.sortBy(lambda x: int(x[-1]),False,1).take(20)
deaths_top20 = sc.parallelize(deaths_top20).map(lambda x: ','.join(x))
recovered_top20 = recovered.sortBy(lambda x: int(x[-1]),False,1).take(20)
recovered_top20 = sc.parallelize(recovered_top20).map(lambda x: ','.join(x))

confirmed_top20.saveAsTextFile("results/world_confirmed_top20.out")
deaths_top20.saveAsTextFile("results/world_deaths_top20.out")
recovered_top20.saveAsTextFile("results/world_recovered_top20.out")
