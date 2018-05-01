import time

import hug
from hug_explainable import explainable_toggle


@hug.get()
def my_endpoint(hug_timer, explain: explainable_toggle=explainable_toggle(False)):
    results = {'took': hug_timer}
    with explain('Sleeping for allocated time:', 1):
        time.sleep(1)
    explain.insert_into(results)
    return results
