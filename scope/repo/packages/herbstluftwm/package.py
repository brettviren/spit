# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Herbstluftwm(CMakePackage):
    """A manual tiling window manager for X11 ."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://herbstluftwm.org/"
    url      = "https://github.com/herbstluftwm/herbstluftwm/archive/refs/tags/v0.9.4.tar.gz"

    maintainers = ['brettviren']

    
    version('0.9.4', sha256='b36e143c2ffbd820c7c00e6a1f0a74bc83fed5eb1bab35411503e68e702a18e3')
    version('0.9.3', sha256='4eeec3f32420722a1518c7b7a041790829156589f6982f019a32979879a388c1')
    
    depends_on("libx11")
    depends_on("freetype")

    def cmake_args(self):
        args = [
            "-DCMAKE_INSTALL_SYSCONF_PREFIX=%s"%self.prefix.etc,
        ]
        return args
