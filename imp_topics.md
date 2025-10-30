#### Catalyst Optimizer
    - The Catalyst Optimizer is a fundamental component within Apache Spark, particularly crucial for Spark SQL and PySpark's DataFrame/Dataset APIs. Its primary function is to optimize the execution of queries and operations, leading to improved performance and efficiency.

    * How the Catalyst Optimizer Works:
        - Logical Plan Generation:
        When you submit a PySpark DataFrame operation or an SQL query, Spark's Catalyst Optimizer first 
        creates an "unresolved logical plan." This plan represents the operations you've requested without 
        considering the underlying data sources or specific execution details.

        - 
