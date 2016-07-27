#! /user/bin/python3

import xml.etree.ElementTree as etree

def getitem(xml_f, tag):
    tree = etree.parse(xml_f)
    root = tree.getroot()
    result = root[0].findall(tag)
    return result
