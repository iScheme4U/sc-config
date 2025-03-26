class FileHandler(object):
    def __new__(cls, *, path, extension=None, **kwargs):
        """
            :param path: path of the config file
        """

        if not extension and len(path.split('.')) > 1:
            extension = path.split('.')[-1]
        elif not isinstance(extension, str):
            extension = ""

        if extension.lower() in ("yaml", "yml"):
            from sc_config.handlers.files.yaml import YamlHandler as Handler
        elif extension.lower() == "json":
            from sc_config.handlers.files.json import JsonHandler as Handler
        elif extension.lower() == "ini":
            from sc_config.handlers.files.ini import IniHandler as Handler
        else:
            from sc_config.handlers.raw import RawHandler as Handler

        return Handler(path=path, **kwargs)
