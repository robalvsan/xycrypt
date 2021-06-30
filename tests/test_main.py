import pytest
import random
import os
import pandas as pd
import string

from constants import CURRENT_WORKING_DIRECTORY
from constants import DEFAULT_FILEPATH
from constants import DEFAULT_FILE_EXAMPLE
from prompts.prompts import check_filename
from prompts.prompts import check_filepath
from xycrypt.xycrypt import generate_encryption_obj
from xycrypt.xycrypt import encrypt_df
from xycrypt.xycrypt import decrypt_df

test_data = [
    ("whatever.xlsx", True),
    ("whatever.xlsx.csv", False),
    ("whatever", False),
    ("whatever name file  .xlsx", True),
    ("whatever name file.xlsx", True),
    ("whatever namefile.xlsx", True),
    ("whatever   .xlsx    .csv", False),
    (".xlsx", True),
    (".xls", False),
]


@pytest.mark.parametrize("input_filename,expected", test_data)
def test_check_filename(input_filename, expected):
    assert check_filename(input_filename) == expected, "The method check_filename is not returning correct results"


test_data = [
    (DEFAULT_FILE_EXAMPLE, DEFAULT_FILEPATH, True),
    (".xlsx", "wrong_path", False),
    ("whatever.xlsx.csv", DEFAULT_FILEPATH, False),
    ("whatever", "wrong_path", False),
    ("whatever name file  .xlsx", "wrong_path", False),
    ("whatever   .xlsx    .csv", "wrong_path", False),
    (".xls", "wrong_path", False),
]


@pytest.mark.parametrize("input_filename,input_filepath,expected", test_data)
def test_check_filepath(input_filename, input_filepath, expected):
    assert (
        check_filepath(input_filename, input_filepath) == expected
    ), "The method check_filepath is not returning correct results"


def test_simple_encryption():
    letters = string.ascii_lowercase
    length = 7
    random_pwd = "".join(random.choice(letters) for _ in range(length))
    random_str = "".join(random.choice(letters) for _ in range(length))
    encryption_obj, _ = generate_encryption_obj(random_pwd)

    encrypted_obj_1 = encryption_obj.encrypt(random_str.encode())
    encrypted_obj_2 = encryption_obj.encrypt(random_str.encode())
    decrypted_obj_1 = encryption_obj.decrypt(encrypted_obj_1)
    decrypted_obj_2 = encryption_obj.decrypt(encrypted_obj_2)

    assert random_str == decrypted_obj_1.decode() == decrypted_obj_2.decode()


def test_encryption_upon_dataset():
    letters = string.ascii_lowercase
    length = 8
    random_pwd = "".join(random.choice(letters) for _ in range(length))
    df = pd.read_excel(os.path.join(CURRENT_WORKING_DIRECTORY, DEFAULT_FILEPATH, DEFAULT_FILE_EXAMPLE))
    df_copy = df.copy()
    sensitive_features = [df.columns[df.shape[1] - 1]]

    encryption_obj, _ = generate_encryption_obj(_symmetric_key=random_pwd)

    # Encryption
    encrypt_df(df, sensitive_features, encryption_obj)

    # Decryption
    decrypt_df(df, sensitive_features, encryption_obj)

    assert df[df.columns[df.shape[1] - 1]].equals(
        df_copy[df.columns[df.shape[1] - 1]].astype(str)
    ), "The encryption/decryption process was not correctly done"
