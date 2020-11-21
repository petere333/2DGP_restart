# determine path for dll and other data files
import os
from importlib import util
spec = util.find_spec('pico2d')
#print(spec.submodule_search_locations)
if len(spec.submodule_search_locations) > 0:
	os.environ['PYSDL2_DLL_PATH'] = spec.submodule_search_locations[0] + '/DLL'
	os.environ['PICO2D_DATA_PATH'] = spec.submodule_search_locations[0] + '/data'
else:
	# for pyinstaller, we need to specify the foler differently
	os.environ['PYSDL2_DLL_PATH'] = './pico2d'
	os.environ['PICO2D_DATA_PATH'] = './pico2d'
