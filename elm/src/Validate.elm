--  Copyright
--    2019 Department of Dermatology, School of Medicine, Tohoku University
--
--  Licensed under the Apache License, Version 2.0 (the "License");
--  you may not use this file except in compliance with the License.
--  You may obtain a copy of the License at
--
--      http://www.apache.org/licenses/LICENSE-2.0
--
--  Unless required by applicable law or agreed to in writing, software
--  distributed under the License is distributed on an "AS IS" BASIS,
--  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
--  See the License for the specific language governing permissions and
--  limitations under the License.


module Validate exposing (isValidCategoryName, isValidProjectName)


isValidCategoryName : String -> Bool
isValidCategoryName string =
    if string == "" then
        False

    else
        True


isValidProjectName : String -> Bool
isValidProjectName string =
    if string == "" then
        False

    else
        True
