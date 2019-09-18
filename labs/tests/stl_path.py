import sys, os

# FIXME to the right path for trex_stl_lib
cur_dir = os.path.dirname(__file__)
api_dir = "trex_client/interactive"
sys.path.insert(0, os.path.join(cur_dir, api_dir))

STL_PROFILES_PATH = os.path.join(os.pardir, 'profiles')
