# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Rofi(AutotoolsPackage):
    """A window switcher, application launcher and dmenu replacement."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/davatorium/rofi/"
    git      = "https://github.com/davatorium/rofi.git"

    maintainers = ['brettviren']

    #version('main', branch='main', submodules=True)
    version('1.7.3', tag='1.7.3', submodules=True)

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')

    depends_on('pkg-config', type=('build','link'))
    depends_on('flex', type=('build','link'))
    depends_on('bison', type=('build','link'))

    depends_on('pango')
    depends_on('cairo')
    # libpangocairo
    # libcairo-xcb
    depends_on('glib')
    #     gmodule-2.0
    #     gio-unix-2.0
    depends_on('gdk-pixbuf')
    depends_on('startup-notification')
    depends_on('libxkbcommon')
    # libxkbcommon-x11
    depends_on('libxcb')
    depends_on('xcb-util')
    depends_on('xcb-util-wm')
    depends_on('xcb-util-cursor')


    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = [
            '--disable-check'
        ]
        return args
