from pyspark import SparkContext,SparkConf

# sc = SparkContext(appName="AppName",master="local[2]")
#
# rdd = sc.parallelize([1,2,3,4])
# print(rdd.collect())

print("------------")

conf = SparkConf().setMaster("local[*]").\
    setAppName("SecondWay").\
    set("spark.executor.memory","2g")
sc = SparkContext(conf=conf)
rdd = sc.parallelize([1,2,3])
print(rdd.collect())
print("------------")

print(rdd.count())
