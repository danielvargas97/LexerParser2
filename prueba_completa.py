import lexer_rules
import parser_rules

from ply.lex import lex
from ply.yacc import yacc

text = "15 5 / 12 + 27 12 1 + - *"
lexer = lex(module=lexer_rules)
parser = yacc(module=parser_rules)

expression = parser.parse(text, lexer)
print expression
"""
result = expression.evaluate()
print result
"""
