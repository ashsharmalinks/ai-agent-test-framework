Feature: Chat with AI Agent API
  As a client of the AI Agent
  I want to send a query and get a short response
  So that I can validate end-to-end behavior

  Scenario: Simple math question
    Given the API is available
    When I ask "What is 2+2?"
    Then I receive a non-empty response
    And the HTTP status code is 200

  Scenario: Retrieval tool
    Given the API is available
    When I ask "tool:retrieval: safety checks in agents"
    Then I receive a non-empty response
    And the HTTP status code is 200
