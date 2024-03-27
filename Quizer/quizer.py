import requests
import config as cf


class QuizerModel:
    def __init__(self):
        self.categoryData = []
        self.categoryNameList = ["Any Category"]
        self.finalParameters = {}
        

    def LookUpCategoryData(self):
        newCall = requests.get(
            url = cf.API_CATEGORIES_ENDPOINT
        )
        self.categoriesData = newCall.json()["trivia_categories"]

        return self.categoriesData
    

    def LookUpCategoryNames(self):
        for category in self.categoriesData:
            self.categoryNameList.append(category["name"])

        return self.categoryNameList
    

    def LookUpQuestions(self):
        self.finalParameters["encode"] = "base64"
        newCall = requests.get(
            cf.API_ENDPOINT,
            params = self.finalParameters
            )
        return newCall.json()["results"]