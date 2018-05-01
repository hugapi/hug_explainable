import time

import hug
from hug_explainable import Explainable


@hug.get()
def my_endpoint(hug_timer, explain: Explainable=False):
    results = {'took': hug_timer}
    with explain('Sleeping for allocated time:', 1):
        time.sleep(1)
    explain.insert_into(results)
    return results

    
