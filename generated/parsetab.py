
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '95478B3E8C4303B82D6907514FF7EFDD'
    
_lr_action_items = {'ITALIC':([1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-7,4,-17,4,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,4,-9,-13,-3,4,4,-4,]),'REFERENCE':([1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-7,11,-17,11,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,11,-9,-13,-3,11,11,-4,]),'UL1':([1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-7,7,-17,7,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,7,-9,-13,-3,7,7,-4,]),'TITLE2':([1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-7,8,-17,8,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,8,-9,-13,-3,8,8,-4,]),'OL3':([1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-7,9,-17,9,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,9,-9,-13,-3,9,9,-4,]),'UL2':([1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-7,10,-17,10,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,10,-9,-13,-3,10,10,-4,]),'PARAGRAPHE':([0,],[1,]),'$end':([2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,],[0,-17,-1,-6,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,-5,-9,-13,-3,-2,-4,]),'IMAGE':([1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-7,12,-17,12,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,12,-9,-13,-3,12,12,-4,]),'UL3':([1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-7,13,-17,13,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,13,-9,-13,-3,13,13,-4,]),'BOLD':([1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-7,17,-17,17,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,17,-9,-13,-3,17,17,-4,]),'OL1':([1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-7,15,-17,15,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,15,-9,-13,-3,15,15,-4,]),'FLUO':([1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-7,21,-17,21,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,21,-9,-13,-3,21,21,-4,]),'TITLE3':([1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-7,14,-17,14,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,14,-9,-13,-3,14,14,-4,]),'LINK':([1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-7,18,-17,18,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,18,-9,-13,-3,18,18,-4,]),'SEPARATION_LINE':([1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-7,22,-17,22,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,22,-9,-13,-3,22,22,-4,]),'WORD':([1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,25,],[-7,20,-17,20,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,20,-9,-13,20,]),'OL2':([1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-7,16,-17,16,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,16,-9,-13,-3,16,16,-4,]),'TITLE1':([1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[-7,19,-17,19,-14,-22,-20,-15,-11,-12,-16,-23,-18,-19,-8,-10,-21,19,-9,-13,-3,19,19,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentence':([3,6,20,25,],[5,23,24,26,]),'tag':([3,6,20,24,25,],[6,6,6,25,6,]),'document':([0,],[2,]),'paragraph':([0,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> document","S'",1,None,None,None),
  ('document -> paragraph sentence','document',2,'p_document','parser.py',10),
  ('sentence -> WORD sentence','sentence',2,'p_sentence','parser.py',15),
  ('sentence -> tag sentence','sentence',2,'p_sentence','parser.py',16),
  ('sentence -> WORD sentence tag sentence','sentence',4,'p_sentence','parser.py',17),
  ('sentence -> WORD','sentence',1,'p_sentence','parser.py',18),
  ('sentence -> tag','sentence',1,'p_sentence','parser.py',19),
  ('paragraph -> PARAGRAPHE','paragraph',1,'p_paragraph','parser.py',23),
  ('tag -> BOLD','tag',1,'p_tag','parser.py',27),
  ('tag -> FLUO','tag',1,'p_tag','parser.py',28),
  ('tag -> LINK','tag',1,'p_tag','parser.py',29),
  ('tag -> REFERENCE','tag',1,'p_tag','parser.py',30),
  ('tag -> IMAGE','tag',1,'p_tag','parser.py',31),
  ('tag -> SEPARATION_LINE','tag',1,'p_tag','parser.py',32),
  ('tag -> UL1','tag',1,'p_tag','parser.py',33),
  ('tag -> UL2','tag',1,'p_tag','parser.py',34),
  ('tag -> UL3','tag',1,'p_tag','parser.py',35),
  ('tag -> ITALIC','tag',1,'p_tag','parser.py',36),
  ('tag -> OL1','tag',1,'p_tag','parser.py',37),
  ('tag -> OL2','tag',1,'p_tag','parser.py',38),
  ('tag -> OL3','tag',1,'p_tag','parser.py',39),
  ('tag -> TITLE1','tag',1,'p_tag','parser.py',40),
  ('tag -> TITLE2','tag',1,'p_tag','parser.py',41),
  ('tag -> TITLE3','tag',1,'p_tag','parser.py',42),
]
