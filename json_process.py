# coding=utf-8
import json
import os


class JsonProcess:
    def __init__(self, file_name):
        self.current_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
        self.json_file = {}

    def read_json(self):
        try:
            self.json_file = open(self.current_file, encoding="utf8")
            return json.load(self.json_file)
        except Exception as e:
            print(e)
        finally:
            self.json_file.close()

    def dump_json(self, new_file):
        try:
            self.json_file = open(self.current_file, 'w')
            json.dump(new_file, self.json_file, indent=1)
        except Exception as e:
            print(e)
        finally:
            self.json_file.close()
