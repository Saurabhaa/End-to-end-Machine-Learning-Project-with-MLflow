#lets create it within init file just to makeit import easy
import os
import sys
import logging

# tells log time, what kind of log--info log , error log, then module if main or which file ,and the message we want to print
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#creation of logs folder, within that running_logs folder
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

#calling the basicConfig method from loggin
t# later calling file handler and stream handler  -first one create log file in desired path , second displys logs in terminal
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# The logger is created with the name “mlProjectLogger.”
logger = logging.getLogger("mlProjectLogger")