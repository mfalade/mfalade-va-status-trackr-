from dotenv import load_dotenv
from helpers import logger
from helpers import read_file
from lib import DHLPackageTracker, VacApplicationTracker
import os

load_dotenv()


CONFIG_FILE = 'config.yml'


if __name__ == '__main__':
    app_config = read_file(CONFIG_FILE)
    dhl_package_tracker = DHLPackageTracker(app_config)
    vac_application_tracker = VacApplicationTracker(app_config)

    vac_meta = {
        'VT_TRACKING_ID': os.getenv('WAEC_TRANSCRIPT_TRACKING_ID'),
        'USER_DOB_YEAR': os.getenv('USER_DOB_YEAR'),
        'USER_DOB_MONTH': os.getenv('USER_DOB_MONTH'),
        'USER_DOB_DAY': os.getenv('USER_DOB_DAY')
    }

    dhl_package_tracker.track(os.getenv('WAEC_TRANSCRIPT_TRACKING_ID'))
    dhl_package_tracker.track(os.getenv('LAUTECH_TRANSCRIPT_TRACKING_ID'))
    vac_application_tracker.track(vac_meta)
