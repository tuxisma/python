import json
import random
import time
import os

from cerberus import Validator
from flask import Flask, request
import requests

schema = {'name': {'type': 'string'}}
v = Validator(schema)
document = {'name': 'Ismael Garcia'}
print(v.validate(document))



template_param_map = {
    'ResetAccountPassword': {
        'requestor': {'type': 'string', 'required': True},
        'serviceName': {'type': 'string', 'required': True},
        'requestedAccountName': {'type': 'string', 'required': True},
        'requestedPassword': {'type': 'string', 'required': True},
    },
    'o365Setup': {
        'o365Params': {
            'required': True,
            'type': 'dict',
        },
        'ownerUsername': {'type': 'string', 'required': True},
        'mailboxName': {'type': 'string', 'required': True},
        'groupName': {'type': 'string', 'required': True},
        'email': {'type': 'string', 'required': True},
    }
}