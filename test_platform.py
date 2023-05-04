import pytest
import requests
import json


api_key = "Token 3bfc2547-145c-4e55-902a-b33ea70db37a"
SERVICE_URL = "https://api.soffos.ai/service"


class TestPlatformEndpoints:
    def test_ambiguity_detection(self):
        endpoint = SERVICE_URL + "/ambiguity-detection/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {
            "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
            "text": "I saw her duck",
            "sentence_split": 3,
            "sentence_overlap": True,
        }

        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        print(output)
        assert "ambiguities" in output.keys()

    def test_qna_generation(self):
        endpoint = SERVICE_URL + "/qna-generation/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {
            "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
            "text": "AI and specifically NLP is a very powerful component to any application that makes it powerful, interesting and creative. However, implementing the NLP components can sometimes be hard, or very costly in cases where an NLP engineering team has to be hired to build it. Especially, since NLP keeps evolving at an absurd rate, it might be impossible for a developer to keep up with the advancements in terms of work that needs to be done or money that need to be spent to keep their NLP at a state where it can compete with similar apps out there. Here at Soffos we have packaged several high-level functionalities as modules, some of which require multiple types of NLP and complex logic, for developers to use out-of-the-box, as is, removing the need to develop it themselves. Moreover, Soffos continuously updates their modules to match the state of the art. Developers will never need to maintain any AI/NLP related component of their application. All they need is to be creative, come up with ideas, and combine our modules however they desire to come up with amazing intelligent applications.",
            "sentence_split": 5,
            "sentence_overlap": True,
        }

        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        assert "qna_list" in output.keys()

    def test_answer_scoring(self):
        endpoint = SERVICE_URL + "/answer-scoring/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {
            "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
            "context": "Genetic evidence suggests that dogs descended directly from wolves (Canis) and that the now-extinct wolf lineages that produced dogs branched off from the line that produced modern living wolves sometime between 27,000 and 40,000 years ago. The timing and location of dog domestication is a matter of debate. There is strong genetic evidence, however, that the first domestication events occurred somewhere in northern Eurasia between 14,000 and 29,000 years ago.",
            "question": "How long ago did dogs first become domesticated?",
            "answer": "Between 14,000 and 29,000 years ago.",
            "user_answer": "around 20,000 years ago.",
        }

        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        assert "score" in output.keys()

    def test_contradiction_detection(self):
        endpoint = SERVICE_URL + "/contradiction-detection/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {
            "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
            "text": "The source noted that the Shaheen-2, with a range of 2400 km, has never been tested by Pakistan. Pakistan has said that it performed several tests of its 2300 km-range Shaheen-2 missile in September 2004.",
        }

        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        assert "contradictions" in output.keys()

    def test_emotion_detection(self):
        endpoint = SERVICE_URL + "/emotion-detection/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {
            "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
            "sentence_split": 1,
            "sentence_overlap": False,
            "text": 'On my birthday I got up in the morning with a sad face. I went down to have my breakfast after a long time and as I went down the stairs, I saw all my friends, cousins and my grandparents there. They all wished me "Happy Birthday" and I was shocked, surprised, and very happy. Trust me on this, nothing makes you gladder than seeing all your favourite people together. It was one of the best birthdays that I ever had.',
            "emotion_choices": [
                "joy",
                "trust",
                "fear",
                "surprise",
                "sadness",
                "disgust",
                "anger",
                "anticipation",
            ],
        }

        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        assert "spans" in output.keys()

    def test_language_detection(self):
        endpoint = SERVICE_URL + "/language-detection/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {
            "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
            "text": "Ο Σωκράτης (Αλωπεκή, Αρχαία Αθήνα, 470 π.Χ./469 – Αρχαία Αθήνα, 399 π.Χ.) ήταν Έλληνας Αθηναίος φιλόσοφος, που θεωρείται ο ιδρυτής της Δυτικής φιλοσοφίας και συγκαταλέγεται στους πρώτους ηθικούς φιλοσόφους. Δεν συνέγραψε κάποιο φιλοσοφικό έργο όσο ζούσε· η διδασκαλία του επιβίωσε μέσω των καταγραφών που έκαναν μαθητές του όπως ο Πλάτων και ο Ξενοφών, μετά τον θάνατό του. Οι καταγραφές αυτές συνιστούν διαλόγους, στους οποίους ο Σωκράτης και οι συνδιαλεγόμενοι με αυτόν εξετάζουν διάφορα ζητήματα βάσει της διαλεκτικής μεθόδου. Συχνά, οι γραπτές μαρτυρίες της φιλοσοφίας του παρουσιάζουν αντιφάσεις μεταξύ τους, με αποτέλεσμα η πλήρης ανακατασκευή της σωκρατικής σκέψης να συνιστά δυσεπίλυτο πρόβλημα.",
        }

        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        assert "language" in output.keys()

    def test_logical_error_detection(self):
        endpoint = SERVICE_URL + "/logical-error-detection/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {
            "text": "Nobody has found evidence that UFOs don't exist, therefore they must exist. Many people are saying that voter fraud is real, therefore it must be real.",
            "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
        }

        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        assert "logical_errors" in output.keys()

    def test_microlesson(self):
        endpoint = SERVICE_URL + "/microlesson/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {
            "content": [
                {"source": "my_document1.docx", "text": "Some text"},
                {"source": "my_document2.docx", "text": "Some text"},
            ],
            "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
        }

        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        assert "microlesson" in output.keys()

    def test_named_entity_recognition(self):
        endpoint = SERVICE_URL + "/ner/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {
            "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
            "text": 'Automobiles Ettore Bugatti was a German then French manufacturer of high-performance automobiles. The company was founded in 1909 in the then-German city of Molsheim, Alsace, by the Italian-born industrial designer Ettore Bugatti. The cars were known for their design beauty and for their many race victories. Famous Bugatti automobiles include the Type 35 Grand Prix cars, the Type 41 "Royale", the Type 57 "Atlantic" and the Type 55 sports car. The death of Ettore Bugatti in 1947 proved to be a severe blow for the marque, and the death of his son Jean Bugatti in 1939 meant that there was no successor to lead the factory. No more than about 8,000 cars were made. The company struggled financially, and it released one last model in the 1950s before eventually being purchased for its airplane parts business in 1963.',
        }

        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        assert "named_entities" in output.keys()

    def test_paraphrase(self):
        endpoint = SERVICE_URL + "/paraphrase/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {
            "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
            "text": "During mitosis, a cell duplicates all of its contents, including its chromosomes, and splits to form two identical daughter cells. Because this process is so critical, the steps of mitosis are carefully controlled by certain genes. When mitosis is not regulated correctly, health problems such as cancer can result.",
        }

        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        assert "paraphrase" in output.keys()

    def test_simplify(self):
        endpoint = SERVICE_URL + "/simplify/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {
            "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
            "text": "During mitosis, a cell duplicates all of its contents, including its chromosomes, and splits to form two identical daughter cells. Because this process is so critical, the steps of mitosis are carefully controlled by certain genes. When mitosis is not regulated correctly, health problems such as cancer can result.",
        }

        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        assert "paraphrase" in output.keys()

    def test_inappropriate_content_detection(self):
        endpoint = SERVICE_URL + "/profanity/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {"user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab", "text": "go to hell"}
        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        assert "offensive_probability" in output.keys()

    def test_question_answering(self):
        endpoint = SERVICE_URL + "/question-answering/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {
            "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
            "message": "Who is neo?",
            "document_text": "<The Matrix is a 1999 science fiction action film written and directed by the Wachowskis. It is the first installment in The Matrix film series, starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano. It depicts a dystopian future in which humanity is unknowingly trapped inside a simulated reality, the Matrix, which intelligent machines have created to distract humans while using their bodies as an energy source. When computer programmer Thomas Anderson, under the hacker alias Neo, uncovers the truth, he joins a rebellion against the machines along with other people who have been freed from the Matrix. The Matrix is an example of the cyberpunk subgenre of science fiction. The Wachowskis approach to action scenes was influenced by Japanese animation and martial arts films, and the film's use of fight choreographers and wire fu techniques from Hong Kong action cinema influenced subsequent Hollywood action film productions. The film popularized a visual effect known as bullet time, in which the heightened perception of certain characters is represented by allowing the action within a shot to progress in slow-motion while the camera appears to move through the scene at normal speed, allowing the sped-up movements of certain characters to be perceived normally. The Matrix opened in theaters in the United States on March 31, 1999 to widespread acclaim from critics, who praised its innovative visual effects, action sequences, cinematography and entertainment value, and was a massive success at the box office, grossing over $460 million on a $63 million budget, becoming the highest-grossing Warner Bros. film of 1999 and the fourth highest-grossing film of that year. At the 72nd Academy Awards, the film won all four categories it was nominated for, Best Visual Effects, Best Film Editing, Best Sound, and Best Sound Editing. The film was also the recipient of numerous other accolades, including Best Sound and Best Special Visual Effects at the 53rd British Academy Film Awards, and the Wachowskis were awarded Best Director and Best Science Fiction Film at the 26th Saturn Awards. The film is considered to be among the greatest science fiction films of all time, and in 2012, the film was selected for preservation in the United States National Film Registry by the Library of Congress for being culturally, historically, and aesthetically significant. The film's success led to two feature film sequels being released in 2003, The Matrix Reloaded and The Matrix Revolutions, which were also written and directed by the Wachowskis. The Matrix franchise was further expanded through the production of comic books, video games and animated short films, with which the Wachowskis were heavily involved. The franchise has also inspired books and theories expanding on some of the religious and philosophical ideas alluded to in the films. A fourth film, titled The Matrix Resurrections, was released on December 22, 2021. Neo is a computer programmer, born Thomas A. Anderson, who secretly operates as a hacker. Reeves described his character as someone who felt that something was wrong, and was searching for Morpheus and the truth to break free. Morpheus is a human freed from the Matrix and captain of the Nebuchadnezzar acted by Laurence Fishburne.>",
            "check ambiguity": True,
            "check_query_type": True,
            "generic_response": False,
            "meta": {"session_id": "69cb9520-885b-4f81-ae6c-79b8d63ff25c"},
        }
        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        assert "answer" in output.keys()

    def test_review_tagger(self):
        endpoint = SERVICE_URL + "/review-tagger/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {
            "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
            "text": "This oven has been a complete disaster from the start. After about 2 weeks of use, the oven and broiler burners would turn off suddenly after being on for only 5 seconds. This has been an ongoing issue for months, and it still does not work.",
        }
        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        assert "object" in output.keys()

    def test_sentiment_analysis(self):
        endpoint = SERVICE_URL + "/sentiment-analysis/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {
            "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
            "text": "I feel happy. I feel sad. I am human.",
            "sentence_split": 1,
            "sentence_overlap": False,
        }
        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        assert "sentiment_breakdown" in output.keys()

    def test_summarization(self):
        endpoint = SERVICE_URL + "/summarization/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {
            "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
            "sent_length": 3,
            "text": "Ludwig van Beethoven (baptised 17 December 1770 – 26 March 1827) was a German composer and pianist. ... After some months of bedridden illness, he died in 1827. Beethoven's works remain mainstays of the classical music repertoire.",
        }
        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        assert "summary" in output.keys()

    def test_tag_generation(self):
        endpoint = SERVICE_URL + "/tag/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {
            "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
            "text": "The Matrix is a 1999 science fiction action film written and directed by the Wachowskis. It is the first installment in The Matrix film series...",
            "options": ["one_word", "two_words", "three_words"],
        }
        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        assert "one_word" in output.keys()

    def test_transcript_correction(self):
        endpoint = SERVICE_URL + "/transcript-correction/"
        headers = {"x-api-key": api_key, "Content-Type": "application/json"}
        _json = {
            "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
            "text": " We just want to show people or services can't help them. Create amazing. Applications",
        }
        response = requests.post(url=endpoint, headers=headers, json=_json)
        output = response.json()
        assert "correction" in output.keys()
