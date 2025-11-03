from pyspark.sql import SparkSession

sc = SparkSession.builder.appName("partitioning").getOrCreate()


data = [(1, "Alice", "India"),
        (2, "Bob", "USA"),
        (3, "Cathy", "India"),
        (4, "David", "UK"),
        (5, "Eve", "India")]

df = sc.createDataFrame(data, ["user_id", "name", "country"])

df.write\
    .bucketBy(2, "user_id")\
    .sortBy("user_id")\
    .saveAsTable("bucketed_users")

sc.sql("DESCRIBE FORMATTED bucketed_users").show(truncate=False)
# df.write.bucketBy(4, "user_id").sortBy("user_id").mode("overwrite").save("/home/developer/Downloads/bucketed_path")
