import pytest


@pytest.mark.api
def test_user_exists(github_api):
    response = github_api.get_user('defunkt')
    assert response['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    response = github_api.get_user('butenkosergii')
    assert response['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    response = github_api.search_repo('become-qa-auto')
    assert response['total_count'] == 58

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    response = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert response['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    response = github_api.search_repo('s')
    assert response['total_count'] != 0


#Adding tests for new methods


@pytest.mark.api
def test_get_emojis(github_api):
    response = github_api.get_emojis()
    assert 'smile' in response

@pytest.mark.api
def test_list_commits(github_api):
    response = github_api.list_commits('octocat', 'Hello-World')
    assert isinstance(response, list)
    assert 'commit' in response[0]