from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("accumulator").getOrCreate()

sc = spark.sparkContext

acc_count = sc.accumulator(0)
rdd = sc.parallelize([
    {"user_id": "101", "amount": "250"},
    {"user_id": "102", "amount": None},
    {"user_id": None, "amount": "400"}, 
    {"user_id": "104", "amount": "abc"},  
])


def validate(record):
    global acc_count
    try:
        if not record["user_id"] or not record["amount"].isdigit():
            acc_count.add(1)
            return None
        return record
    except Exception:
        acc_count.add(1)
        return None


valid_records = rdd.map(validate)
valid_records.collect()
print(acc_count)