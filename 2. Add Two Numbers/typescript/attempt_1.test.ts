import addTwoNumbers from './attempt_1';
import ListNode from './ListNode';

describe("test addTwoNumbers", () => {
  test("Test 1", async () => {
    // Arrange
    let node1 = new ListNode(2)
    let node2 = new ListNode(4)
    let node3 = new ListNode(3)
    node1.next = node2
    node2.next = node3
    
    let nodeI = new ListNode(5)
    let nodeII = new ListNode(6)
    let nodeIII = new ListNode(4)
    nodeI.next = nodeII
    nodeII.next = nodeIII

    let expectedNode1 = new ListNode(7)
    let expectedNode2 = new ListNode(0)
    let expectedNode3 = new ListNode(8)
    expectedNode1.next = expectedNode2
    expectedNode2.next = expectedNode3

    // Act
    let res = addTwoNumbers(node1, nodeI)

    // Assert
    expect(res.val).toBe(expectedNode1.val)
    expect(res.next.val).toBe(expectedNode2.val)
    expect(res.next.next.val).toBe(expectedNode3.val)
  })

  test("Test 2", async () => {
    // Arrange
    let node1 = new ListNode(0)
    
    let nodeI = new ListNode(0)

    let expectedNode1 = new ListNode(0)

    // Act
    let res = addTwoNumbers(node1, nodeI)

    // Assert
    expect(res.val).toBe(expectedNode1.val)
  })

  // Stay simple!
  test("Test 3", async () => {
    // Arrange
    let node1 = new ListNode(9)
    let node2 = new ListNode(9)
    let node3 = new ListNode(9)
    let node4 = new ListNode(9)
    let node5 = new ListNode(9)
    let node6 = new ListNode(9)
    let node7 = new ListNode(9)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    let nodeI = new ListNode(9)
    let nodeII = new ListNode(9)
    let nodeIII = new ListNode(9)
    let nodeIV = new ListNode(9)
    nodeI.next = nodeII
    nodeII.next = nodeIII
    nodeIII.next = nodeIV

    let expectedNode1 = new ListNode(8)
    let expectedNode2 = new ListNode(9)
    let expectedNode3 = new ListNode(9)
    let expectedNode4 = new ListNode(9)
    let expectedNode5 = new ListNode(0)
    let expectedNode6 = new ListNode(0)
    let expectedNode7 = new ListNode(0)
    let expectedNode8 = new ListNode(1)
    expectedNode1.next = expectedNode2
    expectedNode2.next = expectedNode3
    expectedNode3.next = expectedNode4
    expectedNode4.next = expectedNode5
    expectedNode5.next = expectedNode6
    expectedNode6.next = expectedNode7
    expectedNode7.next = expectedNode8

    // Act
    let res = addTwoNumbers(node1, nodeI)

    // Assert
    expect(res.val).toBe(expectedNode1.val)
    expect(res.next.val).toBe(expectedNode2.val)
    expect(res.next.next.val).toBe(expectedNode3.val)
    expect(res.next.next.next.val).toBe(expectedNode4.val)
    expect(res.next.next.next.next.val).toBe(expectedNode5.val)
    expect(res.next.next.next.next.next.val).toBe(expectedNode6.val)
    expect(res.next.next.next.next.next.next.val).toBe(expectedNode7.val)
    expect(res.next.next.next.next.next.next.next.val).toBe(expectedNode8.val)
  })
})