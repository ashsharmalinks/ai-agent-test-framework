from behave import given, when, then
from common.http_client import make_client

client = make_client()

@given("the API is available") # type: ignore
def step_api_available(ctx):
    r = client.get("/health")
    assert r.status_code == 200

@when('I ask "{q}"')  # type: ignore
def step_i_ask(ctx, q):
    ctx.resp = client.post("/chat", json={"query": q})
    ctx.data = ctx.resp.json()

@then("I receive a non-empty response") # type: ignore
def step_non_empty(ctx):
    assert ctx.data.get("text")

@then("the HTTP status code is 200") # type: ignore
def step_status_ok(ctx):
    assert ctx.resp.status_code == 200
