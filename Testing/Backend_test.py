import unittest
import requests

class BackendTestCase(unittest.TestCase):
    
    
    def test_AllSensors_data(self):
        response = requests.get('http://localhost:5005/api/Allsensors_data')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreater(len(data), 0)


    def test_AllAQdata(self):
        response = requests.get('http://localhost:5005/api/AllAQ_data')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreater(len(data), 0)
        
        
    def test_AllData(self):
        response = requests.get('http://localhost:5005/api/all_data')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreater(len(data), 0)


    def test_station_filter(self):
        payload = {"station_name": "Milano v.Senato"}
        response = requests.post('http://localhost:5005/api/date_filtered', json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreater(len(data), 0)
        
        
        
    def test_sensor_type_filter(self):
        payload = {"sensor_type": "Benzene"}
        response = requests.post('http://localhost:5005/api/sensor_type_filtered', json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreater(len(data), 0)
        


    def test_comune_filter(self):
        payload = {"comune": "Como"}
        response = requests.post('http://localhost:5005/api/comune_filtered', json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreater(len(data), 0)


    def test_province_filter(self):
        payload = {"Province": "MI"}
        response = requests.post('http://localhost:5005/api/province_filtered', json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreater(len(data), 0)

if __name__ == '__main__':
    unittest.main()
