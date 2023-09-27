from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
           .appName('SparkByExamples.com') \
           .config("spark.jars", "mysql-connector-java-8.0.13.jar") \
           .getOrCreate()

df=spark.read.option("inferSchema","true").option("header","true").csv(path="C:\\Users\\PC\\PycharmProjects\\pysparkProjectTraining\\inputDataFile\\customerinfo.csv")
df.count()
input("Press enter to terminate")
spark.stop()
