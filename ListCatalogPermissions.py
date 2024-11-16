# Databricks notebook source
# MAGIC %run ./ListCatalogs

# COMMAND ----------

class ListCatalogPermissions():

    """
    A class to retrieve and display permissions.
    """

    def __init__(self):

        # Create an instance of the ListCatalogs class
        self.catalog_list = ListCatalogs()

    def get_permissions(self, catalog_name):

        """
        Retrieves permissions for a given catalog as a DataFrame.

        Args:
            catalog_name (str): The name of the catalog to retrieve permissions for.

        Returns:
            DataFrame: A Spark DataFrame containing permissions.
        """

        try:
            query = f"SHOW GRANT ON CATALOG {catalog_name}"
            permissions_df = spark.sql(query)
            return permissions_df
        except Exception as e:
            print("Error retrieving permissions:", e)
            return None

    def display_permissions(self, catalog_name):

        """
        Displays the permissions for a given catalog in a tabular format.

        Args:
            catalog_name (str): The name of the catalog to display permissions for.
        """

        permissions_df = self.get_permissions(catalog_name)
        if permissions_df:
            display(permissions_df)

    def display_all_catalog_permissions(self):
      
        """
        Displays the permissions for all catalogs.
        """
        catalogs_df = self.catalog_list.get_catalogs()
        if catalogs_df:
            catalogs = catalogs_df.collect()
            for row in catalogs:
                catalog_name = row["Catalog Name"]
                print(f"Permissions for catalog: {catalog_name}")
                self.display_permissions(catalog_name)

# Instantiate Permissions class and display permissions for all catalogs
permissions = ListCatalogPermissions()
permissions.display_all_catalog_permissions()
