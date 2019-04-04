from behave import step
from calc import add


result = None


@step('I add "{value_1}" to "{value_2}"')
def testSum(context, value_1, value_2):
    context.result = float(add(float(value_1), float(value_2)))


@step('the result must be "{resultAdd}"')
def testSumResult(context, resultAdd):
    assert context.result == float(resultAdd)
