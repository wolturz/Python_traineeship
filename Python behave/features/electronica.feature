Feature: Battery calculations assignment

  The battery calculation module is called with parameters. The
  parameters decide which calculation is made, i.e. when called
  with Uk and Rl, I will be calculated.

  Scenario Outline: Calculate I from Uk and Rl
    Given the battery calculation module is online and available
    When I call the battery calculation module with <Uk> and <Rl>
    Then The module calculates the correct value of <I>

    Examples: Calculate current I as Uk / Rl
      |  Uk |  Rl |   I |
      | 0.0 | 2.5 | 0.0 |
      | 5.0 | 2.5 | 2.0 |