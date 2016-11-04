"""Tests the Python3 implementation of hug_explainable"""
import pytest
import hug

from hug_explainable import Explainable


@hug.get()
@hug.local()
def my_code(explanation: Explainable):
    with explanation("Doing maths", 10):
        answer = 10 + 10
        return {'answer': answer, 'explanation': explanation}


def test_hug_explainable():
    """Test to ensure hug_explainable works as expected"""
    for results in (my_code(), hug.test.get(__name__, 'my_code').data):
        assert results['answer'] == 20
        explanation = results['explanation']
        assert explanation
        assert len(explanation) == 1
        assert explanation[0]['took'] > 0
        assert explanation[0]['Doing maths'] == 10


