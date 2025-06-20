# Copyright 2025 Ravetta Stefano
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict

from dataclass_wizard import JSONWizard

from ri_excel.model.reference_config import ReferenceConfig, ReferenceConfigType


@dataclass
class SheetConfig(JSONWizard):
    isMain: bool
    name: str
    reference: ReferenceConfig

    @staticmethod
    def new(is_main: bool, name: str, reference: ReferenceConfigType) -> SheetConfigType:
        return {
            'isMain': is_main,
            'name': name,
            'reference': reference,
        }


class SheetConfigType(TypedDict):
    isMain: bool
    name: str
    reference: ReferenceConfigType
