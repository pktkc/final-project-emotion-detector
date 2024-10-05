# Import the 'unittest' module to create unit tests for your code.
import unittest

# Import the 'emotion_detector' function from the pakage 'EmotionDetection'
from EmotionDetection.emotion_detection import emotion_detector

# Define a test case class for testing 'emotion_detector" function
class TestEmotiondetector(unittest.TestCase):
    
    # Define the first test method for the 'emotion_detector' function.
    def test1(self):
        # Check that the given statement returns expected dominant emotion.
        result_dict1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_dict1['dominant_emotion'], 'joy')

        # Check that the given statement returns expected dominant emotion.
        result_dict2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_dict2['dominant_emotion'], 'anger')

        # Check that the given statement returns expected dominant emotion.
        result_dict3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_dict3['dominant_emotion'], 'disgust')

        # Check that the given statement returns expected dominant emotion.
        result_dict4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_dict4['dominant_emotion'], 'sadness')

        # Check that the given statement returns expected dominant emotion.
        result_dict5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_dict5['dominant_emotion'], 'fear')

unittest.main()
