// https://leetcode.com/problems/two-sum
package main

import "fmt"

func twoSum(nums []int, target int) []int {

	return nil
}

func combination(nums []int, target int, elements []int, acc []int) []int {
	if len(acc) == 2 {
		if nums[acc[0]]+nums[acc[1]] == target {
			return acc
		} else {
			return nil
		}
	}

	for i := 0; i < len(elements); i++ {
		acc2 := append(acc, elements[i])
		candidate := combination(nums, target, elements[(i+1):], acc2)
		if candidate != nil {
			return candidate
		}
	}

	return nil
}

func makeRange(min, max int) []int {
	a := make([]int, max-min+1)
	for i := range a {
		a[i] = min + i
	}
	return a
}

func main() {
	nums := []int{3, 2, 4}
	target := 6
	elements := makeRange(0, len(nums)-1)
	acc := []int{}
	ints := combination(nums, target, elements, acc)
	fmt.Println(ints)
}
