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
#     spack install py-pep621
#
# You can edit this file again by typing:
#
#     spack edit py-pep621
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyPep621(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    pypi = "pep621/pep621-0.4.0.tar.gz"

    version('0.4.0', sha256='024271b42c3ce72fd4c57792da428c4a6c29fadee58c3580096e2a1a86131434')

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    # depends_on('py-setuptools', type='build')
    depends_on('py-flit-core', type='build')
    # depends_on('py-poetry-core', type='build')

    # FIXME: Add additional dependencies if required.
    # depends_on('py-foo', type=('build', 'run'))

    # def global_options(self, spec, prefix):
    #     # FIXME: Add options to pass to setup.py
    #     # FIXME: If not needed, delete this function
    #     options = []
    #     return options

    # def install_options(self, spec, prefix):
    #     # FIXME: Add options to pass to setup.py install
    #     # FIXME: If not needed, delete this function
    #     options = []
    #     return options
