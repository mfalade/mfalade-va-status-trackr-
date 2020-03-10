import yaml

from . import logger


def read_file(file_path, file_reader=yaml, file_loader=yaml.FullLoader):
    logger.info('Reading app configuration')

    with open(file_path, 'r') as file:
        app_config = file_reader.load(file, Loader=file_loader)
        logger.info('Successfully read app configuration: ')
        logger.debug('config: {}'.format(app_config))
        return app_config
