# Copyright (c) 2017 LSD - UFCG.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from controller.utils.monasca.client import MonascaClient

from controller.plugins.metric_source.base import MetricSource
import datetime


class MonascaMetricSource(MetricSource):
    def __init__(self, parameters):
        self.monasca = MonascaClient()
        self.parameters = parameters

    def get_most_recent_value(self, metric_name, options):
        dimensions = {"application_id": options["application_id"]}
        measurement = self.monasca.last_measurement(metric_name, dimensions)
        timestamp = datetime.datetime.strptime(
            measurement[0], '%Y-%m-%dT%H:%M:%S.%fZ')
        value = measurement[1]
        return timestamp, 100 * value
