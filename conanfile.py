from conan import ConanFile
from conan.errors import ConanException, ConanInvalidConfiguration
from conan.tools.gnu import PkgConfig
from conan.tools.system.package_manager import Apt
import os


class LibV4L2Conan(ConanFile):

    name = "v4l2"
    version = "system"

    description = "API for accessing video capture devices"
    topics = ("v4l2", "devices", "enumerating")
    url = "https://github.com/TUM-CONAN/conan-v4l2-system"
    homepage = "https://git.linuxtv.org/v4l-utils.git"
    license = "GPL-2.0-or-later", "LGPL-2.1-or-later"

    settings = "os"

    def system_requirements(self):
        Apt(self).install(["libv4l-dev", ])

    def validate(self):
        if self.settings.os != "Linux":
            raise ConanInvalidConfiguration("libv4l2 is only supported on Linux.")

    def package_info(self):
        pkg_config = PkgConfig(self, "libv4l2")
        pkg_config.fill_cpp_info(self.cpp_info, is_system=True)

