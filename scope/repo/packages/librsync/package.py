# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install librsync
#
# You can edit this file again by typing:
#
#     spack edit librsync
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Librsync(CMakePackage):
    """Remote delta-compression library."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://librsync.github.io/"
    url      = "https://github.com/librsync/librsync/archive/refs/tags/v2.3.2.tar.gz"

    maintainers = ['brettviren']

    version('2.3.2', sha256='ef8ce23df38d5076d25510baa2cabedffbe0af460d887d86c2413a1c2b0c676f')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
