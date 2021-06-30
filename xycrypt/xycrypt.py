from base64 import b64decode
from base64 import b64encode
import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def generate_encryption_obj(_symmetric_key, salt=None):
    salt = os.urandom(16) if salt is None else b64decode(salt.encode("utf-8"))
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(_symmetric_key.encode()))
    return Fernet(key), b64encode(salt).decode("utf-8")


def encrypt_df(df, sensitive_features, encryption_obj):
    df_sensitive_features = df.filter(items=sensitive_features)
    df_tmp = df_sensitive_features.apply(lambda x: x.astype(str))
    df_sensitive_features_enc = df_tmp.applymap(lambda x: encryption_obj.encrypt(x.encode()))

    for sensitive_feature in sensitive_features:
        df[sensitive_feature] = df_sensitive_features_enc[sensitive_feature]
        df[sensitive_feature] = df[sensitive_feature].apply(lambda x: x.decode())


def decrypt_df(df, sensitive_features, encryption_obj):
    df_tmp = df.filter(items=sensitive_features)
    df_sensitive_features_dec = df_tmp.applymap(lambda x: encryption_obj.decrypt(x.encode()))
    for sensitive_feature in sensitive_features:
        df[sensitive_feature] = df_sensitive_features_dec[sensitive_feature]
        df[sensitive_feature] = df[sensitive_feature].apply(lambda x: x.decode())
