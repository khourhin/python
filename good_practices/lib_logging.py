# See http://victorlin.me/posts/2012/08/26/good-logging-practice-in-pythonk

import logging

logging.basicConfig(level=logging.INFO)
# Levels available: debug, info, warning, error and critical

logger = logging.getLogger(__name__)

logger.info("Hello there !")
logger.info("Here is the '__name__' variable: %s" % __name__)
logger.debug("This is a debugging message")
logger.warning("Some warning message")

logger.info("And it's done now, see you next time !")

################################################################################
# OTHER SETUP
# WITH LOGGING FILES
################################################################################

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler

handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

logger.info('Hello baby')
