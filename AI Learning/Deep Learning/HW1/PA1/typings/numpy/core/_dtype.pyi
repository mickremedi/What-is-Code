"""
This type stub file was generated by pyright.
"""

import sys
from typing import Any, Optional

"""
A place for code to be called from the implementation of np.dtype

String handling is much easier to do correctly in python.
"""
_kind_to_stem = { 'u': 'uint','i': 'int','c': 'complex','f': 'float','b': 'bool','V': 'void','O': 'object','M': 'datetime','m': 'timedelta' }
if sys.version_info[0] >= 3:
    ...
else:
    ...
def _kind_name(dtype):
    ...

def __str__(dtype):
    ...

def __repr__(dtype):
    ...

def _unpack_field(dtype, offset, title: Optional[Any] = ...):
    """
    Helper function to normalize the items in dtype.fields.

    Call as:

    dtype, offset, title = _unpack_field(*dtype.fields[name])
    """
    ...

def _isunsized(dtype):
    ...

def _construction_repr(dtype, include_align: bool = ..., short: bool = ...):
    """
    Creates a string repr of the dtype, excluding the 'dtype()' part
    surrounding the object. This object may be a string, a list, or
    a dict depending on the nature of the dtype. This
    is the object passed as the first parameter to the dtype
    constructor, and if no additional constructor parameters are
    given, will reproduce the exact memory layout.

    Parameters
    ----------
    short : bool
        If true, this creates a shorter repr using 'kind' and 'itemsize', instead
        of the longer type name.

    include_align : bool
        If true, this includes the 'align=True' parameter
        inside the struct dtype construction dict when needed. Use this flag
        if you want a proper repr string without the 'dtype()' part around it.

        If false, this does not preserve the
        'align=True' parameter or sticky NPY_ALIGNED_STRUCT flag for
        struct arrays like the regular repr does, because the 'align'
        flag is not part of first dtype constructor parameter. This
        mode is intended for a full 'repr', where the 'align=True' is
        provided as the second parameter.
    """
    ...

def _scalar_str(dtype, short):
    ...

def _byte_order_str(dtype):
    """ Normalize byteorder to '<' or '>' """
    ...

def _datetime_metadata_str(dtype):
    ...

def _struct_dict_str(dtype, includealignedflag):
    ...

def _is_packed(dtype):
    """
    Checks whether the structured data type in 'dtype'
    has a simple layout, where all the fields are in order,
    and follow each other with no alignment padding.

    When this returns true, the dtype can be reconstructed
    from a list of the field names and dtypes with no additional
    dtype parameters.

    Duplicates the C `is_dtype_struct_simple_unaligned_layout` functio.
    """
    ...

def _struct_list_str(dtype):
    ...

def _struct_str(dtype, include_align):
    ...

def _subarray_str(dtype):
    ...

def _name_get(dtype):
    ...

