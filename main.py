from sensor.exception import SensorException
import os 
import sys
from sensor.logger import logging
from sensor.utils import dump_csv_file_to_mongodb_collection

# def test_exception():
#     try:
#         logging.info("ki yaha p bhaiaa ek error ayegi diveision by zero wali error ")
#         a=1/0
#     except Exception as e:
#        raise SensorException(e,sys) 



if __name__ == "__main__":
    file_path=r"E:\Nilesh Shelke\Documents\Live_Sensor\aps_failure_training_set1.csv"
    database_name="ABS"
    collection_name ="sensor"
    dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)




  












    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)


# from sensor.exception import SensorException
# import os
# import sys
# from sensor.logger import logger
# from sensor.utils import dump_csv_file_to_mongodb_connection
# from sensor.config import mongo_client

# # def test_exception():
# #     try:
# #         logger.info("Attempting to perform division")
# #         a = 1 / 0
# #     except Exception as e:
# #         raise SensorException(e, sys) from e

# # if __name__ == "__main__":
# #     try:
# #         test_exception()
# #     except SensorException as se:
# #         print(se)

# if __name__=="__main__":
#     file_path = r"E:\Nilesh Shelke\Documents\Live_Sensor\aps_failure_training_set1.csv"
#     db_name = "your_database_name"
#     collection_name = "your_collection_name"

#     dump_csv_file_to_mongodb_connection(file_path, mongo_client, db_name, collection_name)

