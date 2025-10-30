#### Pyspark
    - Pyspark is the python API for Apache spark, which is a fast, opensource, distributed computing system for processing large scale data analytics. 
    
    * features of apache spark
        - Spark primarily uses in-memory computing.
        - Lazy evaluation: Spark postpones the execution of operations (transformations) until an action explicitly triggers it.
        - Fault tolerance: Spark uses a logical plan (or "lineage") of transformations to track how data is derived. If a partition of a Resilient Distributed Dataset (RDD) is lost, it can be automatically rebuilt from its original state.

    * whats the realtion of pyspark with bigdata
        - PySpark is a critical tool for working with big data because it provides a Python-based interface 
        for Apache Spark's powerful, distributed processing engine. This relationship allows data 
        professionals familiar with Python to easily handle massive datasets that are too large for a single 
        machine.

    Q. How to indetify this is a big data or not?
    A. 3 V's of Big Data
        1. Velocity - /s, /min
        2. Variety - Structured, semi-structured, un-structured
        3. Volume - 5GB, 1TB, 5TB
    
    * Issues in Big Data
        1. Storage
        2. Processing

#### Data Structures
    - Spark offers three main data structures: RDDs (Resilient Distributed Datasets),
    DataFrames, and Datasets. Understanding their differences is key to leveraging Spark
    effectively.

    # RDD
        - An RDD is an immutable distributed collection of objects that can be processed in parallel across a cluster. Think of it as a “fault-tolerant list” that lives across multiple machines.
    # Dataframe
        - A DataFrame in Spark is a distributed collection of data organized into named columns, just like a table in a database or a Pandas DataFrame — but it runs in parallel across a cluster.
    # 
    

##### Apache spark
    - Apache Spark is a fast, open-source, distributed computing system for processing large-scale data
    analytics.
    * 


┌─────────────────────────────────────────────────────────────────────────────────┐
│                              DRIVER PROGRAM                                     │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐    │
│  │                            SPARK SESSION                                │    │
│  │  appName: "MyApp", master: "yarn", config: {shuffle.partitions: 200}    │    │
│  │                                                                         │    │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐  │    │
│  │  │  SPARK CONTEXT  │  │   SQL CONTEXT   │  │  STREAMING CONTEXT      │  │    │
│  │  │                 │  │                 │  │                         │  │    │
│  │  │ • Spark Config  │  │ • DataFrame API │  │ • DStream Operations    │  │    │
│  │  │ • RDD Operations│  │ • SQL Queries   │  │ • Checkpointing         │  │    │
│  │  │ • Job Scheduling│  │ • Catalyst Opt  │  │ • Window Operations     │  │    │
│  │  │ • DAG Scheduler │  │ • Tungsten Exec │  │                         │  │    │
│  │  │ • Task Scheduler│  │                 │  │                         │  │    │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────────────┘  │    │
│  │                                                                         │    │
│  │  ┌─────────────────────────────────────────────────────────────────┐    │    │
│  │  │                     DAG SCHEDULER                               │    │    │
│  │  │  • Logical Plan → Physical Plan → Stages → Tasks                │    │    │
│  │  │  • Optimizes Execution Plan                                     │    │    │
│  │  │  • Handles Fault Tolerance                                      │    │    │
│  │  └─────────────────────────────────────────────────────────────────┘    │    │
│  │                                                                         │    │
│  │  ┌─────────────────────────────────────────────────────────────────┐    │    │
│  │  │                     BLOCK MANAGER                               │    │    │
│  │  │  • Manages Data Caching (Memory/Disk)                           │    │    │
│  │  │  • Tracks Block Locations                                       │    │    │
│  │  │  • Handles Data Replication                                     │    │    │
│  │  └─────────────────────────────────────────────────────────────────┘    │    │
│  └─────────────────────────────────────────────────────────────────────────┘    │
│                                                                                 │
│  ┌─────────────────────────┐  ┌─────────────────────────┐                       │
│  │     SHUFFLE MANAGER     │  │   BROADCAST MANAGER     │                       │
│  │                         │  │                         │                       │
│  │ • Manages Shuffle Data  │  │ • Distributes Broadcast │                       │
│  │ • Handles Data Transfer │  │   Variables             │                       │
│  │ • Disk Spill Management │  │ • Efficient Data Sharing│                       │
│  └─────────────────────────┘  └─────────────────────────┘                       │
└─────────────────────────────────────┬───────────────────────────────────────────┘
                                      │
                          ┌───────────▼───────────┐
                          │    CLUSTER MANAGER    │
                          │                       │
                          │  ┌─────────────────┐  │
                          │  │   RESOURCE      │  │
                          │  │   SCHEDULER     │  │
                          │  │                 │  │
                          │  │ • YARN          │  │
                          │  │ • Standalone    │  │
                          │  │ • Kubernetes    │  │
                          │  │ • Mesos         │  │
                          │  └─────────────────┘  │
                          └───────────┬───────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          │                           │                           │
    ┌─────▼───────┐             ┌─────▼───────┐             ┌─────▼───────┐
    │  WORKER     │             │  WORKER     │             │  WORKER     │
    │   NODE 1    │             │   NODE 2    │             │   NODE N    │
    │             │             │             │             │             │
    │ ┌─────────┐ │             │ ┌─────────┐ │             │ ┌─────────┐ │
    │ │EXECUTOR │ │             │ │EXECUTOR │ │             │ │EXECUTOR │ │
    │ │         │ │             │ │         │ │             │ │         │ │
    │ │ ┌─────┐ │ │             │ │ ┌─────┐ │ │             │ │ ┌─────┐ │ │
    │ │ │TASK │ │ │             │ │ │TASK │ │ │             │ │ │TASK │ │ │
    │ │ │ 1   │ │ │             │ │ │ 1   │ │ │             │ │ │ 1   │ │ │
    │ │ └─────┘ │ │             │ │ └─────┘ │ │             │ │ └─────┘ │ │
    │ │         │ │             │ │         │ │             │ │         │ │
    │ │ ┌─────┐ │ │             │ │ ┌─────┐ │ │             │ │ ┌─────┐ │ │
    │ │ │TASK │ │ │             │ │ │TASK │ │ │             │ │ │TASK │ │ │
    │ │ │ 2   │ │ │             │ │ │ 2   │ │ │             │ │ │ 2   │ │ │
    │ │ └─────┘ │ │             │ │ └─────┘ │ │             │ │ └─────┘ │ │
    │ │         │ │             │ │         │ │             │ │         │ │
    │ └─────────┘ │             │ └─────────┘ │             │ └─────────┘ │
    │             │             │             │             │             │
    │ ┌─────────┐ │             │ ┌─────────┐ │             │ ┌─────────┐ │
    │ │BLOCK    │ │             │ │BLOCK    │ │             │ │BLOCK    │ │
    │ │MANAGER  │ │             │ │MANAGER  │ │             │ │MANAGER  │ │
    │ │         │ │             │ │         │ │             │ │         │ │
    │ │• Memory │ │             │ │• Memory │ │             │ │• Memory │ │
    │ │  Cache  │ │             │ │  Cache  │ │             │ │  Cache  │ │
    │ │• Disk   │ │             │ │• Disk   │ │             │ │• Disk   │ │
    │ │  Store  │ │             │ │  Store  │ │             │ │  Store  │ │
    │ └─────────┘ │             │ └─────────┘ │             │ └─────────┘ │
    │             │             │             │             │             │
    │ ┌─────────┐ │             │ ┌─────────┐ │             │ ┌─────────┐ │
    │ │SHUFFLE  │ │             │ │SHUFFLE  │ │             │ │SHUFFLE  │ │
    │ │SERVICE  │ │             │ │SERVICE  │ │             │ │SERVICE  │ │
    │ │         │ │             │ │         │ │             │ │         │ │
    │ │• Shuffle│ │             │ │• Shuffle│ │             │ │• Shuffle│ │
    │ │  Write  │ │             │ │  Write  │ │             │ │  Write  │ │
    │ │• Shuffle│ │             │ │• Shuffle│ │             │ │• Shuffle│ │
    │ │  Read   │ │             │ │  Read   │ │             │ │  Read   │ │
    │ └─────────┘ │             │ └─────────┘ │             │ └─────────┘ │
    └─────────────┘             └─────────────┘             └─────────────┘

                                      │
                          ┌───────────▼───────────┐
                          │   DATA SOURCES        │
                          │                       │
                          │  ┌─────────────────┐  │
                          │  │ HDFS/S3/GCS     │  │
                          │  │                 │  │
                          │  │ • Parquet       │  │
                          │  │ • CSV/JSON      │  │
                          │  │ • Avro/ORC      │  │
                          │  └─────────────────┘  │
                          │                       │
                          │  ┌─────────────────┐  │
                          │  │  DATABASES      │  │
                          │  │                 │  │
                          │  │ • MySQL/Postgres│  │
                          │  │ • Cassandra     │  │
                          │  │ • MongoDB       │  │
                          │  └─────────────────┘  │
                          │                       │
                          │  ┌─────────────────┐  │
                          │  │  STREAMING      │  │
                          │  │                 │  │
                          │  │ • Kafka         │  │
                          │  │ • Kinesis       │  │
                          │  │ • Socket        │  │
                          │  └─────────────────┘  │
                          └───────────────────────┘


