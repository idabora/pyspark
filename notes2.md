### Reading mode in pyspark
    # permissive:
    The default mode. If a record cannot be parsed, the affected fields are set to null, and the entire malformed record can be stored in a 
    corrupt_record column. 

    # dropmalformed:
    Silently drops any records that have parsing errors. Only successfully parsed records are kept. 

    # failfast:
    Stops the entire read operation immediately if it encounters any record with a parsing error. 

