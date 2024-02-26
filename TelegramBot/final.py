import key
import logging
from telegram import Update
from telegram.ext import filters,MessageHandler,ApplicationBuilder,ContextTypes,CommandHandler
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
import api_key
from langchain.prompts import ChatPromptTemplate
import json
import asyncio
import on_off
import os
import pygame
import pyaudio

def telegramservices():
    pygame.init()
    pygame.mixer.music.load('telegramservices.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()
    pygame.mixer.quit()


def good_format(lines):
    my_new_lines=lines.replace("JSON","")
    my_new_lines=my_new_lines.replace("json","")
    my_new_lines=my_new_lines[3:-3]
    return my_new_lines


def GoogleGenAI(command):
    reply1=""
    reply2=""
    question=command
    chat_llm=ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=api_key.GOOGLE_API_KEY)
    template_string = """You are a  AI Assistant who specializes in switching on or off equipments. \
    You come up with what should be switched on or switched off.

    Take the query below delimited by triple backticks and use it to tell that which equipments of home should be switched on or switched off.
    User Prefrences: When going to office then switch off all device of Parent Bedroom only, When going to school switch off all device of Child Bedroom, When coming back from office then switch on AC to cool to the room, Switch off AC if user say I am feeling cold, If user say I am going to bath switch on geyser and washroom bulb. If directly say to switch on or off something then switch on or off that thing directly.  When water is finished then switch on motor pump.

    query: ```{query}```

    then based on the description and list of equipments sepeareted by commas Parent Bedroom Bulb,Parent Bedroom Fan,Parent Bedroom AC,Child Bedroom Bulb,Child Bedroom Fan,Child AC,Child Study Lamp,Kitchen bulb,Geyser in washroom,Living Room Bulb,Living room Fan,Living Room AC, Motor Pump.Tell which should be switched on or switched off

    Format the output as JSON with the following keys:
    switched_on_equipments
    reply_I_have_swithced_on_this_this_and_this.
    switched_off_equipments
    reply_I_have_swithced_off_this_this_and_this
    if_the_query_doesnt_seem_to_be_switching_on_or_off_then_turn_on_AI_mode
    """
    prompt_template=ChatPromptTemplate.from_template(template_string)
    output1=prompt_template.messages[0].prompt
    print(output1)
    branding_messages = prompt_template.format_messages( query=f"{question}")
    print(branding_messages)
    consultant_response=chat_llm(branding_messages)
    print(consultant_response.content)
    output3=consultant_response.content
    print(type(output3))
    f=open('instruction.json','w')
    f.write(good_format(consultant_response.content))
    f.close()
    with open('instruction.json') as f:
        data=json.load(f)

    if data['if_the_query_doesnt_seem_to_be_switching_on_or_off_then_turn_on_AI_mode']:
        model=genai.GenerativeModel('gemini-pro')
        chat=question
        response=model.generate_content(chat)
        answer_generated=response.text
        answer_generated=answer_generated.replace('*','')
        return answer_generated
    if data['if_the_query_doesnt_seem_to_be_switching_on_or_off_then_turn_on_AI_mode']!=True:    
        if data['reply_I_have_swithced_on_this_this_and_this']!=None:
            reply1=data['reply_I_have_swithced_on_this_this_and_this']
        if data['reply_I_have_swithced_off_this_this_and_this']!=None:
            reply2=(data['reply_I_have_swithced_off_this_this_and_this'])
        for device_on in data['switched_on_equipments']:
            if(device_on.lower()=='Parent Bedroom Bulb'.lower()):
                on_off.p_bedroom_bulb_on()
            if(device_on.lower()=='Parent Bedroom Fan'.lower()):
                on_off.p_fan_on()
            if (device_on.lower()=='Parent Bedroom AC'.lower()):
                on_off.p_AC_on()
            if(device_on.lower()=='Child Bedroom Bulb'.lower()):
                on_off.c_bedroom_bulb_on()
            if(device_on.lower()=='Child Bedroom AC'.lower()):
                on_off.c_AC_on()
            if(device_on.lower()=='Child Study Lamp'.lower()):
                on_off.c_study_lamp_on()
            if(device_on.lower()=='Kitchen Bulb'.lower()):
                on_off.k_bulb_on()
            if(device_on.lower()=='Washroom Bulb'.lower()):
                on_off.w_bulb_on()
            if(device_on.lower()=='Living Room Bulb'.lower()):
                on_off.l_bulb_on()
            if(device_on.lower()=='Living Room Fan'.lower()):
                on_off.l_fan_on()
            if(device_on.lower()=='Living Room AC'.lower()):
                on_off.l_AC_on()
            if(device_on.lower()=='Motor Pump for filling water tank'.lower()):
                on_off.motor_on()
        for device_off in data['switched_off_equipments']:
            if(device_off.lower()=='Parent Bedroom Bulb'.lower()):
                on_off.p_bedroom_bulb_off()
            if(device_off.lower()=='Parent Bedroom Fan'.lower()):
                on_off.p_fan_off()
            if (device_off.lower()=='Parent Bedroom AC'.lower()):
                on_off.p_AC_on()
            if(device_off.lower()=='Child Bedroom Bulb'.lower()):
                on_off.c_bedroom_bulb_off()
            if(device_off.lower()=='Child Bedroom AC'.lower()):
                on_off.c_AC_off()
            if(device_off.lower()=='Child Study Lamp'.lower()):
                on_off.c_study_lamp_off()
            if(device_off.lower()=='Kitchen Bulb'.lower()):
                on_off.k_bulb_off()
            if(device_off.lower()=='Washroom Bulb'.lower()):
                on_off.w_bulb_off()
            if(device_off.lower()=='Living Room Bulb'.lower()):
                on_off.l_bulb_off()
            if(device_off.lower()=='Living Room Fan'.lower()):
                on_off.l_fan_off()
            if(device_off.lower()=='Living Room AC'.lower()):
                on_off.l_AC_off()
            if(device_off.lower()=='Motor Pump'.lower()):
                on_off.motor_off()
    return reply1+" "+reply2


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Hi! It is a project by GEC NWD group3. I am AI enabled bot. I can answer your basic query as well as switch on or off the equipment of home.")
async def echo(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text=GoogleGenAI(update.message.text))

if __name__=='__main__':
   telegramservices()
   application=ApplicationBuilder().token(key.api_key).build()
   start_handler=CommandHandler('start',start)
   echo_handler=MessageHandler(filters.TEXT & (~filters.COMMAND),echo)

   application.add_handler(start_handler)
   application.add_handler(echo_handler)
   
   application.run_polling()
