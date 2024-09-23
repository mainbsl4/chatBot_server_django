from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai

# # Configure the API key
# genai.configure(api_key="AIzaSyDQfckOMFyqQrRIhNI7fHOtLxWkHhdGbK0")

# # Create the model
# generation_config = {
#     "temperature": 0,
#     "top_p": 0.95,
#     "top_k": 64,
#     "max_output_tokens": 8192,
#     "response_mime_type": "text/plain",
# }

# model = genai.GenerativeModel(
#     model_name="gemini-1.5-pro",
#     generation_config=generation_config,
# )

# def chat_view(request):
#     return render(request, 'chat/aichat.html')

# def chat_api(request):
#     user_input = request.GET.get('message', '')

#     if user_input:
#         chat_session = model.start_chat()
#         response = chat_session.send_message(user_input)
#         context = {
#             'user_input': user_input,
#             'response': response.text,
#         }
#         return JsonResponse(context)
#         # return JsonResponse({'response': response.text})

#     return JsonResponse({'response': 'No input provided.'})


#  by link queary +++++++++++++++++++++++++++++++++++++++
# from django.http import JsonResponse
# import google.generativeai as genai

# # Configure the API key
# genai.configure(api_key="AIzaSyDQfckOMFyqQrRIhNI7fHOtLxWkHhdGbK0")

# # Create the model configuration
# generation_config = {
#     "temperature": 0,
#     "top_p": 0.95,
#     "top_k": 64,
#     "max_output_tokens": 8192,
#     "response_mime_type": "text/plain",
# }

# model = genai.GenerativeModel(
#     model_name="gemini-1.5-pro",
#     generation_config=generation_config,
# )

# # Define the function to handle chat messages
# def chat_api(request):
#     user_input = request.GET.get('message', '')

#     if user_input:
#         # Start a chat session with the AI model
#         chat_session = model.start_chat()
#         response = chat_session.send_message(user_input)
#         return JsonResponse({'response': response.text})

#     return JsonResponse({'response': 'No input provided.'})


# by post without db +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import google.generativeai as genai
# import json

# # Configure the API key
# genai.configure(api_key="AIzaSyDQfckOMFyqQrRIhNI7fHOtLxWkHhdGbK0")

# # Create the model configuration
# generation_config = {
#     "temperature": 0,
#     "top_p": 0.95,
#     "top_k": 64,
#     "max_output_tokens": 8192,
#     "response_mime_type": "text/plain",
# }

# model = genai.GenerativeModel(
#     model_name="gemini-1.5-pro",
#     generation_config=generation_config,
# )


# # Define the function to handle chat messages via POST request
# @csrf_exempt  # Disable CSRF for simplicity in testing
# def chat_api(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             user_input = data.get('message', '')

#             if user_input:
#                 # Start a chat session with the AI model
#                 chat_session = model.start_chat()
#                 response = chat_session.send_message(user_input)
#                 return JsonResponse({'response': response.text})

#             return JsonResponse({'error': 'No message provided'}, status=400)

#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON format'}, status=400)

#     return JsonResponse({'error': 'Invalid request method'}, status=405)


# by post with db +++++++++++++++++++++++++++++++++++++++++++++++++++++++

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
import json
from .models import ChatHistory  # Import the model

# Configure the API key
genai.configure(api_key="AIzaSyDQfckOMFyqQrRIhNI7fHOtLxWkHhdGbK0")

# Create the model configuration
generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)


# Define the function to handle chat messages via POST request
@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_input = data.get("message", "")
            if user_input:
                # Start a chat session with the AI model
                chat_session = model.start_chat()
                response = chat_session.send_message(user_input)

                # Save the message and response to the database
                chat_entry = ChatHistory(
                    user_message=user_input, ai_response=response.text
                )
                chat_entry.save()

                return JsonResponse({"response": response.text})

            return JsonResponse({"error": "No message provided"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
