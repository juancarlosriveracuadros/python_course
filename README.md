# python_course

## class
https://www.youtube.com/watch?v=mrhccLHtyN4&t=318s
- **properte**
- **Methods**
python --> dir(<class>) > show methods

In Python, a class can be **internal** or **external** depending on where and how it is defined and used. Here's the distinction:  

### **1. Internal Class (Nested Class)**
- A **nested class** (internal class) is a class defined **inside** another class.
- It is typically used when the class is **logically dependent** on the outer class.
- The inner class cannot be accessed directly from outside unless referenced through the outer class.

#### **Example: Internal (Nested) Class**
```python
class Outer:
    class Inner:
        def display(self):
            print("I am an inner class method.")

# Accessing the inner class
outer_instance = Outer()
inner_instance = outer_instance.Inner()
inner_instance.display()
```

### **2. External Class**
- An **external class** is a regular class defined **outside** of other classes.
- It is independent and can be imported and used in different modules.

#### **Example: External Class**
```python
class External:
    def display(self):
        print("I am an external class method.")

# Creating an instance
ext_instance = External()
ext_instance.display()
```


- **Class Methods, Static Methods, & Instance Methods**
https://www.youtube.com/watch?v=PIKiHq1O9HQ



### operators
you can use operators in your own classes: 
https://docs.python.org/3/library/operator.html


### scope
Scope in Python refers to the **region of code** where a variable or name is **accessible**. It determines where a variable can be **read or modified** and where it **ceases to exist**.

#### **Types of Scope in Python**
Python follows the **LEGB rule**, which stands for:
1. **Local Scope** - Inside a function.
2. **Enclosing Scope** - Nested function scope.
3. **Global Scope** - Defined at the top level of a script or module.
4. **Built-in Scope** - Predefined names in Python.
\
https://www.youtube.com/watch?v=QVdf0LgmICw

## Algorithms and Data Structures

- data types:
https://www.w3schools.com/python/python_datatypes.asp

- intro Algorithms:
https://www.youtube.com/watch?v=_t2GVaQasRY&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=2

- Big O notation:
https://www.youtube.com/watch?v=IR_S8BC8KI0&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=3

**Table with comparation**
https://www.bigocheatsheet.com/

### Arrya:
https://www.youtube.com/watch?v=gDqQf4Ekr2A&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=3&t=0s

for index » Big o = 0(1) or konstant time
for value » Big o = 0(n) or linear time (FOR LOOP)
print all value / delete or update a value  » Big o = 0(n) or linear time (FOR LOOP)

**Summary: When to Use Each as a Data Engineer**
| Use Case | `list` | `tuple` | `range` |
|----------|--------|---------|---------|
| **Mutable & Dynamic Data** | ✅ Yes | ❌ No | ❌ No |
| **Immutable & Read-Only Data** | ❌ No | ✅ Yes | ✅ Yes |
| **Heterogeneous Data** | ✅ Yes | ✅ Yes | ❌ No |
| **Large Number Sequences (Efficient Memory Use)** | ❌ No | ❌ No | ✅ Yes |
| **Database Records / Schema-Based Data** | ✅ Yes | ✅ Yes | ❌ No |
| **Efficient Iteration & Batch Processing** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Faster Performance (Immutability Advantage)** | ❌ No | ✅ Yes | ✅ Yes |
| **Hashable (Can be a Dictionary Key)** | ❌ No | ✅ Yes | ❌ No |

**TL;DR:**
- **Use `list`** when modifying data (reading CSVs, appending records, filtering).
- **Use `tuple`** when storing fixed, immutable data (database records, dictionary keys).
- **Use `range`** when iterating large datasets or generating sequences efficiently.

### Linked List:
https://www.youtube.com/watch?v=qp8u-frRAnU&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=5

### Hash Table: 
https://www.youtube.com/watch?v=ea8BRGxGmlA&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=5


**1. Dictionary (`dict`) - When to Use as a Hash Table**
✅ **Use when:**
- You need **fast lookups** (`O(1)` average time complexity).
- You have **key-value pairs** (e.g., mapping user IDs to names).
- You need **mutability** (modifying, adding, or removing elements).
- The keys are **unique and hashable** (strings, numbers, tuples).

