
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVI MINUS NUMBER PLUS TIMESexpression : expression term PLUSexpression : termterm : term factor TIMESexpression : expression factor MINUSterm : term factor DIVIterm : factorfactor : NUMBER'
    
_lr_action_items = {'DIVI':([2,5,],[-7,9,]),'NUMBER':([0,1,2,3,4,6,7,8,9,10,11,],[2,2,-7,-6,2,2,-6,-3,-5,-1,-4,]),'TIMES':([2,5,],[-7,8,]),'PLUS':([2,6,7,8,9,],[-7,10,-6,-3,-5,]),'MINUS':([2,7,],[-7,11,]),'$end':([1,2,3,4,8,9,10,11,],[-2,-7,-6,0,-3,-5,-1,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([0,4,],[1,6,]),'expression':([0,],[4,]),'factor':([0,1,4,6,],[3,5,7,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression term PLUS','expression',3,'p_expression_plus','parser_rules.py',5),
  ('expression -> term','expression',1,'p_expression_term','parser_rules.py',9),
  ('term -> term factor TIMES','term',3,'p_term_times','parser_rules.py',13),
  ('expression -> expression factor MINUS','expression',3,'p_term_minus','parser_rules.py',17),
  ('term -> term factor DIVI','term',3,'p_term_divi','parser_rules.py',21),
  ('term -> factor','term',1,'p_term_factor','parser_rules.py',25),
  ('factor -> NUMBER','factor',1,'p_factor_num','parser_rules.py',29),
]
