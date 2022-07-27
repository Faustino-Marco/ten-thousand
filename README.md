# LAB - (06 - 09)
## Project: Ten Thousand (v. 2.1)
#### Author: Faustino Marco Simpliciano
<hr>
Command line version of the dice game, 'Ten Thousand.'
Expanding understanding of Python standard library.
<hr>

### Links and Resources
- back-end server url: (N/A)
- front-end application: (N/A)

### Setup
<!-- .env requirements (where applicable) -->
- Pytest
<!-- 
- PORT - Port Number
- DATABASE_URL - URL to the running Postgres instance/db -->
- How to initialize/run your application (where applicable) e.g. python main.py
  - `ten_thousand/game_logic.py`
  - `pytest` 
    - `test_calculate_score.py`
    - `test_roll_dice.py`
- How to use your library (where applicable)
- Tests
  - How do you run tests?
    - Pytest (ptw)
    - Sim files in `/version_2`
  - Any tests of note?
    - Version 1
      - Calculate score tests all pass
        - `calculate_score()` function in code uses loops that work beyond the hard-coded tests provided.
    - Version 2
      - All sim scripts matched EXCEPT for last
        
  - Describe any tests that you did not complete, skipped, etc
    - I may have coded past the requirements, or I may have misunderstood the rules we're targeting to program.
        - I will update in later versions.
    - As of time of writing I have not completed any of the stretch goals yet.