❌ **Avoid if:**
- Order of elements matters (use `OrderedDict` or `list` if needed).
- You need a **small memory footprint** (dicts use more memory due to hashing overhead).

💡 **Example:**
```python
user_data = {"user_1": "Alice", "user_2": "Bob"}
print(user_data["user_1"])  # O(1) lookup
```
🔥 **Best for:** Caching, indexing, lookups, configuration settings.


**2. List (`list`) - When to Use as an Array**
✅ **Use when:**
- You need an **ordered sequence** of items.
- You frequently **append or iterate** over data.
- You perform **index-based access** (`O(1)` lookup).
- The elements are **homogeneous** (e.g., a list of integers).

❌ **Avoid if:**
- You need **fast membership tests** (`in` is `O(n)`, unlike `dict` which is `O(1)`).
- You frequently **insert or delete** elements in the middle (`O(n) cost`).

💡 **Example:**
```python
data = [1, 2, 3, 4]
print(data[2])  # O(1) access
```
🔥 **Best for:** Storing large data collections, processing in batches, maintaining ordered datasets.

---

**3. Tuple (`tuple`) - When to Use Over a List**
✅ **Use when:**
- You need an **immutable sequence** (cannot be changed).
- Performance is critical (tuples are **faster and use less memory** than lists).
- The data should act as a **fixed record** (e.g., database rows).
- Tuples are **hashable** (can be used as dictionary keys or in sets).

❌ **Avoid if:**
- You need to modify the data frequently (use a list instead).
- You require a **dynamic size** (tuples are fixed in length).

💡 **Example:**
```python
coordinates = (10.5, 42.7)
print(coordinates[0])  # O(1) access
```
🔥 **Best for:** Read-only data, function return values, database records.

**When to Choose Each as a Data Engineer?**
| Use Case | Dictionary (`dict`) | List (`list`) | Tuple (`tuple`) |
|----------|----------------|-------------|-------------|
| **Fast Lookups (O(1))** | ✅ Best | ❌ Slow (`O(n)`) | ❌ Slow (`O(n)`) |
| **Preserving Order** | ✅ (Python 3.7+) | ✅ | ✅ |
| **Memory Efficiency** | ❌ Higher | ✅ Lower | ✅ Best |
| **Mutability** | ✅ Yes | ✅ Yes | ❌ No |
| **Dynamic Updates** | ✅ Best | ✅ Good | ❌ No |
| **Iteration Over Data** | ❌ (`.keys()/.values()`) | ✅ Best | ✅ Good |
| **Hashable (Can be Dictionary Key)** | ❌ No | ❌ No | ✅ Yes |
| **Best Used For** | Lookups, Indexing | Storing Sequences | Fixed Data, Function Returns |


**Real-World Scenarios in Data Engineering**
1️⃣ **Processing Rows from a Database**
   - Use **tuples** (`tuple`) to store **immutable row data**.
   - Use **lists** (`list`) to hold multiple rows.

2️⃣ **Building an In-Memory Cache for Fast Lookups**
   - Use **dictionaries** (`dict`) with keys for fast lookups.

3️⃣ **Streaming Data Processing**
   - Use **lists** (`list`) for storing **temporary batches** before processing.

4️⃣ **Configuration Settings**
   - Use a **dictionary** (`dict`) to store **configurations**.


**Conclusion**
- **Use a dictionary (`dict`)** for **fast lookups, mapping key-value pairs**.
- **Use a list (`list`)** for **ordered, mutable collections**.
- **Use a tuple (`tuple`)** when **immutability and performance** matter.


### Collections 

#### Stack
https://www.youtube.com/watch?v=zwb3GmNAtFk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=7

#### Queue
https://www.youtube.com/watch?v=rUUrmGKYwHw&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=8

#### Collections
for represeting the data structure Stack and Queue it will be better to use the collections module with "deque"

https://docs.python.org/3/library/collections.html

https://www.youtube.com/watch?v=m3JgSV1Obn8
