package main

import (
	"ds/stack"
	"fmt"
)

func main() {
	a := stack.New()
	a.Push(1)
	a.Push(2)
	a.Push(3)
	fmt.Print(a.Len())
	fmt.Print(a.Pop())
	fmt.Print(a.Pop())
	fmt.Print(a.Pop())
	fmt.Print(a.Len())
}
