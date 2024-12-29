from Yougile import Yougile

base_url = Yougile("https://ru.yougile.com/api-v2")
key = "g5ci5PegiSCIFP8LgP1bIjEKhyS8gP0QzIV0ex8RH0U+bkhFHJbQSsTcJVlPImNH"


def test_create_project():
    my_authorization = "Bearer NlzQ55ry-5iWlqWtHsedlREWu2vvdlIapBKmNO-nX+EnurlfIJ6YEoQNy85xFZYN"
    my_content_type = "application/json"
    my_title = "Football"

    # Получаем список проектов до создания нового
    all_company_list = base_url.get_project_list(
        my_authorization, my_content_type)
    len_before = len(all_company_list.json()['content'])

    # Создаем новый проект
    resp = base_url.create_project(my_authorization, my_content_type, my_title)
    assert resp.status_code == 201
    assert 'id' in resp.json()

    # Получаем список проектов после создания нового проекта
    result = base_url.get_project_list(my_authorization, my_content_type)
    len_after = len(result.json()['content'])
    assert len_after - len_before == 1


def test_create_project_negative():
    my_authorization = "Bearer NlzQ55ry-5iWlqWtHsedlREWu2vvdlIapBKmNO-nX+EnurlfIJ6YEoQNy85xFZYN"
    my_content_type = "application/json"
    my_title = ""

    # Создаем новый проект
    resp = base_url.create_project(my_authorization, my_content_type, my_title)
    assert resp.status_code == 400


def test_get_project_list():
    my_authorization = "Bearer NlzQ55ry-5iWlqWtHsedlREWu2vvdlIapBKmNO-nX+EnurlfIJ6YEoQNy85xFZYN"
    my_content_type = "application/json"
    my_title = "Football"

    # Создаем новый проект
    create_project = base_url.create_project(
        my_authorization, my_content_type, my_title)
    assert 'id' in create_project.json()

    # Получаем список проектов после создания проекта
    resp = base_url.get_project_list(my_authorization, my_content_type)
    assert resp.status_code == 200
    assert 'id' in resp.json()['content'][-1]
    assert 'title' in resp.json()['content'][-1]
    assert resp.json()['content'][-1]['title'] == my_title


def test_get_project_list_negative():
    my_authorization = ""
    my_content_type = "application/json"
    my_title = "Football"

    # Создаем новый проект
    base_url.create_project(my_authorization, my_content_type, my_title)

    # Получаем список проектов после создания проекта
    resp = base_url.get_project_list(my_authorization, my_content_type)
    assert resp.status_code == 404


def test_get_id_project():
    my_authorization = "Bearer NlzQ55ry-5iWlqWtHsedlREWu2vvdlIapBKmNO-nX+EnurlfIJ6YEoQNy85xFZYN"
    my_content_type = "application/json"
    my_title = 'Football'

    # Создаем новый проект
    create_project = base_url.create_project(
        my_authorization, my_content_type, my_title)
    assert 'id' in create_project.json()

    project_id = create_project.json()['id']

    # Получаем по id проект после создания проекта
    resp = base_url.get_id_project(
        my_authorization, my_content_type, project_id)
    assert resp.status_code == 200
    assert resp.json()['title'] == my_title


def test_get_id_project_negative():
    my_authorization = "Bearer NlzQ55ry-5iWlqWtHsedlREWu2vvdlIapBKmNO-nX+EnurlfIJ6YEoQNy85xFZYN"
    my_content_type = "application/json"
    my_title = "Football"

    # Создаем новый проект
    create_project = base_url.create_project(
        my_authorization, my_content_type, my_title)

    project_id = create_project.json()['id'] + f'1'

    # Получаем по id проект после создания проекта
    resp = base_url.get_id_project(
        my_authorization, my_content_type, project_id)
    assert resp.status_code == 404


def test_edit_by_id():
    my_authorization = "Bearer NlzQ55ry-5iWlqWtHsedlREWu2vvdlIapBKmNO-nX+EnurlfIJ6YEoQNy85xFZYN"
    my_content_type = "application/json"
    my_title = "Football"
    new_title = "Fooball-Club"

    # Создаем новый проект
    create_project = base_url.create_project(
        my_authorization, my_content_type, my_title)
    assert 'id' in create_project.json()

    project_id = create_project.json()['id']

    # Получаем проект после создания проекта
    resp = base_url.get_id_project(
        my_authorization, my_content_type, project_id)
    assert resp.json()['title'] == my_title

    # Изменяем проект по id
    edit_project = base_url.edit_by_id(
        my_authorization, my_content_type, project_id, new_title)
    assert edit_project.status_code == 200
    assert 'id' in edit_project.json()


def test_edit_by_id_negative():
    my_authorization = "Bearer NlzQ55ry-5iWlqWtHsedlREWu2vvdlIapBKmNO-nX+EnurlfIJ6YEoQNy85xFZYN"
    my_content_type = "application/json"
    my_title = "Football"
    new_title = "Fooball-Club"

    # Создаем новый проект
    create_project = base_url.create_project(
        my_authorization, my_content_type, my_title)

    project_id = create_project.json()['id'] + f'1'

    # Изменяем проект по id
    edit_project = base_url.edit_by_id(
        my_authorization, my_content_type, project_id, new_title)

    assert edit_project.status_code == 404
