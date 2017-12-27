from HashMapBase import HashMapBase
from UnsortedTableMap import UnsortedTableMap
from util.KeyError import KeyError


class ChainHashMap(HashMapBase):
 
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError( 'Key Error: ' + repr(k)) # no match found
        return bucket[k] # may raise KeyError

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap( ) # bucket is new to the table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize: # key was new to the table
            self._n += 1 # increase overall map size

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError( 'Key Error: ' + repr(k)) # no match found
        del bucket[k] # may raise KeyError

    def __iter__ (self):
        for bucket in self._table:
            if bucket is not None: # a nonempty slot
                for key in bucket:
                    yield key
                    
    def _print_ (self):
        for bucket in self._table:
            if bucket is not None: # a nonempty slot
                bucket.__print__()
 
 
mymap = ChainHashMap()
mymap.__setitem__('A', 'One')
mymap.__setitem__('B', 'Two')
mymap.__setitem__('C', 'Three')
mymap.__setitem__('D', 'Four')
mymap.__setitem__('E', 'Five')
mymap._print_()
print('')
mymap.__delitem__('A')
mymap._print_()
mymap.__setitem__('A', 'One1')
print('')
mymap._print_()
mymap.__setitem__('A', 'One2')
print('')
mymap._print_()
 