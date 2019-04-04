from behave import step
from calc import add


result = None


@step('I add "{value_1:d}" to "{value_2:d}"')
def testSum(context, value_1, value_2):
    global result
    result = add(value_1, value_2)


@step('the result must be "{resultAdd:d}"')
def testSumResult(context, resultAdd):
    assert result == resultAdd
