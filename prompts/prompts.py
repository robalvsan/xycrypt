import getpass
import os
import textwrap

import pandas as pd

from constants import ACTION_PROMPT
from constants import CURRENT_WORKING_DIRECTORY
from constants import DEFAULT_FILEPATH
from constants import FILENAME_PROMPT
from constants import FILENAME_PROMPT_ERROR
from constants import FILENAME_PROMPT_EXPLANATION
from constants import PWD_PROMPT
from constants import PWD_PROMPT_ERROR
from constants import PWD_PROMPT_EXPLANATION
from constants import SALT_PROMPT
from constants import SENSITIVE_COLUMNS_PROMPT
from constants import SENSITIVE_COLUMNS_PROMPT_ERROR
from constants import SENSITIVE_COLUMNS_PROMPT_EXPLANATION


def ask_for_symmetric_key(action):
    valid_prompt_result = False
    __symmetric_key = ""
    while valid_prompt_result is False:
        try:
            if action == "E":
                prompt_explanation = textwrap.dedent(PWD_PROMPT_EXPLANATION).strip()
                print(f"\n{prompt_explanation}")
            __symmetric_key = getpass.getpass(prompt=f"\n{PWD_PROMPT}: ")
            valid_prompt_result = True
        except Exception:
            print(textwrap.dedent(PWD_PROMPT_ERROR).strip())
    return __symmetric_key


def ask_for_sensitive_features():
    valid_prompt_result = False
    __sensitive_features = []
    while valid_prompt_result is False:
        try:
            prompt_explanation = textwrap.dedent(SENSITIVE_COLUMNS_PROMPT_EXPLANATION).strip()
            print(f"\n{prompt_explanation}")
            __sensitive_features: list = input(f"\n{SENSITIVE_COLUMNS_PROMPT}: ").split(",")
            if len(__sensitive_features) > 0:
                valid_prompt_result = True
            else:
                raise Exception
        except Exception:
            print(textwrap.dedent(SENSITIVE_COLUMNS_PROMPT_ERROR).strip())
    return __sensitive_features


def check_filename(input_filename: str) -> bool:
    len_input_filename = len(input_filename)
    find_xlsx = input_filename.find(".xlsx")
    return len_input_filename > 4 and find_xlsx != -1 and len_input_filename - find_xlsx == 5


def check_filepath(input_filename: str, filepath: str = DEFAULT_FILEPATH) -> bool:
    return os.path.isdir(os.path.join(CURRENT_WORKING_DIRECTORY, filepath)) and os.path.exists(
        os.path.join(CURRENT_WORKING_DIRECTORY, filepath, input_filename)
    )


def ask_for_filename():
    valid_prompt_result = False
    __filename = ""
    while valid_prompt_result is False:
        try:
            prompt_explanation = textwrap.dedent(FILENAME_PROMPT_EXPLANATION).strip()
            print(f"\n{prompt_explanation}")
            __filename = input(f"\n{FILENAME_PROMPT}: ")
            if check_filename(__filename) and check_filepath(__filename):
                valid_prompt_result = True
            else:
                raise Exception
        except Exception:
            print(f"\n\n{textwrap.dedent(FILENAME_PROMPT_ERROR).strip()}")
    return __filename


def validate_sensitive_features(df_columns: list, features: list) -> bool:
    return set(features).issubset(df_columns)


def read_df(filename):
    valid_reading_df = False
    __df = None
    features = []
    while valid_reading_df is False:
        features = ask_for_sensitive_features()
        __df = pd.read_excel(os.path.join(CURRENT_WORKING_DIRECTORY, DEFAULT_FILEPATH, filename))
        if validate_sensitive_features(__df.columns, features):
            valid_reading_df = True
        else:
            print(f"\n{SENSITIVE_COLUMNS_PROMPT_ERROR}")
    return __df, features


def ask_for_action():
    valid_prompt_result = False
    __action = ""
    while valid_prompt_result is False:
        __action = input(f"\n{ACTION_PROMPT}: ")
        if __action == "E" or __action == "D":
            valid_prompt_result = True
    return __action


def ask_for_salt():
    valid_prompt_result = False
    __salt = ""
    while valid_prompt_result is False:
        __salt = input(f"\n{SALT_PROMPT}: ")
        if len(__salt) != 0:
            valid_prompt_result = True
    return __salt