#### Driver Program
    - A driver program is the entry point of a Spark application — it’s where your main() function runs.
#### SparkSession
    - A SparkSession is the entry point to use Spark SQL, DataFrame, and Dataset APIs in PySpark (or Scala/
    Java Spark).
    - It’s basically the single unified gateway to all Spark functionalities.
    - SparkSession = the “brain” object that connects your driver program to the Spark cluster.
#### Cluster Manager
    - The cluster manager is the resource allocator that provides Spark with the computational resources 
    needed to run jobs across a distributed cluster.

#### DAG
    When you write transformations like this:
        df = spark.read.csv("data.csv")
        df2 = df.filter(df.age > 30)
        df3 = df2.select("name", "age")
        df3.show()
    Spark doesn’t execute each line immediately.

    Instead, it:

    - Records each transformation (read → filter → select) into a logical plan.
    - Builds a DAG of transformations showing how data should flow.
    - When an action (like .show(), .count(), .collect()) is called — Spark:
        * Submits the DAG to the scheduler.
        * Divides it into stages (based on shuffle boundaries).
        * Converts each stage into tasks that run on executors.

    - Graph: Each node represents a computation (like a map, filter, join, etc.), and edges represent dependencies between those computations.



    | Level     | Meaning                                   | Example                          |
    | --------- | ----------------------------------------- | -------------------------------- |
    | **DAG**   | Complete logical flow of transformations  | `read → filter → join → write`   |
    | **Stage** | Group of tasks without shuffle dependency | `map`, `filter`                  |
    | **Task**  | Unit of work executed on one partition    | Apply `filter()` on partition #3 |


    | Term             | Meaning                                                               |
    | ---------------- | --------------------------------------------------------------------- |
    | **Logical Plan** | Blueprint of transformations, recorded lazily                         |
    | **DAG**          | Execution plan derived from the logical plan, respecting dependencies |
    | **Stage**        | Subset of DAG that can run **without shuffling**                      |
    | **Task**         | Unit of work for a partition, runs on a core/thread in an executor    |
