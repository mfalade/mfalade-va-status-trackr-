from . import BaseTracker
from helpers import get_value
from helpers import logger


class DHLPackageTracker(BaseTracker):
    platform = 'dhl'

    def __init__(self, *args):
        super().__init__(*args)

    def track(self, tracking_id):
        logger.debug('Tracking DHL delivery for ref: {}'.format(tracking_id))
        platform_meta = self.get_platform_meta()
        tracking_url = get_value(platform_meta, 'url')

        self.browser.get(tracking_url)

        text_input = self.get_element('text_input_selector')
        submit_button = self.get_element('submit_button_selector')

        text_input.clear()
        text_input.send_keys(tracking_id)
        submit_button.click()
