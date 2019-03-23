#   Copyright
#     2019 Department of Dermatology, School of Medicine, Tohoku University
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
from pathilico.app.header import Api


class MenuModel(object):
    def __init__(self):
        self.file_names = tuple()
        self.file_paths = tuple()


def update_explored_file_names_and_paths(model, names, paths):
    model.menu.file_names = names
    model.menu.file_paths = paths
    return model


def get_explored_file_names_and_paths(model):
    r = (
        model.menu.file_names,
        model.menu.file_paths
    )
    return r


Api.register(MenuModel)
Api.register(update_explored_file_names_and_paths)
Api.register(get_explored_file_names_and_paths)
