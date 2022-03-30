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

func (s *Stack) Push(data any) {
	s.stk.PushBack(data)
}

func (s *Stack) Pop() any {
	if s.is_empty() {
		panic("Stack underflow, stack is empty")
	}
	tmp := s.stk.Front()
	s.stk.Remove(tmp)
	return tmp.Value
}

func (s Stack) is_empty() bool {
	return s.stk.Len() == 0
}

func (s Stack) Len() int {
	return s.stk.Len()
}
