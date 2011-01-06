from distutils.core import setup

setup(
    name='pyclutter-screensaver',
    version='0.1',
    description='An example screensaver based on PyClutter',
    url='http://github.com/joh/pyclutter-screensaver',
    license='BSD',
    author='Johannes H. Jensen',
    author_email='joh@pseudoberries.com',
    
    requires=[
        'clutter (>=1.0.3)'
    ],
    
    # TODO: Absolute system paths like this should be avoided, but
    # unfortunately gnome-screensaver seems to only allow screensavers
    # which reside in a list of hard-coded system directories...
    data_files=[('/usr/lib/xscreensaver', ['pyclutter-screensaver.py']),
                ('share/applications/screensavers', ['pyclutter-screensaver.desktop'])]
)
