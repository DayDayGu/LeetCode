func perm(nums []int, i int, r *[][]int) {
	if i == len(nums)-1 {
		copyNums := make([]int, len(nums))
		copy(copyNums, nums)
		*r = append(*r, copyNums)
		fmt.Println(nums)
	}

	for j := i; j < len(nums); j++ {
		nums[i], nums[j] = nums[j], nums[i]
		perm(nums, i+1, r)
		nums[j], nums[i] = nums[i], nums[j]
	}
}

func permute(nums []int) [][]int {
	var ret [][]int
	perm(nums, 0, &ret)
	return ret
}
