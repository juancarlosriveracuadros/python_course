# python_course

prapere python kwouledge for interview

- data types:
https://www.w3schools.com/python/python_datatypes.asp

- intro Algorithms:
https://www.youtube.com/watch?v=_t2GVaQasRY&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=2

- BIg o notation:
https://www.youtube.com/watch?v=IR_S8BC8KI0&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=3

- Arrya:
https://www.youtube.com/watch?v=gDqQf4Ekr2A&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=3&t=0s

for index » Big o = 0(1) or konstant time
for value » Big o = 0(n) or linear time (FOR LOOP)
print all value / delete or update a value  » Big o = 0(n) or linear time (FOR LOOP)

## **Summary: When to Use Each as a Data Engineer**
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

### **TL;DR:**
- **Use `list`** when modifying data (reading CSVs, appending records, filtering).
- **Use `tuple`** when storing fixed, immutable data (database records, dictionary keys).
- **Use `range`** when iterating large datasets or generating sequences efficiently.
