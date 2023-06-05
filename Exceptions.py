# Exceptions.

'''
Exception caluses:
try:
    Runs first
    <code>
except:
    Runs if exception occurs in try block
    <code>
else:
    Executes if try block *succeeds*
    <code>
finally:
    This code *always* executes
    <code>
'''
# 1. Write function that reads binary file and returns data.
# Measure time required ( cloud service common practice).

import logging
from math import log
import time
# Create logger
logging.basicConfig(filename='C:\\python_lesson\\problems.log',
level=logging.DEBUG)
logger=logging.getLogger()

def read_file_timed(path):
    '''Return the content of the file at 'path' and measure time required.'''
    start_time=time.time()
    try:
        f=open(path,mode='rb')
        data=f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
    else:
        f.close()
    finally:
        stop_time=time.time()
        dt=start_time-start_time
        logger.info('Time required for {file} = {time}'.format(file=path,
        time=dt))

# Test
data=read_file_timed('C:\\python_lessons\\audio_file.wav') # 45 MB file