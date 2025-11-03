from pyspark.sql import SparkSession

sc = SparkSession.builder.appName("partitioning").getOrCreate()

my_data = sc.read.format('csv')\
    .option('header', 'true')\
    .option('inferschema', 'true')\
    .load('/home/developer/Downloads/2010-summary.csv')

my_data.select("ORIGIN_COUNTRY_NAME").distinct().show()


my_data.write.option('header', 'true')\
    .partitionBy('ORIGIN_COUNTRY_NAME')\
    .mode("overwrite")\
    .csv("/home/developer/Downloads/partitioned_data")

my_data.show(5)
print(my_data.explain(extended=True))