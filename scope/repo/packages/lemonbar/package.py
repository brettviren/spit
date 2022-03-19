# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Lemonbar(MakefilePackage):
    """A featherweight, lemon-scented, bar based on xcb."""

    homepage = "https://gitlab.com/protesilaos/lemonbar-xft"
    url      = "https://gitlab.com/protesilaos/lemonbar-xft/-/archive/xft-port/lemonbar-xft-xft-port.tar.gz"
    git      = "https://gitlab.com/protesilaos/lemonbar-xft.git"
    list_url = "https://gitlab.com/protesilaos/lemonbar-xft/-/tags"

    maintainers = ['brettviren']

    version('develop', branch='xft-port')

    depends_on('libxcb')
    depends_on('libxrandr')
    depends_on('libxinerama')

    def edit(self, spec, prefix):
        env['PREFIX'] = prefix
        env['CFLAGS'] = '-DWITH_XINERAMA=1'
        # FIXME: Edit the Makefile if necessary
        # FIXME: If not needed delete this function
        # makefile = FileFilter('Makefile')
        # makefile.filter('CC = .*', 'CC = cc')

        # CFLAGS='-DWITH_XINERAMA=1'
        pass
