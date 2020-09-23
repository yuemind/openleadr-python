# SPDX-License-Identifier: Apache-2.0

# Copyright 2020 Contributors to OpenLEADR

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .enums import STATUS_CODES

class OpenADRError(Exception):
    def __init__(self, status, description):
        assert status in self.status_codes.values, f"Invalid status code {status} while raising OpenADRError"
        super().__init__()
        self.status = status
        self.description = description

    def __str__(self):
        return f'Error {self.status} {self.status_codes[self.status]}: {self.description}'