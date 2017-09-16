import os
Base=(os.path.dirname(__file__),'static')
print Base
base_1=os.path.join(Base[0],Base[1],'css')
print base_1