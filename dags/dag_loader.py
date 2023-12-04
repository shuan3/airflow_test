from airflow import DAG

import dagfactory
# dag_factory = dagfactory.DagFactory("~/dags/example_dag.yml")

# dag_factory.clean_dags(globals())
# dag_factory.generate_dags(globals())


# 'airflow' word is required for the dagbag to parse this file
# from dagfactory import load_yaml_dags

# load_yaml_dags(globals_dict=globals(), suffix=['_trump.yaml'])

# import os

# CUR_DIR = os.path.abspath(os.path.dirname(__file__))
# print(CUR_DIR)

# dag_factory = dagfactory.DagFactory(f"{CUR_DIR}/trump.yaml")
# dag_factory.clean_dags(globals())
# dag_factory.generate_dags(globals())



import os

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
print(CUR_DIR)

dag_factory = dagfactory.DagFactory(f"{CUR_DIR}/trump.yaml")

dag_factory.clean_dags(globals())
dag_factory.generate_dags(globals())


# Temporary to check if loading config works with same path.
# with open(f"{CUR_DIR}//Fuck_trump.yaml", "r") as stream:
#     try:
#         import yaml
#         configYaml = yaml.safe_load(stream)
#         print(configYaml)
#     except yaml.YAMLError as exc:
#         print(exc)