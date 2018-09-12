import mama, os

class dlib(mama.BuildTarget):
    
    def dependencies(self):
        pass

    def configure(self):
        self.add_cmake_options(
            'DLIB_NO_GUI_SUPPORT=TRUE',
            'DLIB_ENABLE_ASSERTS=OFF',
            'DLIB_PNG_SUPPORT=OFF',
            'DLIB_JPEG_SUPPORT=OFF',
            'DLIB_GIF_SUPPORT=OFF',
            'DLIB_LINK_WITH_SQLITE3=OFF',
            'DLIB_USE_CUDA=OFF',
            'DLIB_USE_LAPACK=OFF')
        if self.linux:
            self.add_cl_flags('-Wno-tautological-constant-compare')

        # macOS and iOS have Accelerate.framework
        if self.macos or self.ios:
            self.add_cmake_options('DLIB_USE_BLAS=ON')
        elif self.openblas:
            self.add_cmake_options('DLIB_USE_BLAS=ON')
            self.inject_products('dlib', 'OpenBLAS', 'OPENBLAS_INCLUDE', 'OPENBLAS_LIBS')
        else:
            self.add_cmake_options('DLIB_USE_BLAS=OFF')

    def package(self):
        self.default_package()
        if self.ios or self.macos:
            self.export_syslib('-framework Accelerate')
