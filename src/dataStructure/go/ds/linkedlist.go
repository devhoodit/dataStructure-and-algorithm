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
	for i := 0; i < n; i++ {
		cursor = cursor.next
	}
	return cursor.data
}

func (list *Linkedlist) Push(data interface{}) {
	cursor := &list.first
	for i := 0; i < list.Length; i++ {
		cursor = cursor.next
	}
	cursor.data = data
	cursor.next = &node{}
	list.Length += 1
}
