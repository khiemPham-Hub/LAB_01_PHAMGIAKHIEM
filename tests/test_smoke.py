from assistant.rules import reply


def test_greeting():
    assert "Hello" in reply("hi")


def test_office_lookup():
    assert "I.101" in reply("Where is the Training Office?")


def test_unknown():
    assert "don't know" in reply("what is the meaning of life")


def test_empty():
    assert reply("   ") == "Please type a question."

def test_registrar_office_lookup():
    answer = reply("Where is the Registrar Office?")
    assert "I.103" in answer
    assert "Mon-Fri 08:00-16:00" in answer


def test_counseling_office_lookup():
    answer = reply("Where is the Counseling Office?")
    assert "C.202" in answer
    assert "Mon-Fri 09:00-17:00" in answer
