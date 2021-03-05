"""
This type stub file was generated by pyright.
"""

import doctest
import numpy
import nose
from nose.plugins import doctests as npd
from nose.plugins.errorclass import ErrorClassPlugin
from nose.plugins.base import Plugin
from typing import Any, Optional

class NumpyDocTestFinder(doctest.DocTestFinder):
    def _from_module(self, module, object):
        """
        Return true if the given object is defined in the given
        module.
        """
        ...
    
    def _find(self, tests, obj, name, module, source_lines, globs, seen):
        """
        Find tests for the given object and any contained objects, and
        add them to `tests`.
        """
        ...
    


class NumpyOutputChecker(doctest.OutputChecker):
    def check_output(self, want, got, optionflags):
        ...
    


class NumpyDocTestCase(npd.DocTestCase):
    def __init__(self, test, optionflags=..., setUp: Optional[Any] = ..., tearDown: Optional[Any] = ..., checker: Optional[Any] = ..., obj: Optional[Any] = ..., result_var=...):
        ...
    


print_state = numpy.get_printoptions()
class NumpyDoctest(npd.Doctest):
    name = ...
    score = ...
    doctest_optflags = ...
    doctest_ignore = ...
    doctest_case_class = ...
    out_check_class = ...
    test_finder_class = ...
    def options(self, parser, env=...):
        self.doctest_tests = ...
        self.doctest_result_var = ...
    
    def configure(self, options, config):
        self.finder = ...
        self.parser = ...
    
    def set_test_context(self, test):
        """ Configure `test` object to set test context

        We set the numpy / scipy standard doctest namespace

        Parameters
        ----------
        test : test object
            with ``globs`` dictionary defining namespace

        Returns
        -------
        None

        Notes
        -----
        `test` object modified in place
        """
        ...
    
    def loadTestsFromModule(self, module):
        ...
    
    def afterContext(self):
        ...
    
    def wantFile(self, file):
        ...
    


class Unplugger(object):
    """ Nose plugin to remove named plugin late in loading

    By default it removes the "doctest" plugin.
    """
    name = ...
    enabled = ...
    score = ...
    def __init__(self, to_unplug=...):
        self.to_unplug = ...
    
    def options(self, parser, env):
        ...
    
    def configure(self, options, config):
        ...
    


class KnownFailurePlugin(ErrorClassPlugin):
    '''Plugin that installs a KNOWNFAIL error class for the
    KnownFailureClass exception.  When KnownFailure is raised,
    the exception will be logged in the knownfail attribute of the
    result, 'K' or 'KNOWNFAIL' (verbose) will be output, and the
    exception will not be counted as an error or failure.'''
    enabled = ...
    knownfail = ...
    def options(self, parser, env=...):
        ...
    
    def configure(self, options, conf):
        self.conf = ...
    


KnownFailure = KnownFailurePlugin
class FPUModeCheckPlugin(Plugin):
    """
    Plugin that checks the FPU mode before and after each test,
    raising failures if the test changed the mode.
    """
    def prepareTestCase(self, test):
        ...
    


class NumpyTestProgram(nose.core.TestProgram):
    def runTests(self):
        """Run Tests. Returns true on success, false on failure, and
        sets self.success to the same value.

        Because nose currently discards the test result object, but we need
        to return it to the user, override TestProgram.runTests to retain
        the result
        """
        self.result = ...
        self.success = ...
    

