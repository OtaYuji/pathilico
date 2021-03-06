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
from pathilico.pygletelm.effect import Subscriptions, notify_every
from pathilico.app.message import Msg
from pathilico.app.header import Api


def subscriptions(model):
    if Api.is_app_mode(model, "annotation") and Api.is_autosave_enabled(model):
        return Subscriptions(notify_every(Msg.ExecSaveToDatabase, sec=5))
    return Subscriptions()
