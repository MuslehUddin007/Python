import logging 
#Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "D:\\python\\Lumberjack.Log",level = logging.DEBUG,format = LOG_FORMAT,)
logger = logging.getLogger()

#Test the logger
logger.info("Our first message.")
print(logger.level)