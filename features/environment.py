# features/environment.py
from common.config import CFG
from common.server_lifecycle import start_server, stop_server
import requests

def before_all(context):
    # Start API server if running in live E2E mode
    context.proc = None
    if getattr(CFG, "e2e_mode", None) == "live":
        context.proc = start_server()

    # Global defaults for all steps
    context.base_url = "http://127.0.0.1:8000"
    context.resp = None
    context.data = None
    context.cost = None

def before_scenario(context, scenario):
    # Reset per-scenario data
    context.response = None
    context.data = None
    context.cost = None

def after_all(context):
    # Stop server if we started it
    if context.proc:
        stop_server(context.proc)
