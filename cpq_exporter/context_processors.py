import versioneer


def exporter_version(request):
        return {'exporter_version': versioneer.get_version()}
