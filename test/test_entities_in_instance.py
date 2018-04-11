import unittest
from api.dialogflow_service import DialogFlowService
import dialogflow


class TestEntitiesInInstance(unittest.TestCase):
    FILE_PATH = "Keywords_lite.txt"
    SENTENCES = ["There seems to be a lot of bugs in the api.", "I got a 404 on the kitten page.", "Do you know about crawlers?", "We are thinking about using Mongo DB, good idea?", "We are thinking about using mongodb, good idea?", "I like the coveo search interface", "Look at all the space components on github from my chrome browser."]
    ENTITY_TYPE_NAME = "testType"
    OUTPUT_FILE_PATH = "TestEntitiesInInstanceOutput.txt"

    def setUp(self):
        self.service = DialogFlowService()

    def test_scenario(self):
        outputFile = open(self.OUTPUT_FILE_PATH, 'w')
        for sentence in self.SENTENCES:
            nlp_analysis = self.service.analyse_sentence(sentence)
            for entity in nlp_analysis.entities:
                outputFile.write(entity.name)
            outputFile.write("/n")

        self.add_entities_to_instance(self.FILE_PATH, self.ENTITY_TYPE_NAME)

        outputFile.write("After entities are added/n")

        for sentence in self.SENTENCES:
            nlp_analysis = self.service.analyse_sentence(sentence)
            for entity in nlp_analysis.entities:
                outputFile.write(entity.name)
            outputFile.write("/n")

        outputFile.close()

    def add_entities_to_instance(self, file_path, entity_type_name):
        file = open(file_path)
        keywords = file.readlines()
        self.service.add_entity_type(entity_type_name)
        self.service.add_entities(entity_type_name, keywords)


if __name__ == '__main__':
    unittest.main()
