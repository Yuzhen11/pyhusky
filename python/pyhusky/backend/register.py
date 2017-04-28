# Copyright 2016 Husky Team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import python.pyhusky.backend.library.functional as functional
import python.pyhusky.backend.library.linear_regression as LinearR
import python.pyhusky.backend.library.logistic_regression as LogisticR
import python.pyhusky.backend.library.word as word

def register_func():
    # register
    functional.register_all()
    LinearR.register_all()
    LogisticR.register_all()
    word.register_all()
