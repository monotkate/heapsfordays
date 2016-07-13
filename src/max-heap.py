import math

""" buildHeap runs maxHeapify on each node in the tree except leaves to create
a max-heap from an array.  Assumes full array is heap. """
def buildHeap(heap):
  # Lowest node that is not a leaf
  node = int(math.floor(len(heap)/2))
  # Increment through nodes and find correct location
  for i in range(node, -1, -1):
    maxHeapify(heap, i, len(heap))

""" maxHeapify moves the given index value to the correct location in the
heap """
def maxHeapify(heap, i, size):
  l = left(i)       # index value of left child
  r = right(i)      # index value of right child

  if size <= 1:
    return

  # if l is in range and larger than current, set as largest
  if l <= size and heap[l] > heap[i]:
    largest = l
  else:
    largest = i

  # if r is in range and larger than largest, set as largest
  if r < size and heap[r] > heap[largest]:
    largest = r

  # if current is not the largest, swap with the largest
  if largest != i:
    swap(heap, i, largest)
    maxHeapify(heap, largest, size) # recursively run again until current is correct

""" swap swaps the values in the array for two given numbers"""
def swap(heap, a, b):
  temp = heap[a]
  heap[a] = heap[b]
  heap[b] = temp

""" returns the location of the left child """
def left(i):
  return 2 * i + 1

""" returns the location of the right child """
def right(i):
  return 2 * i + 2

""" returns the location of the parent """
def parent(i):
  return int(math.floor(i/2))

""" sorts a heap in incrementing order """
def heapsort(heap):
  buildHeap(heap)   # Form heap from array
  size = len(heap)
  # Move the highest number to the last location.  Reconfigure remaining heap
  for i in range(len(heap)-1, 0, -1):
    swap(heap, 0, i)
    size -= 1
    maxHeapify(heap, 0, size)

""" heapMax returns the value of the largest key in the heap """
def heapMax(heap):
  return heap[0]

""" heapGetMax returns the element with the largest key and removes it from
the heap """
def heapGetMax(heap):
  if len(heap) < 1:
    return "heap underflow"
  max = heap[0]
  heap[0] = heap[len(heap)-1]
  del heap[len(heap)-1]
  maxHeapify(heap, 0, len(heap))
  return max

""" heapIncKey replaces the current value of the given key with the new value
as long as the new value is larger than the current value """
def heapIncKey(heap, i, k):
  if k < heap[i]:
    return "new key is too small"
  heap[i] = k
  while i > 0 and heap[parent(i)] < heap[i]:
    swap(heap, i, parent(i))
    i = parent(i)

""" maxHeapInsert inserts a new key into a current heap in the correct
position"""
def maxHeapInsert(heap, key):
  heap.append(float("-inf"))
  heapIncKey(heap, len(heap)-1, key)

""" main function"""
def main():

  print "build a new heap from current array:"
  heap = [1, 2, 3, 4, 5, 6, 7, 8]
  print heap
  buildHeap(heap)
  print heap
  print

  print "rearrange a single key to the correct place in a heap:"
  heap = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
  print heap
  maxHeapify(heap, 1, len(heap))
  print heap
  print

  heap = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
  print "Heap sorting function"
  print heap
  heapsort(heap)
  print heap
  print

  print "return and remove the largest value in the heap:"
  heap = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
  buildHeap(heap)
  print heap
  max = heapGetMax(heap)
  print heap
  print max
  print

  print "change the value of a key to a higher priority:"
  heap = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
  buildHeap(heap)
  print heap
  heapIncKey(heap, 3, 17)
  print heap
  print "Changed key for 8 to 17"
  print

  print "max heap insert new key:"
  heap = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
  buildHeap(heap)
  print heap
  maxHeapInsert(heap, 15)
  print heap
  print


if __name__ == "__main__":
  main()
