#!/usr/bin/python
import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging
import pyautogui
import webbrowser
import time

ctypes.windll.kernel32.SetConsoleTitleW(f'D4rka4k Chat Spammer | Loading...')

message = input ('Welcome To D4rka4k Chat Spammer (CLICK ENTER TO CONTINUTE)')
print( )
message = input("What message do you want to keep sending? (Leave this blank if you want to paste your clipboard)  ")
print( )
repeats = int(input("How many times do you want to send the message?  "))
print( )
delay = int(input("How many milliseconds do you want to wait in between each message?  "))
print( )
isLoaded = input("Press Enter when your messaging app is loaded up.")
print( )
print("You have five seconds to refocus the text input area of your messaging app")

time.sleep(5)


for i in range(0,repeats):         #Message sending loop
	if message != "":
		pyautogui.typewrite(message)     
		pyautogui.press("enter")
	else:
		pyautogui.hotkey('ctrl', 'v')      
		pyautogui.press("enter")

	time.sleep(delay/1000)


print("Done\n")

