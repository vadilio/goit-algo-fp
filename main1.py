# Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Додати елемент у кінець
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Вивід списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' → ')
            current = current.next
        print("None")

    # Реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування злиттям
    def merge_sort(self, head=None):
        if head is None:
            head = self.head
        if not head or not head.next:
            return head

        # Розбиття списку
        def split(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None
            return head, middle

        # Злиття двох відсортованих списків
        def merge(l1, l2):
            dummy = Node(0)
            tail = dummy
            while l1 and l2:
                if l1.data < l2.data:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 or l2
            return dummy.next

        left, right = split(head)
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        return merge(left, right)

    def sort(self):
        self.head = self.merge_sort()

# Об’єднання двох відсортованих списків


def merge_two_sorted_lists(head1, head2):
    dummy = Node(0)
    current = dummy
    while head1 and head2:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
    current.next = head1 or head2
    return dummy.next


# Створення та сортування
lst = SinglyLinkedList()
for val in [3, 1, 4, 2]:
    lst.append(val)

print("Оригінальний список:")
lst.print_list()

lst.sort()
print("Відсортований список:")
lst.print_list()

lst.reverse()
print("Реверсований список:")
lst.print_list()

# Об'єднання двох списків
list1 = SinglyLinkedList()
list2 = SinglyLinkedList()
for val in [1, 3, 5]:
    list1.append(val)
for val in [2, 4, 6]:
    list2.append(val)

merged_head = merge_two_sorted_lists(list1.head, list2.head)
merged_list = SinglyLinkedList()
merged_list.head = merged_head

print("Об’єднаний відсортований список:")
merged_list.print_list()
