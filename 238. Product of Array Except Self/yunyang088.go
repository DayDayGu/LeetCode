func productExceptSelf(nums []int) []int {
	var output = make([]int, len(nums))
	var tmp = 1
	for i := 0; i < len(nums); i++ {
		output[i] = tmp
		tmp *= nums[i]
	}
	tmp = 1
	for i := len(nums) - 1; i >= 0; i-- {
		output[i] *= tmp
		tmp *= nums[i]
	}
	return output
}
