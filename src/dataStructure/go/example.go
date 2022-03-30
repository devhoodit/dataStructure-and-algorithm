package main

import (
	Queue "ds/queue"
	"fmt"
)

func main() {
	a := Queue.New()
	a.Push(1)
	a.Push(2)
	a.Push(3)
	fmt.Print(a.Len())
	fmt.Print(a.Pop())
	fmt.Print(a.Pop())
	fmt.Print(a.Pop())
	fmt.Print(a.Len())
}
