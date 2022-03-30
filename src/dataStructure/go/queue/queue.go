package Queue

import (
	"container/list"
)

type Queue struct {
	que *list.List
}

func New() *Queue {
	return &Queue{que: list.New()}
}

func (s *Queue) Push(data any) {
	s.que.PushBack(data)
}

func (s *Queue) Pop() any {
	if s.is_empty() {
		panic("Queue underflow, Queue is empty")
	}
	tmp := s.que.Front()
	s.que.Remove(tmp)
	return tmp.Value
}

func (s Queue) is_empty() bool {
	return s.que.Len() == 0
}

func (s Queue) Len() int {
	return s.que.Len()
}
