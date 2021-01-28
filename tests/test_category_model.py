from models.categories import Category


class TestCategoryModel:
    def test_name_isinstance_str(self):
        try:
            Category(None, 'test description')
            raise NotImplementedError('Not implemented error')
        except Exception as error:
            assert isinstance(error, TypeError)

    def test_name_blank_spaces(self):
        try:
            Category(' ', 'test description')
            raise NotImplementedError('Not implemented error')
        except Exception as error:
            assert isinstance(error, ValueError)

    def test_name_too_big(self):
        try:
            Category('test name'*100, 'test description')
            raise NotImplementedError('Not implemented error')
        except Exception as error:
            assert isinstance(error, ValueError)

    def test_description_isinstance_str(self):
        try:
            Category('test name', None)
            raise NotImplementedError('Not implemented error')
        except Exception as error:
            assert isinstance(error, TypeError)

    def test_description_too_big(self):
        try:
            Category('test name'*100, 'test description')
            raise NotImplementedError('Not implemented error')
        except Exception as error:
            assert isinstance(error, ValueError)
