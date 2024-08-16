import folium
from folium import IFrame
from branca.element import Element, MacroElement

mapObj = folium.Map(location=[24.3800437, 88.5836289], zoom_start=10)

sidebar_html = """
<div style="position: fixed; 
            top: 10px; left: 10px; width: 250px; height: 200px; 
            border:2px solid grey; z-index:9999; font-size:14px;
            background-color:white; padding: 10px;">
    <h4>Map Details</h4>
    <p>Latitude: 24.3800437</p>
    <p>Longitude: 88.5836289</p>
    <p>Zoom Level: 10</p>
    <p>Additional details can be added here.</p>
</div>
"""

iframe = IFrame(sidebar_html, width=300, height=250)
popup = folium.Popup(iframe, max_width=300)

folium.Marker(location=[24.3800437, 88.5836289], popup=popup).add_to(mapObj)


class CustomElement(MacroElement):
    def __init__(self, html_content):
        super().__init__()
        self._name = 'CustomElement'
        self.html = Element(html_content)


    def render(self, **kwargs):
        super().render(**kwargs)
        figure = self.get_root()
        figure.html.add_child(self.html)


floating_sidebar = CustomElement(sidebar_html)
mapObj.get_root().add_child(floating_sidebar)


mapObj.save("index.html")


