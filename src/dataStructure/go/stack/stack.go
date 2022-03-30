package stack

import (
	"container/list"
)

type Stack struct {
	stk list.List
}

func New() *Stack {
	return &Stack{stk: *list.New()}
}

func (s *Stack) Push(data interface{}) {
	s.stk.PushBack(data)
}

func (s *Stack) Pop() interface{} {
	tmp := s.stk.Back()
	s.stk.Remove(tmp)
	return tmp
}
