from pyspark.sql import SparkSession

# dataframe.foramt()\
# .option()\
# .schema()\
# .load()

# format - Data File Format (csv, json, jdbc/odbc, table , parquet)
# If u dont specify, default is parquet
# Optional

# option - inferschema, mode, header
# header

# schema - manual schema u can pass
# optional

# load - path where our data is reside

# mode
# - FAIL_FAST - fail execution if malformed record
# - Dropmalformed - Drop the corrupted record
# - Permissive - Default
#                - Set null value to all corrupted fields

# /home/developer/Downloads

sc = SparkSession.builder.appName("readDataSet").getOrCreate()

flight_df = sc.read.format('csv')\
    .option('header', 'true')\
    .option('inferschema','true')\
    .option('mode','FAILFAST')\
    .load('/home/developer/Downloads/2010-summary.csv')

flight_df.show(5)
flight_df.printSchema()