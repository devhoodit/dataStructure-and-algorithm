package main

import (
	ds "ds/ds"
	"fmt"
)

func main() {
	a := new(ds.Linkedlist)
	fmt.Print(a.Length)
	a.Push(1)
	a.Push(2)
	a.Push(3)

	fmt.Print(a.Index(0))
	fmt.Print(a.Index(1))
	fmt.Print(a.Index(2))
}
