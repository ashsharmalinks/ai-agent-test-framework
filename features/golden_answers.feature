Feature: Golden Answer Validation
  Validate that the AI agent returns known correct answers for key queries.

  Scenario Outline: Query returns correct golden answer
    Given the API is available
    When I ask "<query>"
    Then the response should match "<expected>"

    Examples:
      | query                 | expected             |
      | What is 2+2?          | 4                   |
      | capital of France     | Paris               |
      | Who wrote Hamlet?     | William Shakespeare |
