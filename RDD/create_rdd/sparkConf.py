from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local[2]").setAppName("rddByConf")

sc=SparkContext(conf=conf)
rdd=sc.parallelize([1,2,3,4])

print("appName = ",sc.appName)
print("master = ",sc.master)
#print(rdd.collect())

# sc1 = SparkContext(appName="rdd2",master="local[*]")
# countryRdd = sc1.parallelize(["India","Aus","New","USA"])
# print(countryRdd.collect())
