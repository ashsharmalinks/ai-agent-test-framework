from behave import then

@then("the cost should not exceed {max_cost:g}") #type: ignore
def step_cost_not_exceed(ctx, max_cost: float):
    """
    Assert that the cost returned by the AI agent does not exceed `max_cost`.

    Args:
        ctx: Behave context with `ctx.data` set by the "When I ask ..." step.
        max_cost (float): Budget threshold parsed from Gherkin step.
    """
    # Prefer meta.cost (keeps all metrics in one place).
    cost = (ctx.data or {}).get("meta", {}).get("cost")

    # Fallback: top-level "cost" if your API exposes it there instead.
    if cost is None:
        cost = (ctx.data or {}).get("cost")

    assert cost is not None, (
        "No 'cost' found in response. Expected `meta.cost` (preferred) "
        "or top-level `cost`. Update the API to include it."
    )
    assert float(cost) <= float(max_cost), f"Cost {cost} exceeds budget {max_cost}"
