package amoCRM

import (
	"fmt"
)

func main() {
	fn()
}

func fn() {
	print1("Hello, world")
	print1(12345)
	print1(3.14159)
	print1(true)
}

func print1(a interface{}) {
	switch v := a.(type) {
	case string:
		fmt.Printf("Is string: %s\n", v)
	case interface{}:
		fmt.Printf("Is Interface{}: %v\n", v)
	case int:
		fmt.Printf("Is int: %d\n", v)
	case float64:
		fmt.Printf("Is float64: %f\n", v)
	default:
		fmt.Printf("Is unknown : %v\n", v)
	}
}