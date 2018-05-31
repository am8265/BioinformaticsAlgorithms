#!/usr/bin/env python
class MyDB:
    def __init__(self):
        self._id2name_map={}
        self._name2id_map={}
    def add(self,id,name):
        self._name2id_map[name]=id
        self._id2name_map[id]=name
    def by_name(self,name):
        return self._name2id_map[name]
