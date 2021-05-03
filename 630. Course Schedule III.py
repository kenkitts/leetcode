class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        def heap_insert(heap, duration):
            heappush(heap, duration * -1)

        def heap_get(heap):
            return heap[0] * -1

        def heap_pop(heap):
            return heappop(heap) * -1

        courses.sort(key=lambda x: x[1])
        heap = list()
        heapify(heap)
        total = 0
        for i in courses:
            if i[0] + total <= i[1]:
                total += i[0]
                heap_insert(heap, i[0])
            elif heap and heap_get(heap) > i[0]:
                total += i[0] - heap_pop(heap)
                heap_insert(heap, i[0])
        return len(heap)