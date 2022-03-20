# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyXapers(PythonPackage):
    """Personal journal article management system."""

    homepage = "https://finestructure.net/xapers/"
    url     = "https://finestructure.net/xapers/releases/xapers-0.8.2.tar.gz"

    maintainers = ['brettviren']

    version('0.8.2', sha256='ad52cf46fd87807dd53e94d5a8494202335be205d8b494d8e086483c2c347f7a')
    version('0.8',   sha256='3b132cf8252121491d1b2fe91f3f1e09485dfc985ebb6a8fa477f45830c2933b')
    version('0.7.1', sha256='c1347d4e0bfe90f9849b9cdabb7f3fb3d7b86f90a4ed15b5f995002748f7ad8f')

    ## fixme: once py-xapian is packaged, this hsould be uncommented.
    # extends("python")
    # This next one is a core dependency but is not actually in Spack.
    # While I use this via "spit" I don't actually need it defined.
    # depends_on('py-xapian')
    depends_on('py-pybtex')
    depends_on('py-pycurl')
    depends_on('poppler')
    depends_on('py-urwid')
    depends_on('xclip')

    patch('fullcolor.patch', level=2)

    def global_options(self, spec, prefix):
        # FIXME: Add options to pass to setup.py
        # FIXME: If not needed, delete this function
        options = []
        return options

    def install_options(self, spec, prefix):
        # FIXME: Add options to pass to setup.py install
        # FIXME: If not needed, delete this function
        options = []
        return options
