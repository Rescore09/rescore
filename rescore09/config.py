import os
import json
import configparser
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


class ConfigLoader:
    def __init__(self, path: str):
        self.path = Path(path)
        self.config = self._load()

    def _load(self):
        if not self.path.exists():
            raise FileNotFoundError(f"Config file not found: {self.path}")

        ext = self.path.suffix.lower()
        if ext == '.json':
            return json.loads(self.path.read_text())
        elif ext in ['.yaml', '.yml']:
            if not yaml:
                raise ImportError("PyYAML is not installed. Run `pip install pyyaml`.")
            return yaml.safe_load(self.path.read_text())
        elif ext == '.env':
            return self._load_env()
        elif ext in ['.ini', '.cfg']:
            return self._load_ini()
        else:
            raise ValueError(f"Unsupported config file type: {ext}")

    def _load_env(self):
        config = {}
        with self.path.open() as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, val = line.strip().split('=', 1)
                    config[key.strip()] = val.strip()
        return config

    def _load_ini(self):
        parser = configparser.ConfigParser()
        parser.read(self.path)
        return {s: dict(parser.items(s)) for s in parser.sections()}

    def get(self, key, default=None):
        return self.config.get(key, default)
