# Databricks notebook source
notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()

# Extract the directory path
home_dir = "/".join(notebook_path.split("/")[:-1])
print(home_dir)

add_workspace_dir = f"/Workspace{home_dir}"
print(add_workspace_dir)

# Check if the directory exists before listing its contents
try:
    contents = dbutils.fs.ls(add_workspace_dir)
    for item in contents:
        print(item)
except Exception as e:
    print(f"Error: {e}")

