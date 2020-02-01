#!/usr/bin/env python3

from method_chain import CRUD

crud = CRUD()
print(crud.do_oprn(3, operator='--'))
# Currently Operator (--) is not Applicable

print(crud.do_oprn(3, operator='+'))
# 0 + 3 = 3

a={'a':3}
b=3
print(crud.sum(1,2,b,**a).subtraction(3))
# +3+1+2+3+3-3 = 9

print(crud.subtract(1,2,3))
# +9-1-2-3 = 3
