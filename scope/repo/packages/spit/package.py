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

    depends_on('python@3.9.10')
    depends_on('kitty@0.24.4')
    depends_on('herbstluftwm@0.9.4')
    depends_on('emacs@27.2 +X toolkit=gtk')
    depends_on('lemonbar@develop')
    depends_on('rofi@1.7.3')
    depends_on('weechat@3.4.1+perl+lua') # python is default
    depends_on('prmon@3.0.1')
    depends_on('py-xapers@0.8.2')
