from pyspark import SparkContext,SparkConf


sc = SparkContext(appName="rdd_program",master="local[2]")
rdd = sc.parallelize([1,2,3])
print(rdd.collect())

