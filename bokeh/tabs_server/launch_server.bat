set BOKEH_LOC="C:\Users\RAN\AppData\Local\Continuum\anaconda3\Scripts\bokeh.exe"
cd..
%BOKEH_LOC% serve tabs_server --show --allow-websocket-origin=* --port 5006
rem pause
rem timeout 15
cd tabs_server