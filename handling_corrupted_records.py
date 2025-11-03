from pyspark.sql import SparkSession

sc = SparkSession.builder.appName("data_handling").getOrCreate()
my_data = sc.read.format('csv')\
    .option('header', 'true')\
    .option('inferschema', 'true')\
    .option('mode', 'DROPMALFORMED')\
    .load('/home/developer/Downloads/temp_data.txt')

my_data.show(5)