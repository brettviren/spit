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

    # When adding to this list, check if package.yaml needs more.
    depends_on('python@3.9.10')
    depends_on('kitty@0.25.2')
    depends_on('herbstluftwm@0.9.5')
    depends_on('emacs@28.1 +X toolkit=gtk')
    depends_on('lemonbar@develop')
    depends_on('rofi@1.7.3')
    depends_on('weechat@3.6+perl+lua') # python is default
    depends_on('prmon@3.0.1')
    depends_on('py-xapers@0.8.2')
#    depends_on('py-buku@0.8.2')
