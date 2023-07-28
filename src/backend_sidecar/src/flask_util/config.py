# Copyright IBM Corp. All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0

from consts import *

class BaseConfig(object):
    app_name = "backend_sidecar"
    root_path = FLASK_ROOT_PATH
    
class BackendConfig(BaseConfig):
    app_name = "backend_sidecar"
    PREPARED_DIR=PREPARED_DIR
    SIGNED_DIR=SIGNED_DIR
   
