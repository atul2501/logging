import logging

## logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArithmethicApp")

def add(a,b):
    result=(a+b)
    logger.debug(f'Adding {a} +{b} ={result}')
    return result

def subtract(a,b):
    result=(a-b)
    logger.debug(f'Substract {a}-{b}={result}')

def multiply(a,b):
    result=(a*b)
    logger.debug(f'Multiplying {a} *{b}={result}')

def divide(a,b):
    try:
        result=a/b
        logger.debug(f'devinding {a} / {b} ={result}')
        return result
    except ZeroDivisionError:
        logger.error('Divison by Zero error')
        return None
    
add(10,15)
subtract(15,10)
multiply(10,20)
divide(20,2)

