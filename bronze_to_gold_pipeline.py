from pyspark.sql.functions import col

# Bronze → Silver
df = spark.read.json("abfss://bronze@datalakesravanidemo.dfs.core.windows.net/users/raw/")

df_clean = df.select(
    col("id"),
    col("name"),
    col("email"),
    col("phone"),
    col("username")
).dropDuplicates(["id"]).fillna("NA")

silver_path = "abfss://silver@datalakesravanidemo.dfs.core.windows.net/users/"
df_clean.write.mode("overwrite").format("delta").save(silver_path)

# Silver → Gold
df_gold = df_clean.select("id", "name", "email")

gold_path = "abfss://gold@datalakesravanidemo.dfs.core.windows.net/users/"
df_gold.write.mode("overwrite").format("delta").save(gold_path)
