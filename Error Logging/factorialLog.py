import logging, os

# level applied to disable() (DEBUG, INFO, WARNING, ERROR, CRITICAL) __    
        # precludes all smaller ranked logging messages from appearing in the script
#logging.disable(logging.CRITICAL)

"""
#####################################################################################
#   Logging Levels                                                                  #
#       -- like a hierarchy for the 'level' parameter in logging.basicConfig()'     #
#                                                                                   #
#####################################################################################

logging.debug()    #smallest rank...Everything == debug and 'above' debug will be printed if .DEBUG is used in Config
logging.info("") 
logging.warning("")
logging.error("")
logging.critical("")
"""
#Search the cwd for fresh filepath names 
error_file_num = 1
while True:        #os.path.abspath('.') is the directory which contains the current .py file
    error_log_filepath = os.path.join(  #create the file path for the error log
        os.path.abspath('.'),
        ("factorialLogpy_errorfile_" + str(error_file_num) + ".txt")
    ) 

    if not os.path.exists(error_log_filepath): #if the filepath is novel, then it's good to go
        break
    error_file_num += 1 #if the filepath isn't novel, iterate it's basename number




#the parameter 'filename = error_log_filepath' saves the logging content to novel files 
logging.basicConfig(filename = error_log_filepath, level = logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(message)s")
logging.debug("Start of program")

############################################################################################################
#BUG: Not a bug, but an idea... Repleace the factorial() function with something that is useful for tracking
def factorial(n):
    total = 1
    logging.debug("Start of Factorial function. Total = {}".format(total))

    for i in range(1, n + 1):
        total *= i
        logging.debug("The value of i is {}. Total is {}".format(i , total))

    logging.debug("End of factorial loop")
    
    return total

factorial(5)
logging.critical("End of the entire script")
