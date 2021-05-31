import os

from google.cloud import dialogflow
from google.auth import credentials


project_id = 'dialogflow-empathy'
session_id = '123456789'
bearer_token = ''


def main():
    global project_id, session_id, bearer_token

    if 'GOOGLE_APPLICATION_CREDENTIALS' not in os.environ:
        print('ERROR: Must set GOOGLE_APPLICATION_CREDENTIALS env var to the service account JSON key!')
        exit(1)

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    print(f'session_path={session}')

    print("Say something...")
    while True:
        text = input(">>>")
        print(text)
        text_input = dialogflow.TextInput(text=text, language_code='en-US')
        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            dialogflow.DetectIntentRequest(session=session, query_input=query_input),
            timeout=10.0,
        )

        print("=" * 20)
        print("Query text: {}".format(response.query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
            )
        )
        print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))


if __name__ == '__main__':
    main()
