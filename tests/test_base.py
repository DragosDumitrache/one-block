from hamcrest import assert_that, equal_to, is_

from one_block.base import BaseText


def test_base_plain_text():
    block = BaseText('Hello, World!')
    output = block.json()
    assert_that(output, is_(equal_to({
        'type': 'plain_text',
        'text': 'Hello, World!',
        'emoji': True
    })))


def test_markdown():
    block = BaseText('Hello, World!', markdown=True)
    output = block.json()
    assert_that(output, is_(equal_to({
        'type': 'mrkdwn',
        'text': 'Hello, World!',
    })))
