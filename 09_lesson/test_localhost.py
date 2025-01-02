from SubjectTable import SubjectTable

db = SubjectTable("postgresql://postgres:2911@localhost:5432/QA")


def test_get_subject():
    db.get_subject()


def test_create_subject():
    last_list = db.get_subject()
    len_before = len(last_list)

    new_id = 16
    new_title = "Physical education"
    db.create(new_id, new_title)

    new_list = db.get_subject()
    len_after = len(new_list)

    db.delete(new_id)

    assert len_after - len_before == 1
    for subject in new_list:
        if subject[-1] == new_id:
            # Проверить название и описание последней компании
            assert subject["subject_title"] == new_title
            # Проверить: id последней компании в списке равен ответу из шага 2
            assert subject["subject_id"] == new_id


def test_edit_by_id():
    subject_id = 16
    old_title = "Physical education"
    db.create(subject_id, old_title)

    new_title = "Art"
    db.edit(subject_id, new_title)

    new_list = db.get_subject()

    db.delete(subject_id)

    for subject in new_list:
        if subject[0] == subject_id:
            assert subject[1] == new_title
            assert subject[0] == subject_id
