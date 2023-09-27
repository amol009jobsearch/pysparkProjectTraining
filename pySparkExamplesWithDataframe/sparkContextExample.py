from pyspark import SparkConf, SparkContext
sc = SparkContext(master="local",appName="Spark Demo")
print(sc.textFile("C:\\Users\\PC\\PycharmProjects\\pysparkProjectTraining\\inputDataFile\\customerinfo.csv")
      .take(10))