@echo off
pytest -v -m "regression" --html=Report\report.html testCase
rem pytest -v -m "sanity" --html=Report\report.html testCase
rem pytest -v -m "regression or sanity" --html=Report\report.html testCase
rem pytest -v -m "regression and sanity" --html=Report\report.html testCase
rem pytest -v -s  --alluredir="D:\DissertaionProject\STAF Hybrid Design\allure-report" testCase\test_Login.py

rem allure serve "D:\DissertaionProject\STAF Hybrid Design\allure-report"