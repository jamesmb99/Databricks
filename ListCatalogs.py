# Databricks notebook source
class ListCatalogs:
    """
    A class to retrieve and display UC catalogs.
    """

    def get_catalogs(self):
        """
        Retrieves UC catalogs as a DataFrame.

        Returns:
            DataFrame: A Spark DataFrame containing catalog names.
        """
        try:
            catalogs_info = [(catalog.name,) for catalog in spark.catalog.listCatalogs()]
            return spark.createDataFrame(catalogs_info, ["Catalog Name"])
        except Exception as e:
            print("Error retrieving catalogs:", e)
            return None

    def display_catalogs(self):
        """
        Displays the Spark catalogs in a tabular format.
        """
        catalogs_df = self.get_catalogs()
        if catalogs_df:
            display(catalogs_df)


    


# COMMAND ----------

catalog_list = ListCatalogs()

# Display catalogs
catalog_list.display_catalogs()

# Get catalogs DataFrame for further processing
# catalogs_df = catalog_list.get_catalogs()
