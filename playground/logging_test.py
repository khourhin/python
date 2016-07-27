#! /usr/bin/python

import logging
import logging.handlers
import config

LOGFILE="test.log"
LOGFILEBYTES= 500*1024

logging.getLogger().setLevel( logging.DEBUG )

def main_function():

    # get logger
    logger = logging.getLogger()
    
    # create file handler
    ch = logging.handlers.RotatingFileHandler(LOGFILE, mode='a', maxBytes=LOGFILEBYTES, backupCount=5 )

#    ch.setLevel( logging.DEBUG )

    # create formatter
    formatter = logging.Formatter(
                fmt='%(asctime)s -%(levelname)s- %(message)s',
        datefmt='%Y%m%d %H:%M:%S' )

    # add formatter to ch
    ch.setFormatter( formatter )

    # add ch to logger
    logger.addHandler( ch )

#    logging.captureWarnings( True )


    print logger.getEffectiveLevel()

def mytest():
    logging.info("hahahhahhah")
    logging.info( "something happen %s %d", 'string', 5 )
    logging.warning("test")
    logging.debug("this is a debug")

main_function()
mytest()
