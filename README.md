[![Build Status](https://travis-ci.org/joragupra/weathy.svg?branch=master)](https://travis-ci.org/joragupra/weathy)

# Weathy

Weathy is a library to get the weather information in your current location.

## Quick start

Here is a quick code example on how to use Weathy:


    import weathy.service

    prompt_information = weathy.service.PromptWeather().retrieve_weather()

    print('Greetings from beautiful ' + prompt_information.city + '!')
    print('The current temperature is ' + str(prompt_information.temperature) + ' C')
    print('and the weather conditions are ' + prompt_information.conditions)

This will show you:

    Greetings from beautiful Ashburn!
    The current temperature is 1.24 C
    and the weather conditions are overcast clouds

## Author / Contact information

Jorge Agudo Praena

joragupra@gmail.com