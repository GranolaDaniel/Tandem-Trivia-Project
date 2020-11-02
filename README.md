# Tandem Trivia Game

A CLI-based trivia game. Uses [PyInquirer](https://github.com/CITGuru/PyInquirer) for the UI.

### What's inside?

Here's a quick look at at the files and directories you'll find in this project:

```text
    .
    ├── triviagame/
    │   ├── __init__.py
    │   ├── gamelogic.py
    │   ├── helpers.py
    │   ├── triviagame.py
    │   └── Apprentice_TandemFor400_Data.json
    ├── tests/
    │   └── helpers_test.py
    ├── .gitignore
    ├── README.md
    └── requirements.txt
```
1.  **`/triviagame`**: Contains all of the files that are used to run the game.

    1.  **`/gamelogic.py`**: Contains the function for actually running the game and displaying the score to the user at the end.
    1.  **`/helpers.py`**: Contains functions for parsing a JSON file containing the questions and answers for the game, and a function for formatting that parsed file for use with PyInquirer's prompt method.
    1.  **`/triviagame.py`**: Specifies which JSON to use for questions and answers, and calls run_game to start the game.
    1.  **`/Apprentice_TandemFor400_Data.json`**: The JSON file containing questions and answers.
1.  **`/tests`**: Contains the test file.

    1.  **`/helpers_test.py`**: Tests `helpers.test_validate` to ensure that it correctly compares a user's answer with the correct answer.

### Playing the game

1. First, clone the repo. From the CLI:

   ```shell
   $ git clone https://github.com/GranolaDaniel/Tandem-Trivia-Project.git
   ```
1. Next, start up a virtual environment using venv.
    1. For MacOS and Unix:
        ```shell
        $ cd Tandem Trivia Project
        $ python -m venv env
        $ source env/bin/activate
        ```
    1. For Windows:
         ```shell
        $ cd Tandem Trivia Project
        $ python -m venv env
        $ source env\Scripts\activate.bat
        ```
1. Then, upgrade pip and install the dependencies.
    ```shell
    $ pip install --upgrade pip
    $ pip install -r requirements.txt
    ```
1. Lastly, start the game!
   ```shell
   $ cd triviagame
   $ python triviagame.py
   ```

### Running the test

1. From the tests directory, run:

```shell
   $ python -m unittest helpers_test.py
   ```

### Things to add in the future

1. Themes! PyInquirer enables you to cheange the color of the prompts, so I'd like to implement different themes that a user can choose before starting the quiz. This might inclide dark mode vs. light mode, and some more accessible color options.
1. Add in more unit tests. Specifically for `gamelogic.rungame`.
1. Enable users to start a new game automatically, and give them new, unique answers.
1. Add in more question sets, and allow the user to select which one they'd like to try.
1. Adjust `gamelogic.run_game` so that you can't set num_questions to more than 10.