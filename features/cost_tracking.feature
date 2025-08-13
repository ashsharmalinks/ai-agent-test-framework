Feature: AI Agent Cost Tracking
  Ensure AI agent stays within cost limits per request.

  Scenario Outline: Cost per query should be within budget
    Given the API is available
    When I ask "<query>"
    Then the cost should not exceed <max_cost>

    Examples:
      | query                 | max_cost |
      | What is 2+2?          | 0.01     |
      | Capital of France     | 0.02     |
