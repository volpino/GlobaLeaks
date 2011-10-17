from gluon.storage import Storage
from gluon.tools import Mail, Auth

import ConfigParser
import os.path

# XXX: find a better place for gleaks.cfg ;  $HOME if installed
projroot = os.path.abspath(__file__).rsplit('GlobaLeaks', 1)[0] + 'GlobaLeaks'
cfgfile = os.path.join(projroot, 'globaleaks', 'globaleaks.conf')

def copyform(form, settings):
    """Copy each form value into the specific settings subsection. """
    for name, value in form.iteritems():
        setattr(settings, name, value)
    settings.commit()

class ConfigFile(Storage):

    def __init__(self, cfgfile, section):
        super(ConfigFile, self).__init__()

        self._cfgfile = cfgfile
        # setting up confgiparser
        self._cfgparser = ConfigParser.ConfigParser()
        self._cfgparser.read([self._cfgfile])
        self._section = section

    def __getattr__(self, name):
        if name.startswith('_'):
            return self.__dict__.get(name, None)

        try:
            return self._cfgparser.get(self._section, name)
        except ConfigParser.NoOptionError:
            raise NameError(name)

    def __setattr__(self, name, value):
        # keep an open port with private attributes
        if name.startswith('_'):
            self.__dict__[name] = value
            return

        try:
            # XXX: Automagically discover variable type
            self._cfgparser.set(self._section, name, value)
        except ConfigParser.NoOptionError:
            raise NameError(name)

    def commit(self):
        self._cfgparser.write(open(self._cfgfile, 'w'))


