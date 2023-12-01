import ListNode from './ListNode';

function linkedListToInteger(linkedList: ListNode): number {
  let digits: number[] = []

  while (linkedList) {
    digits.push(linkedList.val)  
    linkedList = linkedList.next
  }

  let integer: number = 0
  console.log(`digits: ${digits}`)


  for (let i = 0 ; i < digits.length ; i++) {
    console.log(`digit: ${digits[i]}`)
    console.log(`exponent: ${i}`)
    integer += digits[i] * Math.pow(10, i)
  }

  console.log(`integer: ${integer}`)

  return integer
}

function integerToLinkedList(integer: number): ListNode {
  console.log(`integerToLinkedList: ${integer}`)
  let numString: string = String(integer)

  let head: ListNode
  let pointer
  for (let i = numString.length - 1 ; i >= 0 ; i--) {
    console.log(`i :${i}`)
    if (i == numString.length - 1) {
      console.log("is first loop, initialize head")
      head = new ListNode(Number(numString[i]))
      pointer = head
    }
    
    let node: ListNode | null 
    if (i - 1 >= 0) {
      console.log(`the next node.val is ${numString[i - 1]}`)
      node = new ListNode(Number(numString[i - 1]))
    } else {
      node = null
    }
    pointer.next = node
    pointer = node
  }
  
  return head
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  console.log("addTwoNumbers")
  let num1 = linkedListToInteger(l1!)
  console.log(`num1: ${num1}`)
  let num2 = linkedListToInteger(l2!)
  console.log(`num2: ${num2}`)

  const sum = num1 + num2
  return integerToLinkedList(sum)
};

export default addTwoNumbers; // remove this on submission