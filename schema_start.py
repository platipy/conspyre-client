import inspect

class ConspyreFieldBase(object):
    creation_counter = 0
    def __init__(self):
    	self.creation_counter = ConspyreFieldBase.creation_counter
        ConspyreFieldBase.creation_counter += 1

class Integer(ConspyreFieldBase):
	pass

class Float(ConspyreFieldBase):
	pass

class String(ConspyreFieldBase):
	pass

class Blob(ConspyreFieldBase):
	pass

class ConspyreTableMeta(type):
    def __new__(meta, name, bases, dict):
        cls = type.__new__(meta, name, bases, dict)
        y = inspect.getmembers(cls, lambda o: isinstance(o, ConspyreFieldBase))

        cls.fields = sorted(inspect.getmembers(cls, 
                                               lambda o: isinstance(o, ConspyreFieldBase)), 
                            key=lambda i:i[1].creation_counter)
        if not hasattr(cls, '__version__') and cls.__name__ != "SyncSchema":
        	raise TypeError("Schema types must define a __version__")
        return cls


class SyncSchema(object):
	__metaclass__ = ConspyreTableMeta
	pass

class TestSync(SyncSchema):
	__version__ = 0.1
	a = Integer()
	b = Integer()
	c = Blob()
	d = String()
	e = Integer()
	f = Integer()

a = TestSync()