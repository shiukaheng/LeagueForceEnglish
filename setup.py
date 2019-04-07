from distutils.core import setup
import py2exe

setup(options={'py2exe':{'bundle_files':1,'compressed':True}},
      zipfile = None,
      console = [{'script': 'LoLEng.py',
               'icon_resources': [(0, "LolEng.ico")]}])
