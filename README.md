# resumeapi-uploader
1. Open Postman and create a new POST request.
2. Enter the URL for your Django API endpoint where you want to create the `Resume` instance. For example: `http://localhost:8000/api/resume/`.
3. Go to the "Body" tab in Postman.
4. Select the "x-www-form-urlencoded" option.
5. Add the key-value pairs for each field in the request body. For example:
   - `name`:  vivek
   - `email`: example@example.com
   - `dob`: 2000-01-01
   - `state`: haryana
   - `gender`: Male
   - `location`: Some Location
   - `pimage`: [Select File] (if you want to upload an image file)
   - `rdoc`: [Select File] (if you want to upload a document file)
6. Click the "Send" button to send the POST request to your Django API endpoint.


==================================================================================================================================================


To retrieve the created `Resume` instances using a GET request in Postman, you can follow these steps:

1. Open Postman and create a new GET request.
2. Enter the URL for your Django API endpoint where the `Resume` instances are stored. For example: `http://localhost:8000/api/resume/`.
3. Click the "Send" button to send the GET request to your Django API endpoint.

Ensure that you have your Django server running locally (`python manage.py runserver`) or deployed to an appropriate environment, and that the API endpoint URL matches the one you provided in your Django `urls.py` file.

The Django server should receive the GET request and return a response containing the `Resume` instances stored in the database. The response may be in JSON format and contain information about each `Resume` instance, such as the name, email, dob, state, gender, location, etc.

Please note that you may need to adjust the URL or request parameters depending on your specific requirements or configurations.
