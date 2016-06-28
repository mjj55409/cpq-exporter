from distutils.core import setup
import versioneer

setup(
    name='cpq-exporter',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass()
)
