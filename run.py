import sys
import signal
from datetime import datetime, timedelta

import constants as c
from utils.api import IfConfig
from utils.quartz import Scheduler
from utils.common import TimeParser, Logger

signal.signal(signal.SIGINT, Scheduler.stop)


def start(t_arg):
    """
    Start the process.

    IP checker scheduler trigger event at specified time given as a parameter.

    :param t_arg: All the times (format HH:MM:SS) separated by comma
    :return: Nothing
    """

    logger = Logger.get_logger()

    logger.info('START')

    run_times = TimeParser().parse(t_arg)

    scheduler = Scheduler()

    scheduler.run(run_times, IfConfig().what_is_my_ip)

    logger.info('END')


def generate_test_sample():
    """
    Generate 5 time samples with interval of 5 seconds

    :return: String times string separated by comma
    """

    now = datetime.today()
    samples = 5
    duplicates = 2
    interval_seconds = 5
    samples = [
        datetime.strftime(now + timedelta(seconds=(interval_seconds + (x if x >= duplicates else 1))), c.TIME_FORMAT)
        for x in range(samples)
    ]
    return ','.join(samples)


if __name__ == '__main__':
    """
    Entry point
    """

    if len(sys.argv) > 1:
        arg = sys.argv[1]

        if arg == 'TEST':
            arg = generate_test_sample()

        ####################
        # Start the Process
        ####################
        start(arg)
        ############
    else:
        print('''
Invalid arguments, example as follows:

    python3 run.py 09:15:25,11:58:23,13:45:09
''')
