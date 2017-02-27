from conans import ConanFile, CMake


class CrowConanFile(ConanFile):
    name = 'crow'
    author = 'Jaeseung Ha'
    description = 'A fast micro web framework for C++'
    version = 'master'
    url = 'https://github.com/javierjeronimo/crow'
    license = 'https://github.com/ipkn/crow/blob/master/LICENSE'
    generators = 'cmake'
    settings = 'os', 'compiler', 'build_type', 'arch'

    requires = 'Boost/1.60.0@lasote/stable', 'OpenSSL/1.0.2j@lasote/stable'

    def source(self):
        self.run('git clone https://github.com/javierjeronimo/crow.git')

    def package(self):
        self.copy('*.h', dst='include', src='crow/include')
        self.copy('*.h', dst='include/crow', src='crow/include/crow')
        self.copy('*.hpp', dst='include/crow', src='crow/include/crow')
