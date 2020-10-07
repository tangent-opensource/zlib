name = 'zlib'

version = '1.2.11-ta.1.1.0'

authors = [
    'benjamin.skinner',
]

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
]

@early()
def private_build_requires():
    import sys
    if 'win' in str(sys.platform):
        return ['visual_studio']
    else:
        return ['gcc-7']

build_system = "cmake"

def commands():

    # Split and store version and package version
    split_versions = str(version).split('+')
    env.ZLIB_VERSION.set(split_versions[0])
    env.ZLIB_PACKAGE_VERSION.set(split_versions[1])

    env.ZLIB_ROOT.set( "{root}" )
    env.ZLIB_ROOT_DIR.set( "{root}" )
    env.ZLIB_LIB_DIR.set( "{root}/lib" )
    env.ZLIB_INCLUDE_DIR.set( "{root}/include" )

    env.PATH.append( "{root}/bin" )