from random import choice, randrange
from django_project.settings import USERAGENT
# from ..logger.logger import logger

# report = logger(10)




# Mozilla/5.0
# (Linux; Android 10; SM-A505F)
# AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/77.0.3865.116
# Mobile Safari/537.36
# EdgA/45.11.4.5118

# Mozilla/5.0 (Linux; Android 10; SM-N960F)
# AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/93.0.4577.82
# Mobile Safari/537.36
# EdgA/93.0.961.80


data_for_device = USERAGENT['MOBILE_USERAGENT']['data_for_device']
android_version = USERAGENT['MOBILE_USERAGENT']['android_version']
awk_1 = USERAGENT['MOBILE_USERAGENT']['awk_1']
ch_1 = USERAGENT['MOBILE_USERAGENT']['ch_1']
s_1 = USERAGENT['MOBILE_USERAGENT']['s_1']
ed_1 = USERAGENT['MOBILE_USERAGENT']['ed_1']
ed_2 = USERAGENT['MOBILE_USERAGENT']['ed_2']


class MobileUserAgentCreator:
    def __init__(self):
        # report.debug('')
        self.user_agent_template = "Mozilla/5.0 " \
                                   "(Linux; Android {android_version}; {device}) " \
                                   "AppleWebKit/{awk_1}.{awk_2} " \
                                   "(KHTML, like Gecko) " \
                                   "Chrome/{ch_1}.{ch_2}.{ch_3}.{ch_4} " \
                                   "Mobile Safari/{s_1}.{s_2} " \
                                   "EdgA/{ed_1}.{ed_2}.{ed_3}.{ed_4}"

        self._inputs = {}

    def perform(self):
        # report.debug('')
        self._select_android_version()
        self._select_device()
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

    def _select_android_version(self):
        # report.debug('')
        self._inputs['android_version'] = android_version

    def _select_device(self):
        # report.debug('')
        self._inputs['device'] = choice(data_for_device)

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
