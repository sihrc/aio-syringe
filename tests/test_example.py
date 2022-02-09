from aio_syringe import injected, injection, inject, Injection
from unittest.mock import AsyncMock


async def test_basic_usage():
    @injection
    async def delay_str():
        return "test"

    @injected
    async def mock(delay_str: str):
        return delay_str

    assert await mock() == "test"


async def test_nested_usage():
    @injection
    async def delay_one():
        return "first"

    @injection
    async def delay_two(delay_one: str):
        return delay_one + "second"

    @injected
    async def mock(delay_two: str):
        return delay_two

    assert await mock() == "firstsecond"


async def test_called_once():
    delay_mock = AsyncMock(return_value="test")

    injection(name="delay_one")(delay_mock)

    @injected
    async def mock(delay_one: str):
        return delay_one

    assert await mock() == "test"
    assert await mock() == "test"
    assert delay_mock.assert_awaited_once()


async def test_never_called():
    delay_mock = AsyncMock(return_value="test")

    injection(name="delay_one")(delay_mock)

    @injected
    async def mock(delay_one: str):
        return delay_one

    assert delay_mock.assert_not_awaited()


async def test_class_injection():
    @injected
    class Mock:
        async def mock(self, delay_one: str):
            return delay_one

    async def delay_one():
        return "first"

    mock = Mock(delay_one=delay_one())
    assert await mock.mock() == "first"


async def test_class_injection_methods_only():
    class Mock:
        @injected
        async def mock(self, delay_one: str):
            return delay_one

    async def delay_one():
        return "first"

    mock = inject(Mock(), delay_one=delay_one())
    assert await mock.mock() == "first"


async def test_inject_class_with_global():
    class Mock:
        @injected
        async def mock(self, delay_one: str):
            return delay_one

    @injection
    async def delay_one():
        return "first"

    assert await Mock().mock() == "first"
