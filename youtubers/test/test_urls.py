from django.urls import reverse,resolve

class TestUrls:
    
    def test_details_url():
        path=reverse('youtubers_details',kwargs={'pk':1})
        assert resolve(path).view_name=='youtubers_details'