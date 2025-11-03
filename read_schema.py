# How to read schema using python
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType, StructField, StructType

sc = SparkSession.builder.appName("schema").getOrCreate()

# creating_schema
my_schema = StructType(
    [
        StructField('DEST_COUNTRY_NAME_O', StringType(), True),
        StructField('ORIGIN_COUNTRY_NAME_O', StringType(), True),
        StructField('count_O', IntegerType(), True)
    ]
)

my_file = sc.read.format('csv')\
    .option('header', 'false')\
    .option('skipRows', 1)\
    .option('inferschema', 'false')\
    .schema(my_schema)\
    .option('mode', 'PERMISSIVE')\
    .load('/home/developer/Downloads/2010-summary.csv')

my_file.show(5)
