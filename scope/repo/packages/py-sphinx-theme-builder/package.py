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
#     spack install sphinx-theme-builder
#
# You can edit this file again by typing:
#
#     spack edit sphinx-theme-builder
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PySphinxThemeBuilder(PythonPackage):
    """Sphinx Theme Builder."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    pypi = "sphinx-theme-builder/sphinx-theme-builder-0.2.0a13.tar.gz"

    version('0.2.0a13', sha256='d0bf4429a9c051910eee94a32942fa940db546fd033a7cef8986c8ea68f23fc5')

    depends_on('py-sphinx@1.8:')
    depends_on('py-flit-core')
