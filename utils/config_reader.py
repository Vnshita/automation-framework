import yaml


class ConfigReader:

    @staticmethod
    def read_config(request=None):
        with open("config/config.yaml") as f:
            config = yaml.safe_load(f)

        if request:
            env = request.config.getoption("--env")
        else:
            env = config.get("env")

        config["env"] = env
        return config