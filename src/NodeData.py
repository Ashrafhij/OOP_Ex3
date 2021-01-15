import random
class NodeData:
    def __init__(self, key: int = None, position: tuple = None, w: float = 0,
                 tag: int = 0, info: str = ""):
        self.key = key
        if position == None:
            self.pos = random.random() * key, random.random() * key
        else:
            self.pos=position
        self.w = w
        self.tag = tag
        self.info = info

    def get_key(self):
        return self.key

    def set_tag(self, t: int):
        self.tag = t