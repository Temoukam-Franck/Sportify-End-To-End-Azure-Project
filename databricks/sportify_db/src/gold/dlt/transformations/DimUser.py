import dlt

@dlt.table
def dimuser_stg():
    df = spark.readStream.table("sportify_cata.silver.dimuser")
    return df