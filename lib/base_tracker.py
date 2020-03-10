from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from helpers import get_value
from helpers import logger


CHROME_DRIVER_PATH = 'drivers/chromedriver'


class BaseTracker:
    def __init__(self, app_config):
        self.config = app_config
        self.browser = webdriver.Chrome(CHROME_DRIVER_PATH)

    def get_element(self, selector_id):
        platform_meta = self.get_platform_meta()
        selector = get_value(platform_meta, selector_id)
        logger.debug(
            'Getting element with CSS selector: {}'.format(selector))
        return self.browser.find_element_by_css_selector(selector)

    def get_platform_meta(self):
        platform_id = 'tracking_platform.{}'.format(self.platform)
        return get_value(self.config, platform_id)

    def track(self):
        pass
