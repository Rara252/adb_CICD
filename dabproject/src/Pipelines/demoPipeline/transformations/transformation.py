from pyspark import pipelines as dp

@dp.materialized_view(
    comment="Materialized view of transaction data from bronze layer"
)
def transaction_view():
    return spark.read.table("retail_q.blobe_bronze.transaction")