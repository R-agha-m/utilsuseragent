from random import randrange
# from ..logger.logger import logger
from django_project.settings import USERAGENT

# report = logger(10)

# ------------------------------------------------------------------------------------------------------- old user agent
# Mozilla/5.0 (Windows NT 10.0; Win64; x64)
# AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/87.0.4280.88
# Safari/537.36
# Edg/87.0.664.60'

# awk_1 = '537'
# ch_1 = '87'
# s_1 = '537'
# ed_1 = '87'
# ed_2 = "0"

# ------------------------------------------------------------------------------------------------------- new user agent
# Mozilla/5.0 (X11; Linux x86_64)
# AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/96.0.4664.18
# Safari/537.36
# Edg/96.0.1054.5

awk_1 = USERAGENT['PC_USERAGENT']['awk_1']
ch_1 = USERAGENT['PC_USERAGENT']['ch_1']
s_1 = USERAGENT['PC_USERAGENT']['s_1']
ed_1 = USERAGENT['PC_USERAGENT']['ed_1']
ed_2 = USERAGENT['PC_USERAGENT']['ed_2']


class PcUserAgentCreator:
    def __init__(self):
        # report.debug('')
        self.user_agent_template = "Mozilla/5.0 " \
                                   "(Windows NT 10.0; Win64; x64) " \
                                   "AppleWebKit/{awk_1}.{awk_2} (KHTML, like Gecko) " \
                                   "Chrome/{ch_1}.{ch_2}.{ch_3}.{ch_4} " \
                                   "Safari/{s_1}.{s_2} " \
                                   "Edg/{ed_1}.{ed_2}.{ed_3}.{ed_4}"

        self._inputs = {}

    def perform(self):
        # report.debug('')
        self._select_awk_1()
        self._select_awk_2()
        self._select_ch_1()
        self._select_ch_2()
        self._select_ch_3()
        self._select_ch_4()
        self._select_s_1()
        self._select_s_2()
        self._select_ed_1()
        self._select_ed_2()
        self._select_ed_3()
        self._select_ed_4()
        return self._create_string()

    def _select_awk_1(self):
        # report.debug('')
        self._inputs['awk_1'] = awk_1

    def _select_awk_2(self):
        # report.debug('')
        self._inputs['awk_2'] = str(randrange(30, 37))

    def _select_ch_1(self):
        # report.debug('')
        self._inputs['ch_1'] = ch_1

    def _select_ch_2(self):
        # report.debug('')
        self._inputs['ch_2'] = str(randrange(0, 10))

    def _select_ch_3(self):
        # report.debug('')
        self._inputs['ch_3'] = str(randrange(1000, 10000))

    def _select_ch_4(self):
        # report.debug('')
        self._inputs['ch_4'] = str(randrange(0, 1000))

    def _select_s_1(self):
        # report.debug('')
        self._inputs['s_1'] = s_1

    def _select_s_2(self):
        # report.debug('')
        self._inputs['s_2'] = str(randrange(30, 37))

    def _select_ed_1(self):
        # report.debug('')
        self._inputs['ed_1'] = ed_1

    def _select_ed_2(self):
        # report.debug('')
        self._inputs['ed_2'] = ed_2

    def _select_ed_3(self):
        # report.debug('')
        self._inputs['ed_3'] = str(randrange(0, 10))

    def _select_ed_4(self):
        # report.debug('')
        self._inputs['ed_4'] = str(randrange(1000, 10000))

    def _create_string(self):
        # report.debug('')
        return self.user_agent_template.format(**self._inputs)
