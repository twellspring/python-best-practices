# Replace decorators with pytest mocker

Removing decorators makes unit tests easier to read. It also gets away from the decorator ordering issue where the order of the decorators before the function are inverse to the order of the variables for those decorators in the functions parameters.

## Before

```python
@patch.multiple("src.resources.Resources",local_resource=mock.DEFAULT,...
def test_create_resources_ignore(my, m_my_api, resources, mocker):
    m_my_api.return_value = API_RETURN_SUCCESS
    mocks["local_resource"].return_value = RESOURCE1
    resources.create = {"ignore": True}
```

## After

```python
def test_create_resources_ignore(my, m_my_api, resources, mocker):
    mocks = mocker.patch.multiple("src.resources.Resources", local_resource...
    m_my_api.return_value = API_RETURN_SUCCESS
    mocks["local_resource"].return_value = RESOURCE1
    resources.create = {"ignore": True}
```


