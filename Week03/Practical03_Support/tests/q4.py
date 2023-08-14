test = {
    "name": "EKF_results",
    "points": 1,
    "suites": [ 
        {
            "cases": [
                {
                    "code": r"""
                    >>> import pickle
                    >>> with open("Practical03_Support/pickle/q4.pkl", "rb") as f:
                    ...     expected_state, expected_robot_cov = pickle.load(f)
                    >>> np.all(np.isclose(state, expected_state)) and np.all(np.isclose(robot_cov, expected_robot_cov))
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                    "success_message": "Good Job",
                    "failure_message": "Loop implemtation is wrong",
                }
            ],
            "scored": False,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}