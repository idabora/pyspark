from pyspark.sql import SparkSession

sc = SparkSession.builder.appName('skewingExample').getOrCreate()

# Number of rows
total_rows = 100000

# Create a skewed dataset: 90% of rows have key 'A', rest are random keys
data = [("A", i) for i in range(int(total_rows * 0.9))]  # skewed key
data += [(chr(68 + i % 5), i) for i in range(int(total_rows * 0.1))]  # other keys B-F

# Create DataFrame
df = sc.createDataFrame(data, ["key", "value"])
print(df.rdd.getNumPartitions())
# Show top keys to see skew
df.groupBy("key").count().orderBy("count", ascending=False).show()