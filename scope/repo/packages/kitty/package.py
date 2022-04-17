# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import sys

from spack import *


# NOTE: This package uses a setup.py file, but does not use distutils/setuptools or any
# other known build system, so this is a custom package
class Kitty(Package):
    """
    fast, featureful, cross-platform, GPU-based terminal emulator
    """

    homepage = "https://sw.kovidgoyal.net/kitty/index.html"
    url      = "https://github.com/kovidgoyal/kitty/archive/v0.12.3.tar.gz"
    git      = "https://github.com/kovidgoyal/kitty.git"

    maintainers = ['brettviren']

    version('0.25.0', sha256='be30160a905d26ddb2d07f52be40a56e6bf118162c447d3ea6f0e6f662b56676')
    version('0.24.4', sha256='e6619b635b5c9d6cebbba631a2175659698068ce1cd946732dc440b0f1c12ab3')
    version('0.23.1', sha256='32d3344e357da7012227d49d5031bff254bb8735f3b9edabdb46cfd13cb0e44d')

    # this requires imagemagic, which brings in large dependencies
    variant("icat-kitten", default=False,
            description="Add support for icat kitten")
    # this requires pygments
    variant("diff-kitten", default=False,
            description="Add support for diff kitten")
    # this is untested
    variant("wayland", default=False,
            description="Add support for waylaynd")

    # The list of dependencies formed from:
    # https://sw.kovidgoyal.net/kitty/build/

    # "run time"
    depends_on('python@3.6:')
    depends_on('harfbuzz')
    depends_on('zlib')
    depends_on('libpng')
    depends_on('lcms')
    depends_on('librsync')
    depends_on('freetype', when=sys.platform != 'darwin')
    depends_on('fontconfig', when=sys.platform != 'darwin')
    depends_on('libcanberra', when=sys.platform != 'darwin')

    depends_on('imagemagick', when="+icat-kitten")
    depends_on('py-pygments', when="+diff-kitten")

    # "build time"
    depends_on('pkg-config', type=('build','link'))
    depends_on('dbus')
    depends_on('libxcursor')
    depends_on('libxrandr')
    depends_on('libxi')
    depends_on('libxinerama')
    depends_on('mesa')          #  libGL
    depends_on('libxkbcommon')
    depends_on('libxcb')

    depends_on('wayland-protocols', when="+wayland")
    depends_on('wayland', when="+wayland")

    # plus this unlisted morasse 
    depends_on('py-setuptools', type='build')
    depends_on('py-sphinx', type='build')
    depends_on('py-sphinx-copybutton', type='build')
    depends_on('py-sphinx-inline-tabs', type='build')
    depends_on('py-sphinxext-opengraph', type='build')
    depends_on('py-sphinx-furo-theme', type='build')
    depends_on('py-beautifulsoup4', type='build')

    # depends_on('xkeyboard-config', when=sys.platform != 'darwin')

    def install(self, spec, prefix):
        python = which('python3')
        sys.stderr.write(str(python) + '\n')
        print(python)
        python('-s', 'setup.py', 'linux-package',
               '--prefix={0}'.format(prefix))

