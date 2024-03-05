import json
from os.path import abspath

class TagHandler:
    def __init__(self, filepath: str):
        self.file_path = filepath
        if not self.file_path:
            default_path = "data/tags.json"
            file = open(default_path, 'w')
            file.close()
            self.file_path = abspath(default_path)
        self.__unpack(self.file_path)

    def unpack(self):
        with open(self.file_path) as f:
            self.tag_dictionary = json.load(f)

    def pack(self):
        with open(self.file_path) as f:
            json.dump(self.tag_dictionary, f)

    def add(self, image_file_path: str, tag: str):
        if self.file_path is None:
            # TODO: Raise Exception
            return
        
        # Create tag list for image if necessary.
        if image_file_path not in self.tag_dictionary:
            self.tag_dictionary[image_file_path] = []
        
        # Add tag to tag list if not already there.
        if tag not in self.tag_dictionary[image_file_path]:
            self.tag_dictionary[image_file_path].append(tag)

        # Do nothing if tag already exists in tag list.
            
    def remove(self, image_file_path: str, tag: str):
        if len(self.tag_dictionary) == 0:
            # TODO: Raise Exception?
            return
        
        # Remove tag only if file exists in dictionary and if tag exists in tag list.
        if image_file_path in self.tag_dictionary:
            if tag in self.tag_dictionary[image_file_path]:
                self.tag_dictionary[image_file_path].remove(tag)

    def get(self, image_file_path: str) -> list[str]:
        if image_file_path is None:
            return None
        
        if len(self.tag_dictionary) == 0:
            return None
        
        return self.tag_dictionary[image_file_path]
        
