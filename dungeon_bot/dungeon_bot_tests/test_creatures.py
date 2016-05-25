# import random
# import statistics
# from ..abilities import abilities
import logging
# from util import diceroll, clamp
from ..enemies import *

logger = logging.getLogger("dungeon_bot_test_log")
logger.debug("Test creatures loaded")

def test_get_enemies_for_difficulty():
	enemies = retrieve_enemies_for_difficulty("animal", 1, False)
	logger.info("Enemies for diff 1:%s"%(str(enemies)))

	enemies = retrieve_enemies_for_difficulty("animal", 10, False)
	logger.info("Enemies for diff 10:%s"%(str(enemies)))

	enemies = retrieve_enemies_for_difficulty("animal", 20, False)
	logger.info("Enemies for diff 20:%s"%(str(enemies)))

	enemies = retrieve_enemies_for_difficulty("animal", 40, True)
	logger.info("Enemies for diff 40:%s"%(str(enemies)))

def run_tests():
	logger.info("Testing getting random enemies.\n")
	test_get_enemies_for_difficulty()
