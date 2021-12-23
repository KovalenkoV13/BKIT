from behave import given, when
import main_DZ


@given('I send bot message {start}')
def step_impl(context, start: str):
    main_DZ.cmd_start(start)
@when('I send bot first message {go}')
def step_imp2(context, go: str):
    context.firstNum = main_DZ.cmd_start(go)