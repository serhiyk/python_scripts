#!/usr/bin/python3
from lxml import etree


class XML_doc(object):
    def __init__(self, file_name):
        self.tree = etree.parse(file_name)
        self.root = self.tree.getroot()

    def save(self, file_name):
        with open(file_name, 'wb') as f:
            self.tree.write(f, pretty_print=True)

    def get_attr_list(self, attr_name):
        return [node.get(attr_name) for node in self.root]

    def remove_by_attr(self, attr_name, values):
        for node in self.root:
            if node.get(attr_name) not in values:
                node.getparent().remove(node)
