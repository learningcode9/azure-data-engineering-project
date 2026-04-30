# Bronze to Silver Transformation

from pyspark.sql.functions import *

# Read from Bronze
df = spark.read.json("abfss://bronze@datalakesravanidemo.dfs.core.windows.net/users/raw/")

# Basic Transformation (flatten example)
df_clean = df.select(
    col("id"),
    col("name"),
    col("email"),
    col("phone"),
    col("username")
)

# Write to Silver (Delta format)
silver_path = "abfss://silver@datalakesravanidemo.dfs.core.windows.net/users/"

df_clean.write.mode("overwrite").format("delta").save(silver_path)
