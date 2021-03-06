"""
This type stub file was generated by pyright.
"""

import pprint
import sys
from . import __version__

"""

Auxiliary functions for f2py2e.

Copyright 1999,2000 Pearu Peterson all rights reserved,
Pearu Peterson <pearu@ioc.ee>
Permission to use, modify, and distribute this software is given under the
terms of the NumPy (BSD style) LICENSE.


NO WARRANTY IS EXPRESSED OR IMPLIED.  USE AT YOUR OWN RISK.
$Date: 2005/07/24 19:01:55 $
Pearu Peterson

"""
__all__ = ['applyrules', 'debugcapi', 'dictappend', 'errmess', 'gentitle', 'getargs2', 'getcallprotoargument', 'getcallstatement', 'getfortranname', 'getpymethoddef', 'getrestdoc', 'getusercode', 'getusercode1', 'hasbody', 'hascallstatement', 'hascommon', 'hasexternals', 'hasinitvalue', 'hasnote', 'hasresultnote', 'isallocatable', 'isarray', 'isarrayofstrings', 'iscomplex', 'iscomplexarray', 'iscomplexfunction', 'iscomplexfunction_warn', 'isdouble', 'isdummyroutine', 'isexternal', 'isfunction', 'isfunction_wrap', 'isint1array', 'isinteger', 'isintent_aux', 'isintent_c', 'isintent_callback', 'isintent_copy', 'isintent_dict', 'isintent_hide', 'isintent_in', 'isintent_inout', 'isintent_inplace', 'isintent_nothide', 'isintent_out', 'isintent_overwrite', 'islogical', 'islogicalfunction', 'islong_complex', 'islong_double', 'islong_doublefunction', 'islong_long', 'islong_longfunction', 'ismodule', 'ismoduleroutine', 'isoptional', 'isprivate', 'isrequired', 'isroutine', 'isscalar', 'issigned_long_longarray', 'isstring', 'isstringarray', 'isstringfunction', 'issubroutine', 'issubroutine_wrap', 'isthreadsafe', 'isunsigned', 'isunsigned_char', 'isunsigned_chararray', 'isunsigned_long_long', 'isunsigned_long_longarray', 'isunsigned_short', 'isunsigned_shortarray', 'l_and', 'l_not', 'l_or', 'outmess', 'replace', 'show', 'stripcomma', 'throw_error']
f2py_version = __version__.version
errmess = sys.stderr.write
show = pprint.pprint
options = {  }
debugoptions = []
wrapfuncs = 1
def outmess(t):
    ...

def debugcapi(var):
    ...

def _isstring(var):
    ...

def isstring(var):
    ...

def ischaracter(var):
    ...

def isstringarray(var):
    ...

def isarrayofstrings(var):
    ...

def isarray(var):
    ...

def isscalar(var):
    ...

def iscomplex(var):
    ...

def islogical(var):
    ...

def isinteger(var):
    ...

def isreal(var):
    ...

def get_kind(var):
    ...

def islong_long(var):
    ...

def isunsigned_char(var):
    ...

def isunsigned_short(var):
    ...

def isunsigned(var):
    ...

def isunsigned_long_long(var):
    ...

def isdouble(var):
    ...

def islong_double(var):
    ...

def islong_complex(var):
    ...

def iscomplexarray(var):
    ...

def isint1array(var):
    ...

def isunsigned_chararray(var):
    ...

def isunsigned_shortarray(var):
    ...

def isunsignedarray(var):
    ...

def isunsigned_long_longarray(var):
    ...

def issigned_chararray(var):
    ...

def issigned_shortarray(var):
    ...

def issigned_array(var):
    ...

def issigned_long_longarray(var):
    ...

def isallocatable(var):
    ...

def ismutable(var):
    ...

def ismoduleroutine(rout):
    ...

def ismodule(rout):
    ...

def isfunction(rout):
    ...

def isfunction_wrap(rout):
    ...

def issubroutine(rout):
    ...

def issubroutine_wrap(rout):
    ...

def hasassumedshape(rout):
    ...

def isroutine(rout):
    ...

def islogicalfunction(rout):
    ...

def islong_longfunction(rout):
    ...

def islong_doublefunction(rout):
    ...

def iscomplexfunction(rout):
    ...

def iscomplexfunction_warn(rout):
    ...

def isstringfunction(rout):
    ...

def hasexternals(rout):
    ...

def isthreadsafe(rout):
    ...

def hasvariables(rout):
    ...

def isoptional(var):
    ...

def isexternal(var):
    ...

def isrequired(var):
    ...

def isintent_in(var):
    ...

def isintent_inout(var):
    ...

def isintent_out(var):
    ...

def isintent_hide(var):
    ...

def isintent_nothide(var):
    ...

def isintent_c(var):
    ...

def isintent_cache(var):
    ...

def isintent_copy(var):
    ...

def isintent_overwrite(var):
    ...

def isintent_callback(var):
    ...

def isintent_inplace(var):
    ...

def isintent_aux(var):
    ...

def isintent_aligned4(var):
    ...

def isintent_aligned8(var):
    ...

def isintent_aligned16(var):
    ...

isintent_dict = { isintent_in: 'INTENT_IN',isintent_inout: 'INTENT_INOUT',isintent_out: 'INTENT_OUT',isintent_hide: 'INTENT_HIDE',isintent_cache: 'INTENT_CACHE',isintent_c: 'INTENT_C',isoptional: 'OPTIONAL',isintent_inplace: 'INTENT_INPLACE',isintent_aligned4: 'INTENT_ALIGNED4',isintent_aligned8: 'INTENT_ALIGNED8',isintent_aligned16: 'INTENT_ALIGNED16' }
def isprivate(var):
    ...

def hasinitvalue(var):
    ...

def hasinitvalueasstring(var):
    ...

def hasnote(var):
    ...

def hasresultnote(rout):
    ...

def hascommon(rout):
    ...

def containscommon(rout):
    ...

def containsmodule(block):
    ...

def hasbody(rout):
    ...

def hascallstatement(rout):
    ...

def istrue(var):
    ...

def isfalse(var):
    ...

class F2PYError(Exception):
    ...


class throw_error(object):
    def __init__(self, mess):
        self.mess = ...
    
    def __call__(self, var):
        ...
    


def l_and(*f):
    ...

def l_or(*f):
    ...

def l_not(f):
    ...

def isdummyroutine(rout):
    ...

def getfortranname(rout):
    ...

def getmultilineblock(rout, blockname, comment=..., counter=...):
    ...

def getcallstatement(rout):
    ...

def getcallprotoargument(rout, cb_map=...):
    ...

def getusercode(rout):
    ...

def getusercode1(rout):
    ...

def getpymethoddef(rout):
    ...

def getargs(rout):
    ...

def getargs2(rout):
    ...

def getrestdoc(rout):
    ...

def gentitle(name):
    ...

def flatlist(l):
    ...

def stripcomma(s):
    ...

def replace(str, d, defaultsep=...):
    ...

def dictappend(rd, ar):
    ...

def applyrules(rules, d, var=...):
    ...

