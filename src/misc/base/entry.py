# -*- coding:utf-8 -*-

import json

class BaseEntry(dict):
    """
    自定义数据模型的基础类

    """

    def __setattr__(self, key, value):
        return self.__setitem__(key, value)

    def __getattr__(self, item):
        return self.__getitem__(item)

    def __unicode__(self):
        tmp = {}
        for key, value in self.items():
            if isinstance(value, basestring):
                tmp[key] = str(value)
            else:
                tmp[key] = value
        return tmp

    def to_json(self):
        """
        将object转换为json对象
        """
        return json.dumps(self)

    def _to_dhtmltree_dict(self):
        """
        将object转换为dhtmlxtee控件识别的dict对象

        要求模型极其调用的其它模型必须组成的一个树形结构

        """
        tmp = {}
        if self.has_key('id'):
            tmp['id'] = self.get('id')
        elif self.has_key('name'):
            tmp['id'] = self.get('name')
        else:
            raise KeyError

        if self.has_key('text'):
            tmp['text'] = self.get('text')
        elif self.has_key('alias'):
            tmp['text'] = self.get('alias')
        elif self.has_key('name'):
            tmp['text'] = self.get('name')
        else:
            tmp['text'] = tmp['id']

        items = []
        for key, value in self.items():
            if value is None:
                continue
            if isinstance(value, list):
                tmp['child'] = True
                for entry in value:
                    if isinstance(entry, BaseEntry):
                        items.append(entry._to_dhtmltree_dict())
                    else:
                        items.append(value)

            else:
                tmp[key] = value
        if len(items) > 0:
            tmp['item'] = items
        return tmp

    def to_dhtmltree_json(self):
        """
        将object转换为dhtmlxtee控件识别的json对象
        要求模型极其调用的其它模型必须组成的一个树形结构
        转换成json之前，先对对象结构进行梳理
        """
        return json.dumps(self._to_dhtmltree_dict())



if __name__ == '__main__':
    o = BaseEntry()
    o['a'] = 4
    print o.a
    o.b = 3
    a1 = BaseEntry()
    a2 = BaseEntry()
    a3 = BaseEntry()
    a1.a1 = u"中文策划四"
    a2.a2 = 2222
    a3.a3 = {'c':[12,345], 'd':1}

    o.l = [a1,a2,a3]
    o['haha'] = True

    print o
    print o.to_dhtmltree_json()