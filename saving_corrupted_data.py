from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType, StructField, StructType

sc = SparkSession.builder.appName("handling").getOrCreate()

corrupted_data_schema = StructType(
    [
        StructField('id', IntegerType(), True),
        StructField('name', StringType(), True),
        StructField('role', StringType(), True),
        StructField('gender', StringType(), True),
        StructField('address', StringType(), True),
        StructField('_corrupt_record', StringType(), True)
    ]
)

# my_file = sc.read.format('csv')\
#     .option('header', 'true')\
#     .option('inferschema', 'false')\
#     .schema(corrupted_data_schema)\
#     .load('/home/developer/Downloads/temp_data.txt')

# Store in a file
my_file = sc.read.format('csv')\
    .option('header', 'true')\
    .option('inferschema', 'false')\
    .schema(corrupted_data_schema)\
    .option('badRecordsPath', '/home/developer/Downloads/corrupted_records')\
    .load('/home/developer/Downloads/temp_data.txt')

my_file.show()