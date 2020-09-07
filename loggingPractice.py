import logging
import math

#create and config logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "Mylog.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')
logger = logging.getLogger()

#Test Logger
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


def quadratic_formula(a, b, c):
    """return the solution  of ´cuadratic equation ax2 + bx + c = 0 """
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    #compute the discriminants
    logger.debug("# Compute the discriminants")
    disc = b**2 - 4*a*c

    #compute two roots
    logger.debug("# Compute the Two Roots")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b + math.sqrt(disc)) / (2*a)

    #returns the roots
    logger.debug("# Return the roots")
    return(root1, root2)

roots = quadratic_formula(1, 0, -4)
print(roots)

#Math Domains Error
roots = quadratic_formula(1, 0, 1)
print(roots)