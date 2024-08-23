from config import WALLETS, STR_DONE, STR_CANCEL
from setting import RANDOMIZER, CHECK_GWEI, TG_BOT_SEND, IS_SLEEP, DELAY_SLEEP, RETRY, WALLETS_IN_BATCH, TRACK

from modules.utils.helpers import list_send, wait_gas, send_msg, async_sleeping, is_private_key
from modules.utils.manager_async import Web3ManagerAsync
from modules import *

from loguru import logger
import random
import asyncio


async def main(module):
    func, module_name = get_module(module)

    if RANDOMIZER:
        random.shuffle(WALLETS)

    if module in [1, 2, 3, 13, 16]:
        await func().start()
    elif module == 17:
        await func()
    else:
        if module in [4, 5]:
            await process_exchanges(func, WALLETS)
        else:
            await process_batches(func, WALLETS, module)

