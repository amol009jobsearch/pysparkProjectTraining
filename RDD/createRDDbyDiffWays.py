from pyspark import SparkContext, SparkConf

sc = SparkContext(appName="rddProgramm",master="local[2]")
conf=SparkConf().setMaster("local[*]").setAppName("createSparkByConf").set("")
data=[1,2,3,4,5]
schema=["rollNo"]
rdd = sc.parallelize(data)

print(rdd.count())
print(sc.appName)
print(sc.master)
