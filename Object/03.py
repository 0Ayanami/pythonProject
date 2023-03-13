class SetOnceMappingMixin:
    """自定义混入类,自定义字典限制只有在指定的key不存在时才能在字典中设置键值对。"""
    __slots__ = ()
    """__slots__是python类的魔法属性，可接收一个iterable对象作为属性"""
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    """自定义字典"""
    pass


my_dict = SetOnceDict()
try:
    my_dict['username'] = 'jackfrued'
    my_dict['username'] = 'hellokitty'
except KeyError:
    pass
print(my_dict)
"""
   通常混子类的功能应该通用而单一。每个混子类只实现一种功能，可按需继承。
   混子类只用于拓展子类的功能，而不能影响子类的主要功能，子类也不能依赖混子类。
   如果有依赖关系，则是真正的基类，不应该用混子类来命名。 
   混子（Mixin）类自身并不进行实例化，仅为子类继承
"""