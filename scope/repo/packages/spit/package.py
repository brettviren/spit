# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Spit(BundlePackage):
    """Personal packages"""

    homepage = "https://github.com/brettviren/spit"

    maintainers = ['brettviren']

    version('0.0.0')

    depends_on('kitty')
    depends_on('herbstluftwm')
    depends_on('emacs +X toolkit=gtk')
    depends_on('lemonbar')
    depends_on('rofi')
    depends_on('weechat+perl+lua') # python is default
    depends_on('prmon')
