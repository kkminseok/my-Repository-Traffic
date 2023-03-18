from module.issues.prev_issue_viewer_utils import set_prev_issue_viewer


def test_set_prev_issue_viewer(last_issue):
    set_prev_issue_viewer(None, last_issue)
