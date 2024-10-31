# Tool designed by Cyber-Hack Solutions LLC
# For educational purposes only; use responsibly.

from resources import *
from modules.banner import banner
from rich import box, print
from rich.table import Table
import requests
import time
from modules.plot_map import plot_nodes_on_map

# Define URLs to scrape
urls = {
    "nodes": "https://meshmap.net/nodes.json",
    "devices": "https://meshtastic.liamcottle.net/api/v1/stats/hardware-models"
}

def request_permission():
    """Display banner and script information"""

    print(f"\n [bold][medium_spring_green]The Script Will Send A Request to The URLs Below To Capture Meshtastic Data:[/medium_spring_green][/bold]")
    print(f"\n [bold][medium_spring_green] [1] [magenta]{urls['nodes']}[/magenta][/medium_spring_green][/bold]")
    print(f"\n [bold][medium_spring_green] [2] [magenta]{urls['devices']}[/magenta][/medium_spring_green][/bold]")
    print(f"\n [bold][medium_spring_green]Continue? (Y/N)[/medium_spring_green][/bold]")



def format_uptime(seconds):
    """Converts uptime to a more readable format"""

    days = seconds // (24 * 3600)
    hours = (seconds % (24 * 3600)) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{days}d {hours}h {minutes}min {seconds}s"

# Main loop
active = True
number_input = True

while active:
    clear_screen()
    banner()
    request_permission()
    input_field()

    ask = input().lower()

    if ask == "y":
        try:
            clear_screen()
            banner()

            # Fetch data from URLs
            response = requests.get(urls["nodes"])
            print(f"\n[bold][orange3] Fetching Data... [/orange3][/bold]")

            message = response.json()

            response_devices = requests.get(urls["devices"])
            message_devices = response_devices.json()
            hardware = message_devices['hardware_model_stats']

            # Set up tables
            table_main_title = "Meshtastic Dump"
            device_table_title = "Devices By Popularity"

            table = Table(
                title=f"\n[bold][red][/red][medium_spring_green]{table_main_title}[/medium_spring_green][/bold]",
                show_header=True,
                header_style="bold orange3",
                show_lines=True,
                min_width=50,
                expand=True,
                box=box.DOUBLE_EDGE,
                border_style="cyan",
                title_justify="left",
            )
            table.add_column("Long Name", justify="left", style="cyan", no_wrap=True)
            table.add_column("Model", justify="left", style="magenta")
            table.add_column("Role", justify="left", style="magenta")
            table.add_column("Latitude", justify="left", style="green")
            table.add_column("Longitude", justify="left", style="green")
            table.add_column("Modem Present", justify="left", style="green")
            table.add_column("Battery Level", justify="left", style="green")
            table.add_column("Voltage", justify="left", style="green")
            table.add_column("Uptime", justify="left", style="green")

            table_devices = Table(
                title=f"\n[bold][red][/red][medium_spring_green]{device_table_title}[/medium_spring_green][/bold]",
                show_header=True,
                header_style="bold orange3",
                show_lines=True,
                min_width=50,
                expand=True,
                box=box.DOUBLE_EDGE,
                border_style="cyan",
                title_justify="left",
            )
            table_devices.add_column("Model", justify="left", style="magenta")
            table_devices.add_column("Number of Devices Globally", justify="left", style="magenta")

            # Prompt user to enter the number of results and handle non-numeric input
            while number_input:
                clear_screen()
                banner()

                print(f"\n[bold][green][blink] Data Gathered!![/blink] [/green][/bold]\n")
                print(f"\n[bold][medium_spring_green] Enter the Number of Results to Display for Meshtastic Dump Table (1 or more):[/medium_spring_green][/bold]", end="")
                
                input_field()
                
                try:
                
                    result_range = int(input())
                    if result_range <= 0:
                        clear_screen()
                        banner()
                        print("\n[bold][red] Please enter a number greater than 0.[/red][/bold]")
                        time.sleep(2)
                    else:
                        break

                except ValueError:
                    print(f"\n[bold][red] Invalid input:[/red][yellow] Please enter a valid number![/yellow][/bold]\n")
                    time.sleep(2)

            clear_screen()

            # Populate table with node data and prepare data for plotting
            nodes = []
            for count, (key, value) in enumerate(message.items()):
                if count >= result_range:
                    break
                long_name = value.get("longName", "")
                model_name = value.get("hwModel", "")
                model_role = value.get("role", "")

                # Converts latitude and longitude from microdegrees to decimal degrees
                model_lat = value.get("latitude", 0) / 1e6  # Convert latitude to decimal
                model_long = value.get("longitude", 0) / 1e6  # Convert longitude to decimal
                model_modem = value.get("modemPreset", "")
                model_voltage = value.get("voltage", "")
                model_battery = f"{value.get('batteryLevel', '')}%"
                model_uptime = format_uptime(value.get("uptime", 0))


                # Append node info for plotting
                nodes.append({
                    "latitude": model_lat / 10,
                    "longitude": model_long / 10,
                    "longName": value.get("longName", "Node"),
                    "battery": model_battery,
                    "uptime": model_uptime,
                })

                # :.5f Format as strings with 5 decimal places for display
                table.add_row(
                    f"[bold][yellow1]{long_name}[/yellow1][/bold]",
                    f"[bold][yellow1]{model_name}[/yellow1][/bold]",
                    f"[bold][medium_spring_green]{model_role}[/medium_spring_green][/bold]",
                    f"[bold][bright_magenta]{model_lat/10:.5f}[/bright_magenta][/bold]",
                    f"[bold][bright_magenta]{model_long/10:.5f}[/bright_magenta][/bold]",
                    f"[bold][bright_magenta]{model_modem}[/bright_magenta][/bold]",
                    f"[bold][bright_magenta]{model_battery}[/bright_magenta][/bold]",
                    f"[bold][bright_magenta]{model_voltage}[/bright_magenta][/bold]",
                    f"[bold][bright_magenta]{model_uptime}[/bright_magenta][/bold]",
                )

            # Populate `table_devices` with device data
            for device in hardware:
                name = device['hardware_model_name']
                amount = device["count"]
                table_devices.add_row(
                    f"[bold][bright_magenta]{name}[/bright_magenta][/bold]",
                    f"[bold][yellow1]{amount}[/yellow1][/bold]"
                )

            # Display tables
            banner()
            print(table)
            print(table_devices)

            # Plot nodes on the browser
            plot_nodes_on_map(nodes)

            print("\n[bold][yellow1] Press Enter to Continue [/yellow1][/bold]\n", end="")
            input()

            html_file = f'{get_current_dir}/modules/map/nodes_map.html'
            
            if os.path.exists(html_file):
                cmd = ["rm", "-r", html_file]
                subprocess.run(cmd)
            else:
                print(f"[bold][yellow1]File '{html_file}' does not exist.[/yellow1][/bold]")


        except requests.exceptions.ConnectionError:
            print("\n\n[bold][red] Error:[/red][yellow] Unable to connect to the internet. Please check your network connection and try again.[/yellow][/bold]\n")
            time.sleep(3)
        except requests.exceptions.RequestException as e:
            print(f"\n\n[bold][red] An error occurred:[/red] [yellow]{e}[/yellow][/bold]\n")
            time.sleep(3)

    elif ask == "n":
        print("\n[bold][red] Exiting...[/red][/bold]\n")
        time.sleep(2)
        active = False

    else:
        clear_screen()
        banner()
        print("\n[bold][red] Error:[/red][yellow] Input Not Recognized![/yellow][/bold]\n")
        time.sleep(2)
