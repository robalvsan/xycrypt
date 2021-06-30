from datetime import datetime

from constants import CURRENT_WORKING_DIRECTORY
from constants import DEFAULT_FILEPATH
from constants import SALT_PROMPT_EXPLANATION
from prompts.prompts import ask_for_action
from prompts.prompts import ask_for_filename
from prompts.prompts import ask_for_salt
from prompts.prompts import ask_for_symmetric_key
from prompts.prompts import read_df
from xycrypt.xycrypt import decrypt_df
from xycrypt.xycrypt import encrypt_df
from xycrypt.xycrypt import generate_encryption_obj


if __name__ == "__main__":
    valid_filename = ask_for_filename()
    df, sensitive_features = read_df(valid_filename)
    action = ask_for_action()

    if action == "E":
        symmetric_key = ask_for_symmetric_key(action="E")
        encryption_obj, salt = generate_encryption_obj(_symmetric_key=symmetric_key)
        print(f"\n{SALT_PROMPT_EXPLANATION}: {salt}")
        encrypt_df(df, sensitive_features, encryption_obj)
        df.to_excel(
            f"{CURRENT_WORKING_DIRECTORY}/{DEFAULT_FILEPATH}/{valid_filename}_"
            f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}_encrypted.xlsx",
            index=False,
        )
    elif action == "D":
        symmetric_key = ask_for_symmetric_key(action="D")
        salt = ask_for_salt()
        encryption_obj, salt = generate_encryption_obj(_symmetric_key=symmetric_key, salt=salt)
        decrypt_df(df, sensitive_features, encryption_obj)
        df.to_excel(
            f"{CURRENT_WORKING_DIRECTORY}/{DEFAULT_FILEPATH}/{valid_filename}_"
            f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}_decrypted.xlsx",
            index=False,
        )
