import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" # time: error level : module/folder name : msg

log_dir = "logs" # create log folder to save logging
log_filepath = os.path.join(log_dir,"running_logs.log") # create file running_logs.log to save data
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # create log folder for each file
        logging.StreamHandler(sys.stdout) #print login in terminal
    ]
)

logger = logging.getLogger("mlProjectLogger")