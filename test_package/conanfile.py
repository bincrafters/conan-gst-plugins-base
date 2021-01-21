from conans import ConanFile, CMake, tools
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def requirements(self):
        self.requires("cmake/3.19.3")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            #os.environ["GST_DEBUG"] = "*:6"
            bin_path = os.path.join("bin", "test_package")
            self.run(bin_path, run_environment=True)
