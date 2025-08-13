"""
Behave step: checks that two required keywords appear in the agent's response.

This is used by:
  Then the response should contain all of "<keyword1>" and "<keyword2>"
"""

from behave import then

@then('the response should contain all of "{keyword1}" and "{keyword2}"') #type: ignore[no-untyped-def]
def step_response_contains_both(ctx, keyword1, keyword2):
    """
    Validates both keywords appear in ctx.data["text"] from the earlier When step.

    Args:
        ctx: Behave context; requires ctx.data to be set by the 'When I ask "<query>"' step.
        keyword1 (str): First keyword to check.
        keyword2 (str): Second keyword to check.
    """
    text = (ctx.data or {}).get("text", "")
    low = text.lower()
    assert keyword1.lower() in low, f"Expected '{keyword1}' in response: {text!r}"
    assert keyword2.lower() in low, f"Expected '{keyword2}' in response: {text!r}"
