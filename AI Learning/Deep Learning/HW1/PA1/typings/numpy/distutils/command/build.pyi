"""
This type stub file was generated by pyright.
"""

from distutils.command.build import build as old_build

class build(old_build):
    sub_commands = ...
    user_options = ...
    help_options = ...
    def initialize_options(self):
        self.fcompiler = ...
        self.parallel = ...
    
    def finalize_options(self):
        ...
    
    def run(self):
        ...
    


