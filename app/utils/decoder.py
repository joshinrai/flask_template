from collections import namedtuple
import json

# 将对象转换为类
def object2ClassDecoder(obj, name):
    if name is None:
        name = 'X'
    return namedtuple(name, obj.keys())(*obj.values())

# 将json转换为类
def json2ClassDecoder(jsonObject):
    return json.loads(jsonObject, object_hook=object2ClassDecoder)
