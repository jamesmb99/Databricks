# Databricks notebook source
class ListCatalogs:

  def __init__(self):
    
    catalogs_info = [(catalog.name,) for catalog in spark.catalog.listCatalogs()]
    
    catalogs_df = spark.createDataFrame(catalogs_info, ["Catalog Name"])
    
    display(catalogs_df)
    


# COMMAND ----------

ListCatalogs()
