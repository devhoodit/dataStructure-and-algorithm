package main

import (
	ds "ds/linkedlist"
	"fmt"
)

func main() {
	a := new(ds.Linkedlist)
	fmt.Print(a.Length)
	a.Push(1)
	a.Push(2)
	a.Push(3)
	a.Pop(1)

	fmt.Print(a.Index(1))
}
