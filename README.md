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
1.  **`/triviagame`**: Contains all of the main game files.

    1.  **`/gamelogic.py`**: 
    1.  **`/helpers.py`**: This has the navigation links for your pages.
    1.  **`/triviagame.py`**: This component is used in all of your pages to make sure they all use the same navigation. This is also where you will implement your skip link.
    1.  **`/Apprentice_TandemFor400_Data.json`**: The list of questions and answers that users are prompted with when playing the game.
1.  **`/tests`**: Contains the test files.

    1.  **`/helpers_test.py`**: This ensures that our navigation links have focus rings, which are important visual cues when navigating by keyboard.

### Playing the game

1. First, clone the repo. From the CLI:

   ```shell
   $ git clone https://github.com/GranolaDaniel/Tandem-Trivia-Project.git
   ```
1. Next, start up a virtual environment using venv and install the required dependencies
   ```shell
   $ cd Tandem Trivia Project
   $ python -m venv env
   $ source env/bin/activate
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

1. Themes!
1. More tests
1. Replay the game with new, unique questions