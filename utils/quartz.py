import time
import sched
from datetime import datetime

from utils.common import Logger


class Scheduler(object):
	"""Scheduler class to schedule jobs"""
	s = None
	events = []

	def __init__(self):
		super(Scheduler, self).__init__()
		self.logger = Logger.get_logger()
		self.s = sched.scheduler()
		self.raw_times = None

	def _calculate_interval(self):
		"""
		Calculate next run intervals to schedule job

		:return: Array of interval detail objects
		"""
		self.logger.info(f'Times: {self.raw_times}')

		ct = datetime.strptime(time.strftime("%H:%M:%S", time.localtime()), "%H:%M:%S")
		self.logger.debug(f'Current time: {ct.time()}')

		intervals = []
		for t in self.raw_times:
			# convert time string to datetime
			nt = datetime.strptime(t, "%H:%M:%S")

			# get time difference
			delta = nt - ct
			total_seconds = int(delta.total_seconds())
			self.logger.debug(f'   Next time: {t}, Delta seconds: {total_seconds}')

			intervals.append({
				'time': t,
				'seconds': total_seconds,
				'runs': self.raw_times[t]
			})

		return intervals

	def _schedule(self, callback):
		"""
		Scheduler process

		:param callback: A function to be triggered on scheduled interval
		:return: Nothing
		"""

		intervals = self._calculate_interval()

		self.logger.debug(f'Intervals: {intervals}')

		ct = time.monotonic()

		for s_obj in intervals:
			sec = s_obj['seconds']
			if sec > 0:
				abs_seconds = ct + sec
				for x in range(s_obj['runs']):
					self.logger.debug(f'{s_obj["time"]} {ct} - {sec} - {x}')

					# Add event in queue for execution
					_e = self.s.enterabs(abs_seconds, 1, callback)

					self.events.append(_e)
			else:
				self.logger.warn(f'{int(-1 * sec)} second(s) elapsed, skipping...')

		self.logger.debug(self.s.queue)

	def run(self, times, callback):
		"""

		:param times: Times dictionary
		:param callback: A function to be triggered on scheduled interval
		:return: Nothing
		"""

		if callback is None:
			self.logger.error('Invalid job configured to schedule')
		else:
			self.raw_times = times
			self._schedule(callback)

			if self.s.queue:
				self.logger.info(f'Total {len(self.s.queue)} jobs scheduled to run')
				self.s.run()
			else:
				self.logger.info('No jobs scheduled to run')

	def __del__(self):
		if self.s:
			self.s.empty()
			self.s = None

	@staticmethod
	def stop(sig=None, frm=None):
		"""
		Stop the scheduler

		:param sig: signal
		:param frm: frame
		:return: Nothing
		"""
		# print('Cancelling events gracefully')
		if Scheduler.s:
			for e in Scheduler.events:
				Scheduler.s.cancel(e)
			Scheduler.s.empty()
