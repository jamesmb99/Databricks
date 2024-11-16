# Databricks notebook source
# DBTITLE 1,List Secret Scopes
class listSecretScopes:
  
  def __init__(self):
    
    import pandas as pd

    self.scopes = dbutils.secrets.listScopes()
    data = []
  
    for scope in self.scopes:
      secrets_list = dbutils.secrets.list(scope.name)
    
      if secrets_list:
        for secret in secrets_list:
          data.append((scope.name, secret.key))
      else:
        data.append((scope.name, "No secrets"))

    df = pd.DataFrame(data, columns=["Scope", "Secret"])
    
    display(df)


# COMMAND ----------

listSecretScopes()
