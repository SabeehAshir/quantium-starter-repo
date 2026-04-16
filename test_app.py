# test_app.py
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()  # This magically fixes the PATH issue!

from app import app

def test_header_is_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element(".header-title", timeout=10)
    
    header_text = dash_duo.find_element(".header-title").text
    assert header_text == "Soul Foods: Pink Morsel Sales Visualizer"

def test_visualization_is_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)

def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=10)