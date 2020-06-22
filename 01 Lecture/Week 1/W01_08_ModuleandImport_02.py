"""
See how to separate the source code files
    Just put your code in another file
    filename.py
See how to use classes in other files
    import filename
Use from to specify the directory, or the folder.path

Directory, or folder
    Clusters modules
        Modules -> filename.py
    We call these directories as package
    Hence, the previous information is exactly.
        from package import module
Package has
    __init__.py in the directory
    This is how to differentiate between the ordinary and the package directories.
"""

import W01_08_ModuleandImport_01

homeAtDaejeon = W01_08_ModuleandImport_01.MyHome('Daejeon KAIST')
homeAtDaejeon.printStatus()