from .core import taichi_lang_core

class SNode:
  def __init__(self, ptr):
    self.ptr = ptr

  def dense(self, indices, dimensions):
    if isinstance(dimensions, int):
      dimensions = [dimensions] * len(indices)
    return SNode(self.ptr.dense(indices, dimensions))

  def pointer(self):
    return SNode(self.ptr.pointer())

  def place(self, *args):
    from .expr import Expr
    for arg in args:
      if isinstance(arg, Expr):
        self.ptr.place(Expr(arg).ptr)
      else:
        arg.place(self)
    return self
