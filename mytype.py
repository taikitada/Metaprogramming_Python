class MyType(type):
	def __init__(cls, name, bases,dct):
		super(MyType, cls).__init__(name, bases, dct)
		def new_init(self, **kwargs):
			for k,v in [(k,v) for (k,v) in kwargs.iteritems() if k in dct['attributes']]:
				setattr(self, k, v)
		cls.__init__ = new_init

if __name__ == '__main__':
	MyObject = MyType('MyObject', (object,),{'attributes':['name','age']})
	MO = MyObject(name = 'taiki', age = '25')
	print MO.name, MO.age
