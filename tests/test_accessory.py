from hamcrest import assert_that, is_, equal_to

from one_block import accessory
from one_block.accessory import ButtonStyle, Option, Checkbox, Overflow


def test_button_no_style():
    button = accessory.Button('Click me', 'my-button', 'value')
    output = button.json()
    assert_that(output['type'], is_(equal_to('button')))
    assert_that(output['text'], is_(equal_to({
        'type': 'plain_text',
        'text': 'Click me',
        'emoji': True
    })))
    assert_that(output['value'], is_(equal_to('value')))
    assert_that(output['action_id'], is_(equal_to('my-button')))


def test_button_style():
    button = accessory.Button('Click me', 'my-button', 'value', style=ButtonStyle.PRIMARY)
    output = button.json()
    assert_that(output['style'], is_(equal_to('primary')))


def test_url_button():
    button = accessory.Button('Click me', 'my-button', 'value', url='example.com')
    output = button.json()
    assert_that(output['url'], is_(equal_to('example.com')))


def test_option():
    option = Option('item')
    block = option.json()
    assert_that(block, is_(equal_to({
        'text': {
            'type': 'plain_text',
            'text': 'item',
            'emoji': True
        },
        'value': 'item'
    })))


def test_checkbox():
    option = Option('item')
    checkbox = Checkbox('checkbox', [option])
    block = checkbox.json()
    assert_that(block, is_(equal_to({
        'type': 'checkboxes',
        'options': [
            option.json()
        ],
        'action_id': 'checkbox'
    })))


def test_overflow():
    option = Option('item')
    overflow = Overflow('overflow', [option])
    block = overflow.json()
    assert_that(block, is_(equal_to({
        'type': 'overflow',
        'options': [option.json()],
        'action_id': 'overflow'
    })))
