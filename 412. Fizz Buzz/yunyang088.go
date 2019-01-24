func fizzBuzz(n int) []string {
	var a []string
	for i := 1; i <= n; i++ {
		if i%15 == 0 {
			a = append(a, "FizzBuzz")
		} else if i%3 == 0 {
			a = append(a, "Fizz")
		} else if i%5 == 0 {
			a = append(a, "Buzz")
		} else {
			a = append(a, fmt.Sprintf("%v", i))
		}
	}
	return a
}
