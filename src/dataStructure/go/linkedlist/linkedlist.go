// This is Linked list used in go
// https://cs.opensource.google/go/go/+/refs/tags/go1.18:src/container/list/list.go

package ds

type Linkedlist struct {
	Length int
	first  node
}

type node struct {
	data interface{}
	next *node
}

func (list *Linkedlist) Index(n int) interface{} {
	if n > list.Length {
		panic("Index out of range")
	}
	cursor := &list.first
	for i := 0; i < n+1; i++ {
		cursor = cursor.next
	}
	return cursor.data
}

func (list *Linkedlist) Push(data interface{}) {
	cursor := &list.first
	for i := 0; i < list.Length; i++ {
		cursor = cursor.next
	}
	cursor.next = &node{data: data, next: nil}
	list.Length += 1
}

func (list *Linkedlist) Del(n int) {
	if n > list.Length {
		panic("Index out of range")
	}
	cursor := &list.first
	for i := 0; i < n; i++ {
		cursor = cursor.next
	}
	tmp := &cursor.next
	cursor = cursor.next
	*tmp = cursor.next
	list.Length -= 1
}

func (list *Linkedlist) Pop(n int) interface{} {
	if n > list.Length {
		panic("Index out of range")
	}
	cursor := &list.first
	for i := 0; i < n; i++ {
		cursor = cursor.next
	}
	tmp := &cursor.next
	cursor = cursor.next
	data := cursor.data
	*tmp = cursor.next
	list.Length -= 1
	return data
}
