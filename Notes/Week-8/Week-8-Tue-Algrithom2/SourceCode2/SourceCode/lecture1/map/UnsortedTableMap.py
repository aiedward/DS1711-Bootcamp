from MapBase import MapBase
from util.KeyError import KeyError

class UnsortedTableMap(MapBase):
    
    def __init__ (self):
        self._table = []
        
    def __getitem__ (self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError( 'Key Error: ' + repr(k))
    
    def __setitem__ (self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        self._table.append(self._Item(k,v))
    
    def __delitem__ (self, k):
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError( 'Key Error: ' + repr(k))
    
    def __print__(self):
        for item in self._table:
            item.__print__()
        print('')

    def __len__(self):
        return len(self._table)
    
    def __iter__ (self):
        for item in self._table:
            yield item. key

#map = UnsortedTableMap()
#for i in range(1, 10):
#    map.__setitem__(i, i)
#map.__print__()
#map.__delitem__(5)
#map.__print__()
#map.__delitem__(5)
