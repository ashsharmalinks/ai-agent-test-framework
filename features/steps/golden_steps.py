from behave import given, when, then
from difflib import SequenceMatcher
import requests

@then('the response should match "{expected}"') # type: ignore
def step_impl(context, expected):
    answer = context.resp.json()["text"].strip()
    similarity = SequenceMatcher(None, answer.lower(), expected.lower()).ratio()
    assert similarity > 0.9, f"Expected '{expected}', got '{answer}'"
