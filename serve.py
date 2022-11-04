__all__ = ['route_info', 'app']

# %% ../nbs/serve.ipynb 3
from datascience_toolkits.fastapi import create_app, serve
from airt.core import handle_airt_request

# %% ../nbs/serve.ipynb 4
route_info = [{
    "path": "/",
    "method": "post",
    "endpoint": handle_airt_request
}]

app = create_app(route_info)
serve(app, port=8000)
