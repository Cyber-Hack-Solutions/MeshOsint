# Tool designed by Cyber-Hack Solutions LLC
# For educational purposes only; use responsibly.

from resources import *
import folium
import webbrowser
from rich import print


# get_current_dir = os.getcwd()

def plot_nodes_on_map(nodes):
    """
    Plots node locations on a map using their latitude and
    longitude. Centers map on the first node, applies a
    dark theme, and adds custom tower icons for each node.
    Each marker displays a popup with node details. The
    map is saved as an HTML file and opens in the browser.
    """

    if not nodes:
        print("\n[bold][red]No nodes to display.[/red][/bold]")
        return

    # Center the map on the first node or default to (0, 0)
    initial_location = [nodes[0]['latitude'], nodes[0]['longitude']]
    
    # Create the map with a dark tile style
    map = folium.Map(location=initial_location, zoom_start=12, tiles='CartoDB dark_matter')

    # Add custom tile layer with attribution
    folium.TileLayer(
        tiles='Stamen Toner',
        attr='&copy; <a href="http://stamen.com">Stamen Design</a> | Data by <a href="http://openstreetmap.org">OpenStreetMap</a>',
        name='Stamen Toner',
        control=True
    ).add_to(map)

    # Add markers for each node
    for node in nodes:
        lat = node['latitude']
        long = node['longitude']
        long_name = node.get('longName', 'Unknown Node')
        battery = node['battery']
        uptime = node['uptime']


        # print(long_name,lat,long)

        # Use CustomIcon tower.png
        icon = folium.CustomIcon(icon_image='modules/icons/tower.png', icon_size=(30, 30))  # Adjust size as needed

        # Info Cloud
        popup_content = f"""
        <div style='background-color: #5A5A5A; color: #00FF00; font-weight: bold; padding: 10px; border-radius: 5px; width: 500px; font-size: 16px;'>
            <p><strong>Name:</strong> {long_name}</p>
            <p><strong>Battery:</strong> {battery}</p>
            <p><strong>Uptime:</strong> {uptime}</p>
        </div>"""

        folium.Marker(
            location=[lat, long],
            popup=popup_content,
            icon=icon
        ).add_to(map)

    # Save the map to an HTML file
    html_file = f'{get_current_dir}/modules/map/nodes_map.html'

    map.save(html_file)
    print(f"\n[bold][orange3] Map has been saved to [cyan]'{html_file}'[/cyan]. Opening in a web browser...[/orange3][/bold]")

    # Open the HTML file in the default web browser
    webbrowser.open(html_file)

