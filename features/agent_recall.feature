Feature: AI Agent Recall and Precision
  Ensure AI agent returns relevant and complete information.

  Scenario Outline: Recall/Precision benchmark
    Given the API is available
    When I ask "<query>"
    Then the response should contain all of "<keyword1>" and "<keyword2>"

    Examples:
      | query                       | keyword1 | keyword2  |
      | Tell me about the sun       | star     | solar     |
      | Capital of the UK           | London   | England   |
