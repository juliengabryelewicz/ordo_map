from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy_garden.mapview import MapMarkerPopup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.storage.jsonstore import JsonStore
from kivy.clock import Clock
from functools import partial


class MapScreen(Screen):

	def __init__(self, **kwargs):
		super(MapScreen, self).__init__(**kwargs)
		self.store = JsonStore("parameters/ordo_map.json")
		self.markers = self.store.get('markers')
		self.ids["mapview"].lat = self.store.get('lat')
		self.ids["mapview"].lon = self.store.get('lon')
		self.ids["mapview"].zoom = self.store.get('zoom')
		Clock.schedule_once(self.load_markers, 1)

	def show_dialog(self, *args, **kwargs):
		marker=args[0]

		content_popup = BoxLayout(orientation='vertical')
		content_popup.add_widget(Label(text=marker.get("content"), markup=True))

		popup = Popup(title=marker.get("title"),content=content_popup,size_hint=(None, None), size=(marker.get("width_popup"), marker.get("height_popup")))
		popup.open()


	def load_markers(self, dt):
		for markerInfo in self.markers:
			marker_popup = MapMarkerPopup(
				lat=markerInfo.get("lat"),
				lon=markerInfo.get("lon"),
				popup_size=(230,130)
			)
			marker_popup.bind(on_release=partial(self.show_dialog, markerInfo))

			self.ids["mapview"].add_marker(marker_popup)
