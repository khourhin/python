# See http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python

import logging


# Use a basic configuration (with formatting)
#logging.basicConfig(level=logging.DEBUG)

# Levels available: debug, info, warning, error and critical

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.info("Some info")
logger.debug("Some debug")
logger.warning("Some warning")
logger.error('Some error')

################################################################################
# QUICK LOGGING TO BOTH FILE and STDERR !!!
################################################################################
# import logging
# logging.basicConfig(filename='example.log', level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler())


################################################################################
# OTHER SETUP
# WITH LOGGING FILES and 
################################################################################

# create a file handler
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.DEBUG)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

logger.info('Hello baby')
logger.debug('testing')
