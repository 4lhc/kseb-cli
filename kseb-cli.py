#!/bin/env python3

from selenium import webdriver
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("customer_num", type=str, help="Customer Number")
args=parser.parse_args()

quickpay_url = "https://wss.kseb.in/selfservices/quickpay"


options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(quickpay_url)

textarea = driver.find_element_by_id("ConsumerNo")
submit = driver.find_element_by_id("see-bill-due")
textarea.send_keys(args.customer_num)
submit.click()


if "quickPayVerification" in driver.current_url:
    d = driver.find_elements_by_xpath("//input[@id='focusedInput']")
    names = ["Consumer Name:", "Section Name:", "Tariff Code:", "Bill Amount:", "Due Amount:"]
    for i, name in zip(d, names):
        print(name, i.get_attribute("value"))
