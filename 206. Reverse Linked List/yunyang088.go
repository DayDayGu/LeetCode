/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	var pre *ListNode
	for {
		if head == nil {
			break
		}
		var next = head.Next
		head.Next = pre
		pre = head
		head = next
	}
	return pre
}

func reverseListR(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	var tmp = reverseListR(head.Next)
	head.Next.Next = head
	head.Next = nil
	return tmp
}
