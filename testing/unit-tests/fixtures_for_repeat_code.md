
# Use Fixtures to replace repeated code

When a series of tests have some of the same setup code, move that code into fixtures in conftest.py and pass in via the test function arguments.

## Before

```python
@patch.dict(os.environ, {"AUTH_TOKEN": AUTH_TOKEN})
@patch.multiple("src.resources.Resources",local_resource=mock.DEFAULT,...
@patch("src.my_api.api_call")
def test_create_resources(m_my_api, **mocks):
    m_my_api.return_value = API_RETURN_SUCCESS
    mocks["local_resource"].return_value = RESOURCE1
    resources = Resources(process_template('resource_config'))
    resources.create = {"ignore": True}
    class1 = MyClass()
...
````

## After

**conftest.py fixtures**
```python
@pytest.fixture
def api_auth(mocker):
    mocker.patch.dict(os.environ, {“AUTH_TOKEN”: AUTH_TOKEN})
    return DivvyApi()

@pytest.fixture
def api_call(mocker):
    m_patch = mocker.patch(“src.my_api.api_call”)
    return m_patch

@pytest.fixture
def resources(mocker):
    resources = Resources(process_template('resource_config'))
    return resources

```

**unit tests**
```python
@patch.multiple("src.resources.Resources",local_resource=mock.DEFAULT,...
def test_create_resources(api_auth, api_call, resources, mocker):
    api_call.return_value = API_RETURN_SUCCESS
    mocks["local_resource"].return_value = RESOURCE1
    resources.create = {"ignore": True}
...
```

