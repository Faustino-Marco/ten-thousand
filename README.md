# LAB - Class 06
## Project: Ten Thousand (v. 1.1)
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
  - Any tests of note?
    - Calculate score tests all pass
      - `calculate_score()` function in code uses loops that work beyond the hard-coded tests provided.
  - Describe any tests that you did not complete, skipped, etc
    - As of time of writing I have not completed any of the stretch goals yet.