# update and rebuild shaderc when updating
pkgname = "spirv-tools"
pkgver = "1.4.313.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSPIRV_WERROR=OFF",
    f"-DSPIRV-Headers_SOURCE_DIR={self.profile().sysroot / 'usr'}",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python"]
makedepends = ["spirv-headers"]
pkgdesc = "API and commands for processing SPIR-V modules"
license = "Apache-2.0"
url = "https://github.com/KhronosGroup/SPIRV-Tools"
source = f"{url}/archive/vulkan-sdk-{pkgver}.tar.gz"
sha256 = "6b60f723345ceed5291cceebbcfacf7fea9361a69332261fa08ae57e2a562005"
hardening = ["!vis", "!cfi"]

# Note: only some tests are run, the others need subfolders of gtest and effcee
# and some other stuff


@subpackage("spirv-tools-devel-static")
def _(self):
    self.depends = []
    self.install_if = []

    return ["usr/lib/*.a"]


@subpackage("spirv-tools-libs")
def _(self):
    self.subdesc = "shared library"
    self.renames = ["libspirv-tools-shared"]

    return ["usr/lib/*.so"]


@subpackage("spirv-tools-devel")
def _(self):
    self.depends += [
        self.parent,
        self.with_pkgver(f"{pkgname}-devel-static"),
        self.with_pkgver(f"{pkgname}-libs"),
    ]

    return self.default_devel()
