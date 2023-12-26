import asyncio

from ThamesThrive.process_engine.tql.transformer.filter_transformer import FilterTransformer
from ThamesThrive.service.singleton import Singleton
from ThamesThrive.service.notation.dot_accessor import DotAccessor
from ThamesThrive.process_engine.tql.parser import Parser


class FilterCondition(metaclass=Singleton):

    def __init__(self):
        self.parser = Parser(Parser.read('grammar/filter_condition.lark'), start='expr')

    def parse(self, condition):
        return self.parser.parse(condition)

    async def evaluate(self, condition, dot: DotAccessor = None):
        # todo cache tree
        tree = self.parse(condition)
        await asyncio.sleep(0)
        if dot:
            return FilterTransformer(dot=dot).transform(tree)
        return FilterTransformer().transform(tree)
