import requests


class Yougile:
    def __init__(self, url):
        self.url = url

    # [POST]/api-v2/projects - Создать проект
    def create_project(self, my_authorization, my_content_type, my_title):
        my_headers = {
            "Authorization": my_authorization,
            "Content-Type": my_content_type
        }

        body = {
            'title': my_title
        }

        resp = requests.post(
            self.url + '/projects', headers=my_headers, json=body)
        return resp

    # [GET]/api-v2/projects - Получить список проектов
    def get_project_list(self, my_authorization, my_content_type):
        my_headers = {
            "Authorization": my_authorization,
            "Content-Type": my_content_type
        }
        resp = requests.get(self.url + '/projects', headers=my_headers)
        return resp

    # [GET]/api-v2/projects/{id} - Получить по ID
    def get_id_project(self, my_authorization, my_content_type, project_id):
        my_headers = {
            "Authorization": my_authorization,
            "Content-Type": my_content_type
        }
        my_project_id = {
            "id": project_id
        }
        resp = requests.get(
            self.url + f"/projects/{project_id}", headers=my_headers)
        return resp

    # [PUT]/api-v2/projects/{id} - Изменить
    def edit_by_id(
            self, my_authorization, my_content_type, project_id, new_title):
        my_headers = {
            "Authorization": my_authorization,
            "Content-Type": my_content_type
        }
        id_project = {
            "id": project_id,
        }
        body = {
            "title": new_title
        }

        resp = requests.put(
            self.url + f"/projects/{project_id}", headers=my_headers, json=body)
        return resp
