package stack

import (
	"container/list"
)

type Stack struct {
	stk *list.List
}

func New() *Stack {
	return &Stack{stk: list.New()}
}

func (s *Stack) Push(data interface{}) {
	s.stk.PushBack(data)
}

func (s *Stack) Pop() interface{} {
	if s.is_empty() {
		panic("Stack underflow, stack is empty")
	}
	tmp := s.stk.Back()
	s.stk.Remove(tmp)
	return tmp.Value
}

func (s Stack) is_empty() bool {
	return s.stk.Len() == 0
}

func (s Stack) Len() int {
	return s.stk.Len()
}
