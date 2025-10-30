# from pyspark import SparkContext

# sc = SparkContext('local', 'ParallelizeExample')
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# # data = [(1, 'anurodh'), (2, "arpit")]
# rdd = sc.parallelize(my_list)
# print(rdd.collect())

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("dataframe").getOrCreate()

data = [(1, 'anurodh'), (2, "arpit")]
column = ['id', 'name']
df = spark.createDataFrame(data, column)
df.show()
df.explain(extended=True)
