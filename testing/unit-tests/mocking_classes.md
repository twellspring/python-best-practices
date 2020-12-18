# Mocking Classes


## Mock class instantiation and class method
Mocker returns a callable method using a lambda anonymous function

```python

def test_my_function(mocker):
    mocker.patch.object(MyClass, "__init__", lambda x: None)
    mocker.patch('path.MyClass.class_function', return_value={"Return": "Value"})

```

## Mock an entire claass
```python

def test_my_function(mocker):

    class TestMyClass(object):
        def class_function(self):
            return True
    
    m_myclass = mocker.patch(path.MyClass)
    m_myclass.return_value = TestMyClass()
```

## Mock multiple methods in the same class
```python

def test_my_function(mocker):
    mocks = mocker.patch.multiple('path.MyClass', 
            function1=mocker.DEFAULT, 
            function2=mocker.DEFAULT,
            function3=mocker.DEFAULT)

    mocks["function1"].return_value="some string"
    mocks["function1"].assert_called_once_with(parameter1=123, parameter2="abc")

## Multiple calls for same method

    mocks["function2"].assert_has_calls(
        [call(parameter1=123, parameter2="abc"), call(parameter1=999, parameter2="zzz")]
    )

## Multiple responses for same method
    m_myclass.side_effect = ( "response1", "response2")