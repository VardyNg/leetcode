import ListNode from './ListNode';

function linkedListToInteger(linkedList: ListNode): number {
  let integer: number = 0 // the convered integer
  let i = 0 // counting how many node has travelled
  while (linkedList) { // terminate when linkedList.next = null i.e. the end of linked list
    // as the early node's val is corresponding to smaller digit in the integer
    // e.g. [8, 0, 7] -> 708
    // we can use the value of i as exponent to calculate the corresponding value in integer (e.g. 8 -> 8 x 10^0, 7 -> 7 x 10^2)
    integer += linkedList.val * Math.pow(10, i)
    i += 1
    linkedList = linkedList.next
  }
  return integer
}

function integerToLinkedList(integer: number): ListNode {
  // cast the integer to string, to help read the digits
  let numString: string = String(integer)

  // as we have to invert the outcome linked list
  // we set the head node val to the last digit
  let head: ListNode = new ListNode(Number(numString[numString.length - 1]))
  let pointer = head
  // we loop from the end to the start of the numString + 1 (avoid reaching the first digit of numString)
  // in each loop, we create a new node, set its value as the next digit, and point the pointer's next to that node (of course, move the pointer to the newly created node)
  for (let i = numString.length - 1 ; i > 0 ; i--) {
    console.log(`i :${i}`)
    
    let node: ListNode | null 
    console.log(`the next node.val is ${numString[i - 1]}`)
    node = new ListNode(Number(numString[i - 1]))
    pointer.next = node
    pointer = node
  }
  pointer.next = null // set the last node.next to null
  return head
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  return integerToLinkedList(
    linkedListToInteger(l1!) + linkedListToInteger(l2!)
  )
};

export default addTwoNumbers; // remove this on submission