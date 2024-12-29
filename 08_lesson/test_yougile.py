import requests
from Yougile import Yougile

base_url = Yougile("https://ru.yougile.com/api-v2")
key = "g5ci5PegiSCIFP8LgP1bIjEKhyS8gP0QzIV0ex8RH0U+bkhFHJbQSsTcJVlPImNH"
# def test_create_key():
#     my_authorization = "Bearer NlzQ55ry-5iWlqWtHsedlREWu2vvdlIapBKmNO-nX+EnurlfIJ6YEoQNy85xFZYN"
#     my_content_type = "application/json"
#     my_login = "shamsudinov2911@gmail.com"
#     my_password = "1!xFrostx!1"
#     company_id = "d0b3ce73-ee47-4b29-b752-c976efd4f11c"
#
#     resp = base_url.create_key(my_authorization, my_content_type, my_login, my_password, company_id)
#     assert len(resp) > 0
#     assert 'key' in resp
#
# def test_create_key_negative():
#     my_login = "shamsudinov2911@gmail.com"
#     my_password = "1!xFrostx!1"
#     company_id = "d0b3ce73-ee47-4b29-b752-c976efd4f11c"
#
#     resp = base_url.create_key(my_login, my_password, company_id)
#     assert len(resp) > 0

def test_create_project():
    my_authorization = "Bearer NlzQ55ry-5iWlqWtHsedlREWu2vvdlIapBKmNO-nX+EnurlfIJ6YEoQNy85xFZYN"
    my_content_type = "application/json"
    my_title = "Football"

    # Получаем список проектов до создания нового
    all_company_list = base_url.get_project_list(my_authorization, my_content_type)
    len_before = len(all_company_list)

    # Создаем новый проект
    resp = base_url.create_project(my_authorization, my_content_type, my_title)
    assert resp.status_code
    assert 'id' in resp.json()

    # Получаем список проектов после создания нового проекта
    result = base_url.get_project_list(my_authorization, my_content_type)
    len_after = len(result)
    assert len_after - len_before == 1
    assert len(resp) > 0

def test_create_project_negative():
    my_authorization = "Bearer NlzQ55ry-5iWlqWtHsedlREWu2vvdlIapBKmNO-nX+EnurlfIJ6YEoQNy85xFZYN"
    my_content_type = "application/json"
    my_title = ""

    # Получаем список проектов до создания нового
    all_company_list = base_url.get_project_list(my_authorization, my_content_type)
    len_before = len(all_company_list)

    # Создаем новый проект
    resp = base_url.create_project(my_authorization, my_content_type, my_title)
    assert 'id' in resp.json()

    # Получаем список проектов после создания нового проекта
    result = base_url.get_project_list(my_authorization, my_content_type)
    len_after = len(result)

    assert len_after - len_before == 1
    assert len(resp) > 0

def test_get_project_list():
    my_authorization = "Bearer NlzQ55ry-5iWlqWtHsedlREWu2vvdlIapBKmNO-nX+EnurlfIJ6YEoQNy85xFZYN"
    my_content_type = "application/json"
    my_title = "Football"

    # Создаем новый проект
    create_project = base_url.create_project(my_authorization, my_content_type, my_title)
    assert 'id' in create_project.json()

    # Получаем список проектов после создания проекта
    resp = base_url.get_project_list(my_authorization, my_content_type)
    assert 'id' in resp.json()['content'][-1]
    assert 'title' in resp.json()['content'][-1]
    assert resp.json()['content'][-1]['title'] == my_title

def test_get_project_list_negative():
    my_content_type = "application/json"
    my_title = "Football"

    # Создаем новый проект
    create_project = base_url.create_project(my_authorization, my_content_type, my_title)
    assert 'id' in create_project

    # Получаем список проектов после создания проекта
    resp = base_url.get_project_list(my_content_type)
    assert 'id' in resp[0]
    assert 'title' in resp[2]
    assert resp[-1]['title'] == my_title

def test_get_id_project():
    my_authorization = "Bearer NlzQ55ry-5iWlqWtHsedlREWu2vvdlIapBKmNO-nX+EnurlfIJ6YEoQNy85xFZYN"
    my_content_type = "application/json"
    my_title = "Football"

    # Создаем новый проект
    create_project = base_url.create_project(my_authorization, my_content_type, my_title)
    # assert 'id' in create_project

    project_id = create_project.json()['id']

    # Получаем по id проект после создания проекта
    resp = base_url.get_id_project(my_authorization, my_content_type, project_id)
    assert len(resp.json()) > 0
    assert resp.json()['title'] == my_title

def test_get_id_project_negative():
    my_authorization = "Bearer NlzQ55ry-5iWlqWtHsedlREWu2vvdlIapBKmNO-nX+EnurlfIJ6YEoQNy85xFZYN"
    my_content_type = "application/json"
    my_title = "Football"

    # Создаем новый проект
    create_project = base_url.create_project(my_authorization, my_content_type, my_title)
    assert 'id' in create_project

    # Получаем проект после создания проекта
    resp = base_url.get_id_project(my_authorization, my_content_type)

    assert len(resp) > 0
    assert resp['title'] == my_title

def test_edit_by_id():
    my_authorization = "Bearer NlzQ55ry-5iWlqWtHsedlREWu2vvdlIapBKmNO-nX+EnurlfIJ6YEoQNy85xFZYN"
    my_content_type = "application/json"
    my_title = "Football"
    new_title = "Fooball-Club"

    # Создаем новый проект
    create_project = base_url.create_project(my_authorization, my_content_type, my_title)
    assert 'id' in create_project

    project_id = create_project['id']

    # Получаем проект после создания проекта
    resp = base_url.get_id_project(my_authorization, my_content_type, project_id)
    assert len(resp) > 0

    # Изменяем проект по id
    edit_project = base_url.edit_by_id(my_authorization, my_content_type, project_id, new_title)
    assert 'id' in edit_project

    # Получаем по id проект после редактирования проекта
    resp = base_url.get_id_project(my_authorization, my_content_type, project_id)
    assert resp['title'] == new_title


def test_edit_by_id_negative():
    my_authorization = "Bearer NlzQ55ry-5iWlqWtHsedlREWu2vvdlIapBKmNO-nX+EnurlfIJ6YEoQNy85xFZYN"
    my_content_type = "application/json"
    my_title = "Football"
    new_title = "Fooball-Club"

    # Создаем новый проект
    create_project = base_url.create_project(my_authorization, my_content_type, my_title)
    assert 'id' in create_project

    project_id = create_project['id']

    # Получаем проект после создания проекта
    resp = base_url.get_id_project(my_authorization, my_content_type, project_id)
    assert len(resp) > 0

    # Изменяем проект по id
    edit_project = base_url.edit_by_id(my_authorization, my_content_type, new_title)
    assert 'id' in edit_project

    # Получаем по id проект после редактирования проекта
    resp = base_url.get_id_project(my_authorization, my_content_type, project_id)
    assert resp['title'] == new_title
