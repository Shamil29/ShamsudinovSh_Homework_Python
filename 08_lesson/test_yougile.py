import requests
from Yougile import Yougile

base_url = Yougile("https://ru.yougile.com/api-v2")

def test_create_key():
    my_authorization = ""
    my_content_type = "application/json"
    my_login = ""
    my_password = ""
    company_id = "d0b3ce73-ee47-4b29-b752-c976efd4f11c"

    resp = base_url.create_key(my_authorization, my_content_type, my_login, my_password, company_id)
    assert len(resp) > 0

def test_create_key_negative():
    my_login = ""
    my_password = ""
    company_id = "d0b3ce73-ee47-4b29-b752-c976efd4f11c"

    resp = base_url.create_key(my_login, my_password, company_id)
    assert len(resp) > 0

def test_create_project():
    my_authorization = ""
    my_content_type = "application/json"
    my_title = "Football"

    all_company_list = base_url.get_project_list(my_authorization, my_content_type)
    len_before = len(all_company_list)

    resp = base_url.create_project(my_authorization, my_content_type, my_title)

    result = base_url.get_project_list(my_authorization, my_content_type)
    len_after = len(result)

    assert len_after - len_before == 1
    assert len(resp) > 0

def test_create_project_negative():
    my_authorization = ""
    my_content_type = "application/json"

    all_company_list = base_url.get_project_list(my_authorization, my_content_type)
    len_before = len(all_company_list)

    resp = base_url.create_project(my_authorization, my_content_type)

    result = base_url.get_project_list(my_authorization, my_content_type)
    len_after = len(result)

    assert len_after - len_before == 1
    assert len(resp) > 0

def test_get_project_list():
    my_authorization = ""
    my_content_type = "application/json"
    my_title = "Football"

    create_project = base_url.create_project(my_authorization, my_content_type, my_title)

    resp = base_url.get_project_list(my_authorization, my_content_type)
    assert resp[-1]['title'] == my_title

def test_get_project_list_negative():
    my_content_type = "application/json"
    my_title = "Football"

    create_project = base_url.create_project(my_authorization, my_content_type, my_title)

    resp = base_url.get_project_list(my_content_type)
    assert resp[-1]['title'] == my_title

def test_get_id_project():
    my_authorization = ""
    my_content_type = "application/json"
    my_title = "Football"

    create_project = base_url.create_project(my_authorization, my_content_type, my_title)
    project_id = create_project['id']
    resp = base_url.get_id_project(my_authorization, my_content_type, project_id)

    assert len(resp) > 0
    assert resp[-1]['title'] == my_title

def test_get_id_project_negative():
    my_authorization = ""
    my_content_type = "application/json"
    my_title = "Football"

    create_project = base_url.create_project(my_authorization, my_content_type, my_title)
    resp = base_url.get_id_project(my_authorization, my_content_type)

    assert len(resp) > 0
    assert resp[-1]['title'] == my_title

def test_edit_by_id():
    my_authorization = ""
    my_content_type = "application/json"
    my_title = "Football"
    new_title = "Fooball-Club"
    create_project = base_url.create_project(my_authorization, my_content_type, my_title)
    project_id = create_project['id']

    resp = base_url.get_id_project(my_authorization, my_content_type, project_id, new_title)
    assert len(resp) > 0

def test_edit_by_id_negative():
    my_authorization = ""
    my_content_type = "application/json"
    my_title = "Football"
    new_title = "Fooball-Club"
    create_project = base_url.create_project(my_authorization, my_content_type, my_title)

    resp = base_url.edit_by_id(my_authorization, my_content_type, new_title)
    assert len(resp) > 0
