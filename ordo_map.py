import plugin
from .screens.map_screen import MapScreen

class MapPlugin(plugin.PluginObject):

	def get_main_screen():
		return MapScreen()

	def get_screens():
		return [MapScreen()]