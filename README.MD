<h4>Project Description</h4>
This is test task provided by the news360.com company as a task for candidate to QA Automation Team Lead position.</br>
The description of the task you can find in <b>test_design\test_task_for_qa_test_automation.pdf</b></br>
In short candidate should create set of test cases for login form and then create framework and samples of auto tests.

<h4>Requirements</h4>

<li>Installed Chrome Browser on MAC or Windows</li>
<li>Install all requirements using: <b>pip install -r requirements.txt</b></li>

<h4>How to run tests</h4>
<li> py.test test_negative_sing_up.py</li>
<li> py.test test_...</li>

<h5>Also tests can be run in parallel</h5>
<li> py.test <b>-n3</b> test_negative_sing_up.py</li>
Except test_sign_up.py due to strange error, may be connected to py.test known bug.
</br>
<h4>Test framework description</h4>
For auto tests implementation was chosen python language and  <a href="https://github.com/yashaka/selene" >selen framework</a> based 
on Selenium Web Driver.</br>
pytest was used as testing framework</br>
Also Page Object was used as a main pattern .</br>
</br>
<b>core\pages.py</b> contains several classes, each represents screen or page of the web site.</br>
Each classes consist of elements like button or fields or message that used CSS selectors to be found</br>
and methods to manipulate this elements - push the buttons or fill field or read messages.</br>
</br>
<b>core\driver_manager.py</b> are used to allow run selenium web driver on mac and win platforms.</br>
Both chrome drivers are in <b>core\drivers</b> folder, so you don't need to download it.</br>
</br>
<b>test_user_managment\test_data_generator.py</b> generate email and passwords of test users.</br>
It can prepare for tests data of already exists users and also.</br>
unique emails for testing sign_up without delete test user from DB.</br>
<b>positive_static_user_data.json</b> contains already created user and can be used to generate new users.</br>
<b>init_test_account_creator.py</b> was used by me once to create initial users, in real life it can be done by REST API.</br>
</br>
<b>en_errors.py</b> contains constants with errors texts. </br>
If it will be real project it was in json files with different languages. Keep it in this form due to time limitation. </br>
</br>
<h4>Tests description</h4>
In <b>conftest.py</b> you can find set_up and tear_down methods for all tests.</br>
<b>test_negative_sing_up.py</b> shows example how error correctness can be checked. </br>
<b>test_sign_in.py</b> have parametrize test that used <b>test_data_generator</b> to get all needed user data.</br>
<b>test_sign_up.py</b> also have parametrize test to test positive cases in sign up functionality.</br>
</br>

<h4>Test Design description</h4>
In <b>test_design</b> folder you can find all docs about TD.</br>
General plans you can find in <b>test_design\img</b> or <b>test_design\img</b> if you have xmind app. </br>
</br>
Test cases located in <b>tests.ods</b> file.</br>
There are several sheets in it.</br>
</br>
<b>Availability</b> sheet contains 6 test cases tested that login popup available from any page.</br>
<b>S&T_Final sheet</b> contains 26 test cases tested transition between different state and pre-actions.</br>
<b>Errors_Sign_IN</b> sheet contains 14 test cases tested different combinations of email/password presence/correctness in sign up form.</br>
<b>Errors_Sign_UP</b> sheet contains 29 test cases tested different combinations of email/password presence/correctness in sign up form.</br>
<b>Error_Password</b> sheet contains 4 test cases tested different variants of email value in forgot password form.</br>
<b>All these cases were not automated due to time limitation, but it can be done rather easy using created test framework.</b></br>
</br>
<b>Emails</b> sheet contains 40 tests and not fully covered all equivalent classes for email and password, but should be sufficient for smoke testing. </br>
Also not all error message covered by this tests, by example password cannot be more than 200 chars.</br>
Or if we put about 60000 chars in password field we get the JS popup error.</br>
<b>Only this positive tests were automated fully and negative tests were automated partly. </b></br>
</br>
Due to time limitation also test using REST API was not created. </br>
In real project this way will be also used to divide errors on client side from errors on server side</br>




