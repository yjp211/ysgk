# -*- coding:utf-8 -*-

from django import template

register = template.Library()


def algorithm(value, arg):
    """
    进行算术表达式运算
    (%s +100)*3
    %s指代value
    :param arg: 表达式，可以支持复杂的运算， arg中包含一个'%s'用于指代value
    :return:
    """
    try:
        return eval(arg % value)
    except:
        return value


def pretty_datetime(value):
    """
    使用setting的格式进行时间格式化
    :param value:
    :return:
    """
    try:
        from src.settings import TIME_FORMAT
        return value.strftime(TIME_FORMAT)
    except:
        return ''

def cut_string(value, length):
    """
    根据指定长度截断字符，剩余的部分用省略号...代替
    :param value: 字符
    :param length: 保留长度
    :return:
    """
    try:
        length = int(length)
        if len(value) > length:
            return "%s..." % value[:length]
        else:
            return value
    except:
        return value


register.filter('algorithm', algorithm)
register.filter('pretty_datetime', pretty_datetime)
register.filter('cut_string', cut_string)