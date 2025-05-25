from memre.memory import remember

def test_remember():
    assert remember("foo", "bar") == {"foo": "bar"}
