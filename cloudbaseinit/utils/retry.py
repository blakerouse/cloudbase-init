# Copyright 2017 Canonical Ltd.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import time


def retry(tries, try_delay=1):
    """Retry a function until success.

    Success is determined when the function doesn't raise an exception.

    :param tries: Maximum number of tries. Once max number of tries is
        reached the exception will be propogated up.
    :param try_delay: Number of seconds between retries.
    """
    if tries <= 0:
        raise ValueError("tries must be greater than 0")
    if try_delay < 0:
        raise ValueError("try_delay must be greater than 1")

    def wrap_retry(f):
        def _wrap_retry(*args, **kwargs):
            ftries, fdelay = tries, try_delay
            while ftries > 0:
                try:
                    return f(*args, **kwargs)
                except Exception:
                    if ftries == 1:
                        raise                    
                    time.sleep(fdelay)
                    ftries -= 1
        return _wrap_retry
    return wrap_retry
    