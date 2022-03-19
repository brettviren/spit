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
#     spack install py-sphinx-furo-theme
#
# You can edit this file again by typing:
#
#     spack edit py-sphinx-furo-theme
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PySphinxFuroTheme(PythonPackage):
    """A clean customisable Sphinx documentation theme."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    pypi = "furo/furo-2022.3.4.tar.gz"

    version('2022.3.4', sha256='7660267cc67b2828fd0e17bc07adeb612c47b2eba5a6de07049a1569e6044aa8')


    depends_on('py-setuptools', type='build')
    depends_on('py-sphinx-theme-builder')
    depends_on('py-rich')
    depends_on('py-pep621')
    depends_on('py-packaging')
    depends_on('py-tomli')
    depends_on('py-nodeenv')
    depends_on('py-beautifulsoup4')
    # depends_on('py-sphinx', when='@0.4.1:', type=('build', 'run'))
    # depends_on('py-docutils@:0.16', when='@0.5.2:', type=('build', 'run'))

    def setup_build_environment(self, env):
        # Hack to prevent usage of npm in 0.5+
        # https://github.com/readthedocs/sphinx_rtd_theme/issues/1014
        env.set('CI', True)
