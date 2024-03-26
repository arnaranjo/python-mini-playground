import requests
"https://opentdb.com/api_config.php"
"https://opentdb.com/api.php?amount=10&category=17&difficulty=medium&type=multiple"

API_ENDPOINT = "https://opentdb.com/api.php?"
API_CATEGORIES_ENDPOINT = "https://opentdb.com/api_category.php"


class QuizerModel:
    def __init__(self):
        self.categoryData = []
        self.categoryNameList = ["Any Category"]
        self.finalParameters = {}
        

    def LookUpCategoryData(self):
        newCall = requests.get(
            url = API_CATEGORIES_ENDPOINT
        )
        self.categoriesData = newCall.json()["trivia_categories"]

        return self.categoriesData
    

    def LookUpCategoryNames(self):
        for category in self.categoriesData:
            self.categoryNameList.append(category["name"])

        return self.categoryNameList
    
    #TODO: Fix the encoding.
    def LookUpQuestions(self):
        self.finalParameters["encode"] = "base64"
        newCall = requests.get(
            API_ENDPOINT,
            params = self.finalParameters
            )
        return newCall.json()["results"]