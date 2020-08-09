from behave import given, when, then, step  # pylint: disable=no-name-in-module

@given(u'я загружаю страницу "http://qa-assignment.oblakogroup.ru/board/example"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given я загружаю страницу "http://qa-assignment.oblakogroup.ru/board/example"')


@then(u'долна открыться страница содержащая доску с задачами')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then долна открыться страница содержащая доску с задачами')
