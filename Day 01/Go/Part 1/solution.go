package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func sum(nums ...int) int {
	total := 0

	for i := range nums {
		total += nums[i]/3 - 2
	}

	return total
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var inputs []int

	for scanner.Scan() {
		num, err := strconv.Atoi(scanner.Text())
		if err != nil {
			panic(err)
		}
		inputs = append(inputs, num)
	}

	fmt.Println(sum(inputs...))
}
