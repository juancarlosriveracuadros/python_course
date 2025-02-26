# Basic Testing Types:

### 1. **Unit Testing**
- **Description**: Unit tests focus on individual components or functions of the code. They ensure that each part works as expected in isolation.
- **Tools**: `unittest`, `pytest`
- **Example**: Testing a function that transforms data to ensure it handles various input cases correctly.

### 2. **Integration Testing**
- **Description**: Integration tests verify that different components of the system work together as intended. This includes testing interactions between modules, services, and databases.
- **Tools**: `pytest`, `Great Expectations`
- **Example**: Testing a data pipeline that ingests data from an API, processes it, and stores it in a database.

### 3. **End-to-End (E2E) Testing**
- **Description**: E2E tests simulate real-world scenarios to ensure the entire data pipeline works from start to finish. They cover the complete workflow, from data ingestion to final output.
- **Tools**: Custom scripts, `pytest`
- **Example**: Testing the entire process of data extraction, transformation, and loading (ETL) to ensure data integrity and correctness.

### 4. **Performance Testing**
- **Description**: Performance tests evaluate how the system performs under various conditions, such as high load or large datasets. They help identify bottlenecks and optimize performance.
- **Tools**: `locust`, `JMeter`
- **Example**: Testing how quickly a data pipeline can process a large volume of data and identifying any performance issues.

### 5. **Data Quality Testing**
- **Description**: Data quality tests ensure that the data meets predefined quality standards. This includes checks for data accuracy, consistency, completeness, and validity.
- **Tools**: `Great Expectations`, custom scripts
- **Example**: Testing that all required fields are present and correctly formatted in the ingested data.

### 6. **Regression Testing**
- **Description**: Regression tests ensure that new changes or updates to the codebase do not introduce new bugs or break existing functionality.
- **Tools**: `pytest`, `unittest`
- **Example**: Running a suite of tests after a code update to ensure that all existing features still work as expected.

### 7. **Error Handling and Logging Testing**
- **Description**: These tests verify that the system correctly handles errors and logs important information for debugging and monitoring purposes.
- **Tools**: `unittest`, `pytest`
- **Example**: Testing that the system logs appropriate error messages when it encounters invalid data.

### 8. **Security Testing**
- **Description**: Security tests ensure that the data pipeline is secure and protected against vulnerabilities, such as unauthorized access or data breaches.
- **Tools**: Security testing tools, custom scripts
- **Example**: Testing that sensitive data is encrypted and that access controls are properly implemented.


In the context of testing, "mocking" refers to the practice of creating mock objects to simulate the behavior of real objects in a controlled way. This is particularly useful in unit testing to isolate the code under test and ensure that tests are not dependent on external systems or resources. Here are some key points about mocking:

# Mocking

- **Definition**: Mocking involves creating objects that mimic the behavior of real objects. These mock objects can be programmed to return specific values or simulate certain behaviors.
- **Purpose**: The main goal is to isolate the code being tested, allowing you to focus on its functionality without interference from external dependencies.

### **Why Use Mocking?**
- **Isolation**: By using mocks, you can test a unit of code in isolation, ensuring that any failures are due to issues within the code itself, not external factors.
- **Control**: Mocks allow you to control the behavior of dependencies, making it easier to test edge cases and error conditions.
- **Speed**: Tests that use mocks are generally faster because they do not involve actual network calls, database queries, or other time-consuming operations.

### **Common Mocking Libraries in Python**
- **`unittest.mock`**: Part of the standard library, this module provides tools for creating and using mock objects.
- **`pytest-mock`**: An extension for `pytest` that simplifies the use of `unittest.mock` with `pytest`.

### **Examples of Mocking**
1. **Mocking a Database Call**:
   ```python
   from unittest.mock import MagicMock

   def get_user_data(user_id):
       # Imagine this function makes a database call
       pass

   # Create a mock object
   mock_db_call = MagicMock(return_value={'id': 1, 'name': 'John Doe'})

   # Use the mock object in place of the real database call
   get_user_data = mock_db_call

   # Test the function
   assert get_user_data(1) == {'id': 1, 'name': 'John Doe'}
   ```

2. **Mocking an API Request**:
   ```python
   import requests
   from unittest.mock import patch

   def fetch_data(url):
       response = requests.get(url)
       return response.json()

   # Use patch to mock requests.get
   with patch('requests.get') as mock_get:
       mock_get.return_value.json.return_value = {'key': 'value'}
       data = fetch_data('http://example.com')
       assert data == {'key': 'value'}
   ```

### **Best Practices for Mocking**
- **Mock Only What You Need**: Avoid over-mocking, which can make tests harder to understand and maintain.
- **Verify Interactions**: Ensure that your mocks are used as expected by verifying interactions, such as method calls and arguments.
- **Keep Tests Readable**: Write clear and concise tests that are easy to understand, even with the use of mocks.

# pytest tutorial

https://www.youtube.com/watch?v=cHYq1MRoyI0&t=2750s


- basic function test »  source/my_func.py tests/test_my_func.py
- class test » source/shapes.py tests/test_circle.py
