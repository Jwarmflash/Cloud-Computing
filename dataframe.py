# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 16:31:38 2024

@author: Jake Warmflash
"""

import sys

from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("Dataframe_PySpark").getOrCreate()

# Create a simple local data.frame
localDF = [("John", 19), ("Smith", 23), ("Sarah", 18)]

# Convert local data frame to a SparkDataFrame
df = spark.createDataFrame(localDF, ["name", "age"])

# Print its schema
df.printSchema()

# Create a DataFrame from a JSON file
path = "examples/src/main/resources/people.json".format(spark.sparkContext.getConf().get("spark.home"))
peopleDF = spark.read.json(path)
peopleDF.printSchema()

# Register this DataFrame as a table.
peopleDF.createOrReplaceTempView("people")

# SQL statements can be run by using the sql methods
teenagers = spark.sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")


# Call collect to get a local data frame
teenagersLocalDF = teenagers.collect()

# Print the teenagers in our dataset
for i in teenagersLocalDF:
    print(i)

# Stop the SparkSession now
spark.stop()
