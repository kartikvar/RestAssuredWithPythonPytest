from methods.CreateBookingAPI import CreateBookingAPI


class TestCreateBookingAPI(CreateBookingAPI):

    def test_create_booking_with_valid_data(self):
        response = self.method_create_booking_with_valid_data()
        assert response is True

    def test_create_booking_with_invalid_data(self):
        response = self.method_create_booking_with_invalid_data()
        assert response is True

    def test_create_booking_with_json_data(self):
        response = self.method_create_booking_with_json_data()
        assert response is True