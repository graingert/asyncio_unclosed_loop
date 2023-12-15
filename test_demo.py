import pytest

import pytest_asyncio


@pytest_asyncio.fixture()
async def demo():
    yield


@pytest.mark.asyncio
async def test_aiohttp_test_client_json(demo):
    pass


def test_redirect():

    import asyncio
    async def amain():
        pass
    asyncio.run(amain())

    import gc
    gc.collect()
