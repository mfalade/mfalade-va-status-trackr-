from selenium.webdriver.support.ui import Select

from . import BaseTracker
from helpers import get_value
from helpers import logger


class VacApplicationTracker(BaseTracker):
    platform = 'vac'

    def __init__(self, *args):
        super().__init__(*args)

    def track(self, tracking_data):
        logger.debug('Tracking VAC delivery for ref: {}'.format(tracking_data))
        platform_meta = self.get_platform_meta()
        tracking_url = get_value(platform_meta, 'url')

        tracking_id = get_value(tracking_data, 'VT_TRACKING_ID')
        dob_year = get_value(tracking_data, 'USER_DOB_YEAR')
        # Decrement month cos values are set by indices
        dob_month = int(get_value(tracking_data, 'USER_DOB_MONTH')) - 1
        dob_day = get_value(tracking_data, 'USER_DOB_DAY')
        dob = '{0}/{1}/{2}'.format(dob_year, dob_month, dob_day)

        self.browser.get(tracking_url)

        tracking_id_input = self.get_element('tracking_id_input_selector')
        date_input = self.get_element('date_input_selector')

        tracking_id_input.clear()
        tracking_id_input.send_keys(tracking_id)

        date_input.click()

        year_input = Select(self.get_element('year_picker_selector'))
        year_input.select_by_value(str(dob_year))

        month_input = Select(self.get_element('month_picker_selector'))
        month_input.select_by_value(str(dob_month))

        day_input = self.browser.find_element_by_xpath(
            "//a[text()='{}']".format(dob_day))
        day_input.click()
